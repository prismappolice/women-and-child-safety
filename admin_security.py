import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask import session, redirect, url_for
import time

def init_admin_security_db():
    """Initialize the admin security tables"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Create table for admin security questions
    c.execute('''CREATE TABLE IF NOT EXISTS admin_security (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question1 TEXT NOT NULL,
        answer1_hash TEXT NOT NULL,
        question2 TEXT NOT NULL,
        answer2_hash TEXT NOT NULL,
        question3 TEXT NOT NULL,
        answer3_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    conn.commit()
    conn.close()

def hash_answer(answer):
    """Hash a security answer"""
    return generate_password_hash(answer.lower().strip())

def verify_answer(stored_hash, provided_answer):
    """Verify a security answer"""
    return check_password_hash(stored_hash, provided_answer.lower().strip())

def set_security_questions(question1, answer1, question2, answer2, question3, answer3):
    """Set or update security questions and answers"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Hash the answers
    answer1_hash = hash_answer(answer1)
    answer2_hash = hash_answer(answer2)
    answer3_hash = hash_answer(answer3)
    
    # Check if questions exist
    c.execute('SELECT id FROM admin_security LIMIT 1')
    exists = c.fetchone()
    
    if exists:
        # Update existing questions
        c.execute('''UPDATE admin_security SET 
            question1 = ?, answer1_hash = ?,
            question2 = ?, answer2_hash = ?,
            question3 = ?, answer3_hash = ?
            WHERE id = ?''', 
            (question1, answer1_hash, question2, answer2_hash, 
             question3, answer3_hash, exists[0]))
    else:
        # Insert new questions
        c.execute('''INSERT INTO admin_security 
            (question1, answer1_hash, question2, answer2_hash, question3, answer3_hash)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (question1, answer1_hash, question2, answer2_hash, question3, answer3_hash))
    
    conn.commit()
    conn.close()
    return True

def verify_security_questions(answers):
    """Verify security answers during password reset"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('''SELECT answer1_hash, answer2_hash, answer3_hash 
                 FROM admin_security LIMIT 1''')
    stored = c.fetchone()
    conn.close()
    
    if not stored:
        return False
        
    # Verify all three answers
    return (verify_answer(stored[0], answers[0]) and
            verify_answer(stored[1], answers[1]) and
            verify_answer(stored[2], answers[2]))

def get_security_questions():
    """Get the security questions and answer hashes"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('''SELECT question1, question2, question3, 
                        answer1_hash, answer2_hash, answer3_hash 
                 FROM admin_security LIMIT 1''')
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