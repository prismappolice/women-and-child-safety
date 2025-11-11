"""
Check women_safety_db database
"""
import psycopg2

print("="*60)
print("Checking Database: women_safety_db")
print("="*60)

try:
    conn = psycopg2.connect(
        host='localhost',
        database='women_safety_db',
        user='postgres',
        password='postgres123',
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
        print(f"\n📊 Database has {len(tables)} tables:")
        for table in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
            count = cursor.fetchone()[0]
            print(f"  - {table[0]}: {count} rows")
        
        print("\n" + "="*60)
        print("⚠️  DATABASE ALREADY HAS DATA!")
        print("="*60)
        print("\nOptions:")
        print("1. DROP all tables and migrate fresh (CURRENT DATA WILL BE LOST)")
        print("2. Skip migration and use this PostgreSQL database")
        print("3. Create a NEW empty database for migration")
        
    else:
        print("\n✅ Database is EMPTY - Ready for migration!")
        print("\n" + "="*60)
        print("NEXT STEPS:")
        print("="*60)
        print("1. Create database schema")
        print("2. Migrate data from SQLite")
        print("\nRun: python migrate_to_postgresql.py")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"\n❌ Error: {e}")
