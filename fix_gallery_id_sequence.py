"""
Fix gallery_items ID column to use PostgreSQL sequence (SERIAL equivalent)
"""
from db_config import get_db_connection

conn = get_db_connection('main')
cursor = conn.cursor()

print("🔧 Fixing gallery_items ID column...")
print("=" * 80)

try:
    # Step 1: Find the current maximum ID
    cursor.execute("SELECT COALESCE(MAX(id), 0) FROM gallery_items")
    max_id = cursor.fetchone()[0]
    print(f"📊 Current maximum ID: {max_id}")
    
    # Step 2: Create a sequence for the ID column
    print("Creating sequence...")
    cursor.execute("""
        CREATE SEQUENCE IF NOT EXISTS gallery_items_id_seq
        START WITH 1
        INCREMENT BY 1
        NO MINVALUE
        NO MAXVALUE
        CACHE 1
    """)
    
    # Step 3: Set the sequence value to max_id + 1
    next_id = max_id + 1
    print(f"Setting sequence to start at {next_id}...")
    cursor.execute(f"SELECT setval('gallery_items_id_seq', {next_id}, false)")
    
    # Step 4: Set the column default to use the sequence
    print("Setting column default to use sequence...")
    cursor.execute("""
        ALTER TABLE gallery_items 
        ALTER COLUMN id SET DEFAULT nextval('gallery_items_id_seq')
    """)
    
    # Step 5: Associate the sequence with the column (so it gets dropped with the table)
    print("Associating sequence with column...")
    cursor.execute("""
        ALTER SEQUENCE gallery_items_id_seq OWNED BY gallery_items.id
    """)
    
    # Step 6: Fix the one record with NULL id
    print("Fixing NULL ID record...")
    cursor.execute("""
        UPDATE gallery_items 
        SET id = nextval('gallery_items_id_seq') 
        WHERE id IS NULL
    """)
    
    conn.commit()
    
    # Verify the fix
    print("\n✅ Verification:")
    cursor.execute("SELECT column_default FROM information_schema.columns WHERE table_name = 'gallery_items' AND column_name = 'id'")
    col_default = cursor.fetchone()[0]
    print(f"   Column default: {col_default}")
    
    cursor.execute("SELECT pg_get_serial_sequence('gallery_items', 'id')")
    seq_name = cursor.fetchone()[0]
    print(f"   Sequence name: {seq_name}")
    
    cursor.execute("SELECT id, title FROM gallery_items ORDER BY created_at DESC LIMIT 3")
    recent = cursor.fetchall()
    print(f"\n   Recent items:")
    for item in recent:
        print(f"     ID: {item[0]}, Title: {item[1]}")
    
    print("=" * 80)
    print("✅ gallery_items ID column fixed successfully!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    conn.rollback()
    import traceback
    traceback.print_exc()
finally:
    conn.close()
