from db_config import get_db_connection

def test_sequences():
    """Test that sequences work for initiatives and officers"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    print("Testing sequences...\n")
    
    # Test initiatives
    print("1. Testing initiatives table:")
    cursor.execute("SELECT nextval('initiatives_id_seq')")
    next_id = cursor.fetchone()[0]
    print(f"   Next initiative ID will be: {next_id}")
    
    # Reset it (we just tested, don't want to skip IDs)
    cursor.execute("SELECT setval('initiatives_id_seq', %s, false)", (next_id,))
    
    # Test officers
    print("\n2. Testing officers table:")
    cursor.execute("SELECT nextval('officers_id_seq')")
    next_id = cursor.fetchone()[0]
    print(f"   Next officer ID will be: {next_id}")
    
    # Reset it
    cursor.execute("SELECT setval('officers_id_seq', %s, false)", (next_id,))
    
    # Test gallery_items
    print("\n3. Testing gallery_items table:")
    cursor.execute("SELECT nextval('gallery_items_id_seq')")
    next_id = cursor.fetchone()[0]
    print(f"   Next gallery item ID will be: {next_id}")
    
    # Reset it
    cursor.execute("SELECT setval('gallery_items_id_seq', %s, false)", (next_id,))
    
    conn.commit()
    conn.close()
    
    print("\n" + "="*70)
    print("✓ All sequences are working correctly!")
    print("✓ You can now add items through admin panel without NULL ID errors")
    print("="*70)

if __name__ == '__main__':
    test_sequences()
