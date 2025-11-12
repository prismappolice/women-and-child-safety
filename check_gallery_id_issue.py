from db_config import get_db_connection

conn = get_db_connection('main')
cursor = conn.cursor()

# Check column info
cursor.execute("""
    SELECT column_name, data_type, column_default 
    FROM information_schema.columns 
    WHERE table_name = 'gallery_items' 
    AND column_name = 'id'
""")
col_info = cursor.fetchone()
print(f"ID Column info: {col_info}")

# Check if there's a sequence
cursor.execute("""
    SELECT pg_get_serial_sequence('gallery_items', 'id')
""")
seq = cursor.fetchone()
print(f"Sequence: {seq}")

# Check the last few IDs
cursor.execute("SELECT id, title FROM gallery_items ORDER BY created_at DESC LIMIT 5")
recent = cursor.fetchall()
print("\nRecent items:")
for item in recent:
    print(f"  ID: {item[0]}, Title: {item[1]}")

conn.close()
