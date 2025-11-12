from db_config import get_db_connection

def create_and_fix_sequences():
    """Create missing sequences and fix all table ID columns"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    tables = [
        'volunteers', 'gallery_items', 'pdf_resources', 'safety_tips',
        'initiatives', 'officers', 'success_stories', 'about_sections',
        'contact_info', 'events', 'faqs', 'home_content', 'leadership',
        'news', 'testimonials', 'users', 'vision_sections'
    ]
    
    print("Creating sequences and fixing ID columns...\n")
    
    for table in tables:
        try:
            sequence = f"{table}_id_seq"
            
            # Get max ID from table
            cursor.execute(f"SELECT MAX(id) FROM {table}")
            result = cursor.fetchone()
            max_id = result[0] if result and result[0] else 0
            next_val = max_id + 1
            
            # Try to create sequence (will fail if exists, that's OK)
            try:
                cursor.execute(f"CREATE SEQUENCE {sequence} START WITH {next_val}")
                print(f"  Created sequence: {sequence}")
            except:
                conn.rollback()
                # Sequence exists, just update it
                cursor.execute(f"SELECT setval('{sequence}', %s, false)", (next_val,))
                print(f"  Updated sequence: {sequence}")
            
            # Set default value for id column
            cursor.execute(f"""
                ALTER TABLE {table} 
                ALTER COLUMN id SET DEFAULT nextval('{sequence}')
            """)
            
            # Set sequence ownership
            cursor.execute(f"ALTER SEQUENCE {sequence} OWNED BY {table}.id")
            
            conn.commit()
            print(f"✓ {table}: max_id={max_id}, next_id={next_val}\n")
            
        except Exception as e:
            conn.rollback()
            print(f"✗ {table}: {e}\n")
    
    conn.close()
    
    print("="*70)
    print("All sequences created and configured!")
    print("Now you can add unlimited records to any table without NULL IDs.")
    print("="*70)

if __name__ == '__main__':
    create_and_fix_sequences()
