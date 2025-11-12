"""
Fix all tables with NULL IDs by creating proper sequences
"""
from db_config import get_db_connection

tables_to_fix = [
    'pdf_resources',
    'safety_tips',
    'initiatives',
    'about_content',
    'home_content',
    'contact_info',
    'officers',
    'success_stories'
]

conn = get_db_connection('main')
cursor = conn.cursor()

print("🔧 Fixing ID sequences for all tables...")
print("=" * 80)

for table_name in tables_to_fix:
    try:
        # Check if table exists
        cursor.execute(f"""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = '{table_name}'
            )
        """)
        
        if not cursor.fetchone()[0]:
            print(f"⏭️  {table_name}: Table doesn't exist, skipping")
            continue
        
        # Check for NULL IDs
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE id IS NULL")
        null_count = cursor.fetchone()[0]
        
        if null_count == 0:
            print(f"✅ {table_name}: No NULL IDs")
            continue
        
        print(f"\n📋 {table_name}:")
        print(f"   Found {null_count} record(s) with NULL ID")
        
        # Get max ID
        cursor.execute(f"SELECT COALESCE(MAX(id), 0) FROM {table_name}")
        max_id = cursor.fetchone()[0]
        print(f"   Current max ID: {max_id}")
        
        # Create sequence if doesn't exist
        sequence_name = f"{table_name}_id_seq"
        cursor.execute(f"""
            CREATE SEQUENCE IF NOT EXISTS {sequence_name}
            START WITH 1
            INCREMENT BY 1
            NO MINVALUE
            NO MAXVALUE
            CACHE 1
        """)
        
        # Set sequence value
        next_id = max_id + 1
        cursor.execute(f"SELECT setval('{sequence_name}', {next_id}, false)")
        
        # Set column default
        cursor.execute(f"""
            ALTER TABLE {table_name} 
            ALTER COLUMN id SET DEFAULT nextval('{sequence_name}')
        """)
        
        # Associate sequence with column
        cursor.execute(f"""
            ALTER SEQUENCE {sequence_name} OWNED BY {table_name}.id
        """)
        
        # Fix NULL IDs
        cursor.execute(f"""
            UPDATE {table_name} 
            SET id = nextval('{sequence_name}') 
            WHERE id IS NULL
        """)
        
        conn.commit()
        print(f"   ✅ Fixed! Sequence starts at {next_id}")
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        conn.rollback()

print("\n" + "=" * 80)
print("✅ All tables processed!")

conn.close()
