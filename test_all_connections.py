"""
Try different database configurations
"""
import psycopg2

configs = [
    {'db': 'postgres', 'desc': 'Default postgres database'},
    {'db': 'womensafety_db', 'desc': 'womensafety_db'},
    {'db': 'women_safety', 'desc': 'women_safety'},
]

password = 'postgres123'

print("="*60)
print("Testing PostgreSQL Connections")
print("="*60)

for config in configs:
    print(f"\n🔄 Testing: {config['desc']}")
    try:
        conn = psycopg2.connect(
            host='localhost',
            database=config['db'],
            user='postgres',
            password=password,
            port=5432
        )
        
        cursor = conn.cursor()
        cursor.execute("SELECT current_database(), current_user;")
        db_name, user = cursor.fetchone()
        
        print(f"✅ Connected!")
        print(f"   Database: {db_name}")
        print(f"   User: {user}")
        
        # List all databases
        if config['db'] == 'postgres':
            cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
            databases = cursor.fetchall()
            print(f"\n   Available databases:")
            for db in databases:
                print(f"   - {db[0]}")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Failed: {str(e)[:100]}")

print("\n" + "="*60)
