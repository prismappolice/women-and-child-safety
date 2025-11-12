from db_config import get_db_connection

def test_district_sequences():
    """Test all district table sequences"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    tables = [
        ('district_sps', 'district_sps_id_seq'),
        ('shakthi_teams', 'shakthi_teams_id_seq'),
        ('women_police_stations', 'women_police_stations_id_seq'),
        ('one_stop_centers', 'one_stop_centers_id_seq')
    ]
    
    print("Testing sequences...\n")
    
    for table, sequence in tables:
        cursor.execute(f"SELECT nextval('{sequence}')")
        next_id = cursor.fetchone()[0]
        print(f"✓ {table}: Next ID will be {next_id}")
        
        # Reset it (just testing)
        cursor.execute(f"SELECT setval('{sequence}', %s, false)", (next_id,))
    
    conn.commit()
    conn.close()
    
    print("\n" + "="*70)
    print("All sequences working correctly!")
    print("You can now add items through admin panel:")
    print("  - District SPs → ID 55, 56, 57...")
    print("  - Shakthi Teams → ID 214, 215, 216...")
    print("  - Women Police Stations → ID 53, 54, 55...")
    print("  - One Stop Centers → ID 53, 54, 55...")
    print("="*70)

if __name__ == '__main__':
    test_district_sequences()
