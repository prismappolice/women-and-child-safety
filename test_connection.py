"""
Interactive PostgreSQL Connection Test
Will prompt for password securely
"""
import psycopg2
import getpass

print("="*60)
print("PostgreSQL Connection Test")
print("="*60)

# Database details
print("\nDatabase: womensafety_db")
print("User: postgres")
print("Host: localhost")
print("Port: 5432")

# Get password securely
password = getpass.getpass("\nEnter password for postgres user: ")

try:
    print("\n🔄 Connecting to database...")
    
    conn = psycopg2.connect(
        host='localhost',
        database='womensafety_db',
        user='postgres',
        password=password,
        port=5432
    )
    
    cursor = conn.cursor()
    
    print("✅ Connection successful!")
    
    # Check PostgreSQL version
    cursor.execute("SELECT version();")
    version = cursor.fetchone()[0]
    print(f"\n📊 PostgreSQL Version:")
    print(f"   {version[:80]}...")
    
    # Check tables
    cursor.execute("""
        SELECT COUNT(*) 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
    """)
    table_count = cursor.fetchone()[0]
    print(f"\n📁 Tables in database: {table_count}")
    
    if table_count > 0:
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name
            LIMIT 10
        """)
        tables = cursor.fetchall()
        print("\n   First 10 tables:")
        for table in tables:
            print(f"   - {table[0]}")
    
    cursor.close()
    conn.close()
    
    # Save configuration
    print("\n" + "="*60)
    save = input("\n✅ Connection successful! Save password to config? (yes/no): ")
    
    if save.lower() == 'yes':
        # Update migrate_to_postgresql.py
        with open('migrate_to_postgresql.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace("'password': 'Womensafety2025!',", f"'password': '{password}',")
        
        with open('migrate_to_postgresql.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Update db_config.py
        with open('db_config.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace("'password': os.getenv('PG_PASSWORD', 'Womensafety2025!'),", 
                                 f"'password': os.getenv('PG_PASSWORD', '{password}'),")
        content = content.replace("'password': os.getenv('PG_ADMIN_PASSWORD', 'Womensafety2025!'),", 
                                 f"'password': os.getenv('PG_ADMIN_PASSWORD', '{password}'),")
        
        with open('db_config.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("\n✅ Configuration files updated!")
        print("   - migrate_to_postgresql.py")
        print("   - db_config.py")
        
        print("\n" + "="*60)
        print("🎉 READY FOR MIGRATION!")
        print("="*60)
        
        if table_count > 0:
            print("\n⚠️  WARNING: Database already has tables!")
            print("\nOptions:")
            print("1. Drop existing tables and migrate fresh (WILL LOSE EXISTING DATA)")
            print("2. Migrate to a new empty database")
            print("3. Check if we can use existing tables")
        else:
            print("\n✅ Database is empty - ready for schema creation")
            print("\nNext steps:")
            print("1. Create schemas: Run schema SQL files")
            print("2. Migrate data: python migrate_to_postgresql.py")
    
except psycopg2.OperationalError as e:
    print(f"\n❌ Connection failed!")
    print(f"   Error: {e}")
    print("\nPlease check:")
    print("1. Password is correct")
    print("2. Database 'womensafety_db' exists")
    print("3. PostgreSQL service is running")
    print("4. User 'postgres' has access to this database")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
