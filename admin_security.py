import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask import session, redirect, url_for
import time

def init_admin_security_db():
    """Initialize the admin security tables"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Create table for admin security questions - Updated for multiple admin support
    c.execute('''CREATE TABLE IF NOT EXISTS admin_security (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        admin_id INTEGER NOT NULL,
        question1 TEXT NOT NULL,
        answer1_hash TEXT NOT NULL,
        question2 TEXT NOT NULL,
        answer2_hash TEXT NOT NULL,
        question3 TEXT NOT NULL,
        answer3_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (admin_id) REFERENCES admin_credentials (id) ON DELETE CASCADE
    )''')
    
    # Create index for faster lookups (only if table exists)
    try:
        c.execute('''CREATE INDEX IF NOT EXISTS idx_admin_security_admin_id 
                     ON admin_security (admin_id)''')
    except sqlite3.OperationalError:
        # Index creation might fail during initial setup, that's OK
        pass
    
    conn.commit()
    conn.close()

def hash_answer(answer):
    """Hash a security answer"""
    return generate_password_hash(answer.lower().strip())

def verify_answer(stored_hash, provided_answer):
    """Verify a security answer"""
    return check_password_hash(stored_hash, provided_answer.lower().strip())

def set_security_questions(question1, answer1, question2, answer2, question3, answer3, admin_id=None, conn=None):
    """Set or update security questions and answers for specific admin"""
    # Allow using existing connection to prevent database locking
    if conn is None:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        close_conn = True
    else:
        c = conn.cursor()
        close_conn = False
    
    # If admin_id not provided, get from session or use default (for backward compatibility)
    if admin_id is None:
        # For backward compatibility, get the first admin ID or create default
        c.execute('SELECT id FROM admin_credentials LIMIT 1')
        admin_record = c.fetchone()
        if admin_record:
            admin_id = admin_record[0]
        else:
            # No admin found
            if close_conn:
                conn.close()
            return False
    
    # Hash the answers
    answer1_hash = hash_answer(answer1)
    answer2_hash = hash_answer(answer2)
    answer3_hash = hash_answer(answer3)
    
    # Check if record exists for this admin
    c.execute('SELECT id FROM admin_security WHERE admin_id = ?', (admin_id,))
    existing = c.fetchone()
    
    if existing:
        # Update existing record
        c.execute('''UPDATE admin_security 
            SET question1=?, answer1_hash=?, question2=?, answer2_hash=?, question3=?, answer3_hash=?, updated_at=CURRENT_TIMESTAMP
            WHERE admin_id=?''',
            (question1, answer1_hash, question2, answer2_hash, question3, answer3_hash, admin_id))
    else:
        # Insert new record with admin_id
        c.execute('''INSERT INTO admin_security 
            (admin_id, question1, answer1_hash, question2, answer2_hash, question3, answer3_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (admin_id, question1, answer1_hash, question2, answer2_hash, question3, answer3_hash))
    
    if close_conn:
        conn.commit()
        conn.close()
    return True

def verify_security_questions(answers, admin_id=None):
    """Verify security answers during password reset for specific admin"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # If admin_id not provided, get the first admin (backward compatibility)
    if admin_id is None:
        c.execute('SELECT id FROM admin_credentials LIMIT 1')
        admin_record = c.fetchone()
        if admin_record:
            admin_id = admin_record[0]
        else:
            conn.close()
            return False
    
    c.execute('''SELECT answer1_hash, answer2_hash, answer3_hash 
                 FROM admin_security WHERE admin_id = ?''', (admin_id,))
    stored = c.fetchone()
    conn.close()
    
    if not stored:
        return False
        
    # Verify all three answers
    return (verify_answer(stored[0], answers[0]) and
            verify_answer(stored[1], answers[1]) and
            verify_answer(stored[2], answers[2]))

def get_security_questions(admin_id=None):
    """Get the security questions for specific admin"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # If admin_id not provided, get the first admin (backward compatibility)
    if admin_id is None:
        c.execute('SELECT id FROM admin_credentials LIMIT 1')
        admin_record = c.fetchone()
        if admin_record:
            admin_id = admin_record[0]
        else:
            conn.close()
            return None
    
    c.execute('''SELECT question1, question2, question3, 
                        answer1_hash, answer2_hash, answer3_hash 
                 FROM admin_security WHERE admin_id = ?''', (admin_id,))
    data = c.fetchone()
    conn.close()
    
    if data:
        return {
            'question1': data[0],
            'question2': data[1],
            'question3': data[2],
            'answer1_hash': data[3],
            'answer2_hash': data[4],
            'answer3_hash': data[5]
        }
    return None

def get_admin_id_by_username(username):
    """Get admin ID by username - helper function for password recovery"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('SELECT id FROM admin_credentials WHERE username = ?', (username,))
    admin = c.fetchone()
    conn.close()
    
    return admin[0] if admin else None

# Session timeout decorator
def check_session_timeout(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_last_activity' not in session:
            return redirect(url_for('admin_login'))
        
        last_activity = session.get('admin_last_activity')
        if time.time() - last_activity > 900:  # 15 minutes
            session.clear()
            return redirect(url_for('admin_login'))
            
        session['admin_last_activity'] = time.time()
        return f(*args, **kwargs)
    return decorated_function