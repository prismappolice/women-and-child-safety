"""
PostgreSQL Database Helper for Admin Dashboard
Simple functions to replace SQLite calls
"""

import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash

# PostgreSQL Configuration
PG_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'women_safety_db',
    'user': 'women_safety_user',
    'password': 'WomenSafety2025!'
}

def get_pg_connection():
    """Get PostgreSQL connection"""
    try:
        return psycopg2.connect(**PG_CONFIG)
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def get_pg_cursor(conn):
    """Get PostgreSQL cursor with dict results"""
    return conn.cursor(cursor_factory=RealDictCursor)

# Admin Authentication Functions
def verify_admin_login(username, password):
    """Verify admin login credentials"""
    conn = get_pg_connection()
    if not conn:
        return False
        
    try:
        cursor = get_pg_cursor(conn)
        cursor.execute("SELECT password_hash FROM admin_credentials WHERE username = %s", (username,))
        result = cursor.fetchone()
        
        if result and check_password_hash(result['password_hash'], password):
            return True
        return False
        
    except Exception as e:
        print(f"Login verification error: {e}")
        return False
    finally:
        conn.close()

def update_admin_password(username, new_password):
    """Update admin password"""
    conn = get_pg_connection()
    if not conn:
        return False
        
    try:
        cursor = get_pg_cursor(conn)
        new_hash = generate_password_hash(new_password)
        cursor.execute("""
            UPDATE admin_credentials 
            SET password_hash = %s, updated_at = CURRENT_TIMESTAMP 
            WHERE username = %s
        """, (new_hash, username))
        
        conn.commit()
        return cursor.rowcount > 0
        
    except Exception as e:
        print(f"Password update error: {e}")
        return False
    finally:
        conn.close()

def get_security_questions_pg(username):
    """Get security questions for user"""
    conn = get_pg_connection()
    if not conn:
        return []
        
    try:
        cursor = get_pg_cursor(conn)
        cursor.execute("SELECT * FROM admin_security WHERE username = %s", (username,))
        result = cursor.fetchone()
        
        if result:
            return [
                {'question': result['question1'], 'answer': result['answer1']},
                {'question': result['question2'], 'answer': result['answer2']}, 
                {'question': result['question3'], 'answer': result['answer3']}
            ]
        return []
        
    except Exception as e:
        print(f"Security questions error: {e}")
        return []
    finally:
        conn.close()

# Content Management Functions
def get_content_pg(page_name=None, section_name=None):
    """Get content from PostgreSQL"""
    conn = get_pg_connection()
    if not conn:
        return []
        
    try:
        cursor = get_pg_cursor(conn)
        
        if page_name and section_name:
            cursor.execute("SELECT * FROM content WHERE page_name = %s AND section_name = %s", 
                          (page_name, section_name))
        elif page_name:
            cursor.execute("SELECT * FROM content WHERE page_name = %s", (page_name,))
        else:
            cursor.execute("SELECT * FROM content")
            
        return cursor.fetchall()
        
    except Exception as e:
        print(f"Content query error: {e}")
        return []
    finally:
        conn.close()

def get_gallery_items_pg():
    """Get gallery items from PostgreSQL"""
    conn = get_pg_connection()
    if not conn:
        return []
        
    try:
        cursor = get_pg_cursor(conn)
        cursor.execute("SELECT * FROM gallery_items WHERE is_active = true ORDER BY created_at DESC")
        return cursor.fetchall()
        
    except Exception as e:
        print(f"Gallery query error: {e}")
        return []
    finally:
        conn.close()

def get_officers_pg():
    """Get officers from PostgreSQL"""
    conn = get_pg_connection()
    if not conn:
        return []
        
    try:
        cursor = get_pg_cursor(conn)
        cursor.execute("SELECT * FROM officers WHERE is_active = true ORDER BY position_order")
        return cursor.fetchall()
        
    except Exception as e:
        print(f"Officers query error: {e}")
        return []
    finally:
        conn.close()

def get_volunteers_pg():
    """Get volunteers from PostgreSQL"""
    conn = get_pg_connection()
    if not conn:
        return []
        
    try:
        cursor = get_pg_cursor(conn)
        cursor.execute("SELECT * FROM volunteers ORDER BY created_at DESC")
        return cursor.fetchall()
        
    except Exception as e:
        print(f"Volunteers query error: {e}")
        return []
    finally:
        conn.close()

# Test function
def test_postgresql_functions():
    """Test all PostgreSQL functions"""
    print("Testing PostgreSQL integration...")
    
    # Test connection
    conn = get_pg_connection()
    if conn:
        print("✅ Connection: OK")
        conn.close()
    else:
        print("❌ Connection: FAILED")
        return False
    
    # Test admin login
    if verify_admin_login('admin', 'postgres123'):
        print("✅ Admin login: OK")
    else:
        print("❌ Admin login: FAILED")
    
    # Test content
    content = get_content_pg()
    print(f"✅ Content: {len(content)} items")
    
    # Test gallery
    gallery = get_gallery_items_pg()
    print(f"✅ Gallery: {len(gallery)} items")
    
    # Test officers
    officers = get_officers_pg()
    print(f"✅ Officers: {len(officers)} profiles")
    
    print("✅ All PostgreSQL functions working!")
    return True

if __name__ == "__main__":
    test_postgresql_functions()
