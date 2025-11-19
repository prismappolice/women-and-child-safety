import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='women_safety_db',
    user='postgres',
    password='postgres123',
    port='5432'
)
cursor = conn.cursor()

# Check if table exists
cursor.execute("""
    SELECT EXISTS (
        SELECT FROM information_schema.tables 
        WHERE table_name = 'upcoming_events'
    )
""")
exists = cursor.fetchone()[0]
print(f"✅ upcoming_events table exists: {exists}")

if exists:
    # Get count
    cursor.execute("SELECT COUNT(*) FROM upcoming_events")
    count = cursor.fetchone()[0]
    print(f"📊 Total records: {count}")
    
    # Get structure
    cursor.execute("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'upcoming_events'
        ORDER BY ordinal_position
    """)
    columns = cursor.fetchall()
    print(f"\n📝 Table structure:")
    for col, dtype in columns:
        print(f"   - {col}: {dtype}")
    
    # Get sample data
    if count > 0:
        cursor.execute("SELECT * FROM upcoming_events LIMIT 3")
        rows = cursor.fetchall()
        print(f"\n📄 Sample data:")
        for row in rows:
            print(f"   {row}")
else:
    print("❌ Table does not exist - need to create it")

conn.close()
