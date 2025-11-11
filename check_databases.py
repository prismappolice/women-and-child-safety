"""
Check existing databases and connect with women_safety_user
"""
import psycopg2

print("="*60)
print("Testing Database Connection")
print("="*60)

# Test with women_safety database directly
configs = [
    {
        'name': 'women_safety',
        'host': 'localhost',
        'database': 'women_safety',
        'user': 'women_safety_user',
        'password': 'postgres',
        'port': 5432
    },
    {
        'name': 'admin_db',
        'host': 'localhost',
        'database': 'admin_db',
        'user': 'women_safety_user',
        'password': 'postgres',
        'port': 5432
    }
]

for config in configs:
    print(f"\n📊 Testing connection to '{config['name']}'...")
    try:
        conn = psycopg2.connect(
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password'],
            port=config['port']
        )
        
        cursor = conn.cursor()
        
        # Count tables
        cursor.execute("""
            SELECT COUNT(*) 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        table_count = cursor.fetchone()[0]
        
        print(f"✅ Connected to '{config['name']}'")
        print(f"   Tables: {table_count}")
        
        cursor.close()
        conn.close()
        
    except psycopg2.OperationalError as e:
        if "does not exist" in str(e):
            print(f"⚠️  Database '{config['name']}' does not exist - needs to be created")
        else:
            print(f"❌ Connection failed: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

print("\n" + "="*60)
print("Connection Test Complete")
print("="*60)
