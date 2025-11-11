"""
Test PostgreSQL Connection
"""
import psycopg2
import getpass

print("="*60)
print("PostgreSQL Connection Test")
print("="*60)

# Get password from user
password = getpass.getpass("\nEnter PostgreSQL password for user 'postgres': ")

try:
    # Try to connect
    conn = psycopg2.connect(
        host='localhost',
        database='postgres',  # Default database
        user='postgres',
        password=password,
        port=5432
    )
    
    print("\n✅ Connection successful!")
    
    # Get PostgreSQL version
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()[0]
    print(f"\n📊 PostgreSQL Version:\n{version}")
    
    # List databases
    cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    databases = cursor.fetchall()
    print(f"\n📁 Existing Databases:")
    for db in databases:
        print(f"  - {db[0]}")
    
    cursor.close()
    conn.close()
    
    # Save password to config
    print("\n" + "="*60)
    save = input("\nSave this password to configuration files? (yes/no): ")
    
    if save.lower() == 'yes':
        # Update migrate_to_postgresql.py
        with open('migrate_to_postgresql.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace(
            "'password': 'your_password_here',  # Change this",
            f"'password': '{password}',"
        )
        
        with open('migrate_to_postgresql.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Updated: migrate_to_postgresql.py")
        
        # Update db_config.py
        with open('db_config.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace(
            "'password': os.getenv('PG_PASSWORD', 'your_password_here'),",
            f"'password': os.getenv('PG_PASSWORD', '{password}'),"
        )
        content = content.replace(
            "'password': os.getenv('PG_ADMIN_PASSWORD', 'your_password_here'),",
            f"'password': os.getenv('PG_ADMIN_PASSWORD', '{password}'),"
        )
        
        with open('db_config.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Updated: db_config.py")
        
        print("\n🎉 Configuration files updated successfully!")
        print("\nNext step: Run migration")
        print("Command: python migrate_to_postgresql.py")
    
except psycopg2.OperationalError as e:
    print(f"\n❌ Connection failed: {e}")
    print("\nPlease check:")
    print("1. PostgreSQL service is running")
    print("2. Password is correct")
    print("3. Port 5432 is accessible")
except Exception as e:
    print(f"\n❌ Error: {e}")
