"""
Database Configuration
Supports both SQLite and PostgreSQL
"""

import os

# Database Mode: 'sqlite' or 'postgresql'
DB_MODE = os.getenv('DB_MODE', 'postgresql')  # Using PostgreSQL (migration completed!)

# SQLite Configuration
SQLITE_CONFIG = {
    'main_db': 'women_safety.db',
    'admin_db': 'database.db',
    'volunteer_db': 'volunteer_system.db'
}

# PostgreSQL Configuration
POSTGRESQL_CONFIG = {
    'main_db': {
        'host': os.getenv('PG_HOST', 'localhost'),
        'database': os.getenv('PG_DATABASE', 'women_safety_db'),
        'user': os.getenv('PG_USER', 'postgres'),
        'password': os.getenv('PG_PASSWORD', 'postgres123'),
        'port': int(os.getenv('PG_PORT', 5432))
    },
    'admin_db': {
        'host': os.getenv('PG_ADMIN_HOST', 'localhost'),
        'database': os.getenv('PG_ADMIN_DATABASE', 'women_safety_db'),
        'user': os.getenv('PG_ADMIN_USER', 'postgres'),
        'password': os.getenv('PG_ADMIN_PASSWORD', 'postgres123'),
        'port': int(os.getenv('PG_ADMIN_PORT', 5432))
    }
}

def get_db_connection(db_type='main'):
    """
    Get database connection based on current mode
    
    Args:
        db_type: 'main', 'admin', or 'volunteer'
    
    Returns:
        Database connection object
    """
    if DB_MODE == 'sqlite':
        import sqlite3
        if db_type == 'main':
            return sqlite3.connect(SQLITE_CONFIG['main_db'])
        elif db_type == 'admin':
            return sqlite3.connect(SQLITE_CONFIG['admin_db'])
        elif db_type == 'volunteer':
            return sqlite3.connect(SQLITE_CONFIG['volunteer_db'])
    
    elif DB_MODE == 'postgresql':
        import psycopg2
        from psycopg2.extras import RealDictCursor
        
        if db_type in ['main', 'volunteer']:
            return psycopg2.connect(**POSTGRESQL_CONFIG['main_db'])
        elif db_type == 'admin':
            return psycopg2.connect(**POSTGRESQL_CONFIG['admin_db'])
    
    raise ValueError(f"Invalid database type: {db_type}")

def get_placeholder():
    """
    Get correct placeholder for parameterized queries
    SQLite uses ?, PostgreSQL uses %s
    """
    return '?' if DB_MODE == 'sqlite' else '%s'

def adapt_query(query):
    """
    Adapt query from SQLite syntax to PostgreSQL syntax
    
    Args:
        query: SQL query string
    
    Returns:
        Adapted query string
    """
    if DB_MODE == 'postgresql':
        # Replace ? with %s for PostgreSQL
        adapted = query.replace('?', '%s')
        
        # Replace AUTOINCREMENT with SERIAL (for schema creation)
        adapted = adapted.replace('AUTOINCREMENT', 'SERIAL')
        
        # Replace INTEGER PRIMARY KEY AUTOINCREMENT with SERIAL PRIMARY KEY
        adapted = adapted.replace('INTEGER PRIMARY KEY AUTOINCREMENT', 'SERIAL PRIMARY KEY')
        
        return adapted
    
    return query

def execute_query(conn, query, params=None, fetchone=False, fetchall=False):
    """
    Execute a database query with proper parameter binding
    
    Args:
        conn: Database connection
        query: SQL query string
        params: Query parameters tuple
        fetchone: Return single row
        fetchall: Return all rows
    
    Returns:
        Query results or cursor
    """
    cursor = conn.cursor()
    
    # Adapt query for PostgreSQL
    adapted_query = adapt_query(query)
    
    if params:
        cursor.execute(adapted_query, params)
    else:
        cursor.execute(adapted_query)
    
    if fetchone:
        return cursor.fetchone()
    elif fetchall:
        return cursor.fetchall()
    else:
        return cursor

def close_connection(conn, commit=True):
    """
    Properly close database connection
    
    Args:
        conn: Database connection
        commit: Whether to commit before closing
    """
    if commit:
        conn.commit()
    conn.close()

# Helper function for getting last inserted ID
def get_last_insert_id(cursor):
    """
    Get last inserted ID (works for both SQLite and PostgreSQL)
    
    Args:
        cursor: Database cursor
    
    Returns:
        Last inserted ID
    """
    if DB_MODE == 'sqlite':
        return cursor.lastrowid
    elif DB_MODE == 'postgresql':
        cursor.execute("SELECT lastval()")
        return cursor.fetchone()[0]
    
    return None

# Database initialization check
def check_db_connection():
    """
    Check if database connection is working
    
    Returns:
        Boolean indicating connection status
    """
    try:
        conn = get_db_connection('main')
        conn.close()
        return True
    except Exception as e:
        print(f"Database connection error: {e}")
        return False

# Environment configuration
def set_database_mode(mode):
    """
    Set database mode
    
    Args:
        mode: 'sqlite' or 'postgresql'
    """
    global DB_MODE
    if mode in ['sqlite', 'postgresql']:
        DB_MODE = mode
        os.environ['DB_MODE'] = mode
        print(f"Database mode set to: {mode}")
    else:
        raise ValueError("Mode must be 'sqlite' or 'postgresql'")

# For backward compatibility
def get_sqlite_connection(db_file):
    """Legacy function for direct SQLite connection"""
    import sqlite3
    return sqlite3.connect(db_file)

def get_postgresql_connection(config):
    """Legacy function for direct PostgreSQL connection"""
    import psycopg2
    return psycopg2.connect(**config)
