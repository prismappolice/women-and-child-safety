"""
Create PostgreSQL Databases
"""
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

print("="*60)
print("Creating PostgreSQL Databases")
print("="*60)

# Connection parameters
params = {
    'host': 'localhost',
    'database': 'postgres',  # Connect to default database
    'user': 'women_safety_user',
    'password': 'postgres',
    'port': 5432
}

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(**params)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    
    print("\n✅ Connected to PostgreSQL")
    
    # Create women_safety database
    print("\n📊 Creating 'women_safety' database...")
    try:
        cursor.execute("CREATE DATABASE women_safety;")
        print("✅ Database 'women_safety' created successfully")
    except psycopg2.errors.DuplicateDatabase:
        print("⚠️  Database 'women_safety' already exists")
    
    # Create admin_db database
    print("\n📊 Creating 'admin_db' database...")
    try:
        cursor.execute("CREATE DATABASE admin_db;")
        print("✅ Database 'admin_db' created successfully")
    except psycopg2.errors.DuplicateDatabase:
        print("⚠️  Database 'admin_db' already exists")
    
    cursor.close()
    conn.close()
    
    print("\n" + "="*60)
    print("✅ Database creation completed!")
    print("="*60)
    print("\nNext step: Create database schemas")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nPlease check:")
    print("1. PostgreSQL service is running")
    print("2. Password is correct: postgres123")
    print("3. User 'postgres' has database creation privileges")
