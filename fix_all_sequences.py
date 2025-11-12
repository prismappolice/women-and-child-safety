from db_config import get_db_connection

def fix_all_sequences():
    """Fix all table sequences to prevent NULL IDs when inserting new records"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    tables_to_fix = [
        ('volunteers', 'volunteers_id_seq'),
        ('gallery_items', 'gallery_items_id_seq'),
        ('pdf_resources', 'pdf_resources_id_seq'),
        ('safety_tips', 'safety_tips_id_seq'),
        ('initiatives', 'initiatives_id_seq'),
        ('officers', 'officers_id_seq'),
        ('success_stories', 'success_stories_id_seq'),
        ('about_sections', 'about_sections_id_seq'),
        ('contact_info', 'contact_info_id_seq'),
        ('events', 'events_id_seq'),
        ('faqs', 'faqs_id_seq'),
        ('home_content', 'home_content_id_seq'),
        ('leadership', 'leadership_id_seq'),
        ('news', 'news_id_seq'),
        ('testimonials', 'testimonials_id_seq'),
        ('users', 'users_id_seq'),
        ('vision_sections', 'vision_sections_id_seq')
    ]
    
    print("Fixing sequences for all tables...\n")
    
    for table, sequence in tables_to_fix:
        try:
            # Get max ID from table
            cursor.execute(f"SELECT MAX(id) FROM {table}")
            result = cursor.fetchone()
            max_id = result[0] if result and result[0] else 0
            
            # Set sequence to max_id + 1
            next_val = max_id + 1
            cursor.execute(f"SELECT setval('{sequence}', %s, false)", (next_val,))
            
            print(f"✓ {table}: max_id={max_id}, sequence set to {next_val}")
            
        except Exception as e:
            print(f"✗ {table}: {e}")
    
    conn.commit()
    conn.close()
    
    print("\n" + "="*70)
    print("All sequences fixed! Now you can add any number of records safely.")
    print("="*70)

if __name__ == '__main__':
    fix_all_sequences()
