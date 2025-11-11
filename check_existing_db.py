"""
Check existing PostgreSQL database structure
"""
import psycopg2

print("="*60)
print("Checking Existing Database: womensafety_db")
print("="*60)

try:
    conn = psycopg2.connect(
        host='localhost',
        database='womensafety_db',
        user='postgres',
        password='Womensafety2025!',
        port=5432
    )
    
    cursor = conn.cursor()
    
    print("\n✅ Connected successfully!")
    
    # Check tables
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
        ORDER BY table_name
    """)
    tables = cursor.fetchall()
    
    if tables:
        print(f"\n📊 Found {len(tables)} tables:")
        for table in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
            count = cursor.fetchone()[0]
            print(f"  - {table[0]}: {count} rows")
    else:
        print("\n⚠️  No tables found - database is empty")
        print("   We need to create schemas first")
    
    cursor.close()
    conn.close()
    
    print("\n" + "="*60)
    if tables:
        print("✅ Database exists with tables")
        print("\n⚠️  WARNING: Database already has tables!")
        print("\nOptions:")
        print("1. DROP existing tables and recreate (DATA WILL BE LOST)")
        print("2. Check if tables match our schema")
        print("3. Use this database as-is")
    else:
        print("✅ Database exists but empty - Ready for schema creation")
    print("="*60)
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nPlease check:")
    print("1. Database 'womensafety_db' exists")
    print("2. Password is correct: Womensafety2025!")
    print("3. User 'postgres' has access")
