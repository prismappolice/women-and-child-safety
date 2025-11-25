"""
Database Configuration Module
Handles PostgreSQL database connections and query adaptation
"""
import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection(db_type='main'):
    """
    Get PostgreSQL database connection
    
    Args:
        db_type: Type of database ('main' or 'admin')
    
    Returns:
        PostgreSQL connection object
    """
    # Get database configuration from environment variables or use defaults
    db_name = os.environ.get('DB_NAME', 'women_safety_db')
    db_user = os.environ.get('DB_USER', 'postgres')
    db_password = os.environ.get('DB_PASSWORD', 'postgres123')
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', '5432')
    
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        raise

def adapt_query(query):
    """
    Adapt SQL query from SQLite syntax (?) to PostgreSQL syntax (%s)
    
    Args:
        query: SQL query string with ? placeholders
    
    Returns:
        SQL query string with %s placeholders for PostgreSQL
    """
    # Replace ? with %s for PostgreSQL
    return query.replace('?', '%s')
