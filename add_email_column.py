import psycopg2
from db_config import get_db_connection

def add_email_column():
    """Add email column to admin_credentials table"""
    conn = None
    try:
        conn = get_db_connection('admin')
        cur = conn.cursor()
        
        # Check if email column exists
        cur.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name='admin_credentials' AND column_name='email'
        """)
        
        if cur.fetchone():
            print("✅ Email column already exists!")
        else:
            # Add email column
            print("Adding email column to admin_credentials table...")
            cur.execute("""
                ALTER TABLE admin_credentials 
                ADD COLUMN email VARCHAR(255)
            """)
            conn.commit()
            print("✅ Email column added successfully!")
        
        # Show current admin data
        print("\n📋 Current admin credentials:")
        cur.execute("SELECT id, username, email FROM admin_credentials")
        rows = cur.fetchall()
        for row in rows:
            print(f"   ID: {row[0]}, Username: {row[1]}, Email: {row[2]}")
        
        cur.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    add_email_column()
