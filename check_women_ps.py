from db_config import get_db_connection

def check_women_ps():
    """Check women police stations data"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    # Check all women police stations
    cursor.execute("""
        SELECT id, station_name, incharge_name, contact_number, district_id, is_active, created_at
        FROM women_police_stations
        ORDER BY id DESC
        LIMIT 10
    """)
    stations = cursor.fetchall()
    
    print(f"Recent Women Police Stations (Last 10):\n")
    
    for station in stations:
        print(f"ID: {station[0]}")
        print(f"Station: {station[1]}")
        print(f"Incharge: {station[2]}")
        print(f"Contact: {station[3]}")
        print(f"District ID: {station[4]}")
        print(f"is_active: '{station[5]}' (Type: {type(station[5])})")
        print(f"Created: {station[6]}")
        print("-" * 70)
    
    # Check for NULL IDs
    print("\n" + "="*70)
    print("Checking for NULL IDs:\n")
    
    cursor.execute("SELECT COUNT(*) FROM women_police_stations WHERE id IS NULL")
    null_count = cursor.fetchone()[0]
    print(f"Records with NULL id: {null_count}")
    
    if null_count > 0:
        cursor.execute("""
            SELECT station_name, incharge_name, district_id, is_active
            FROM women_police_stations
            WHERE id IS NULL
        """)
        null_stations = cursor.fetchall()
        print("\nNULL ID Records:")
        for station in null_stations:
            print(f"  Station: {station[0]}, Incharge: {station[1]}, District: {station[2]}, Active: {station[3]}")
    
    conn.close()

if __name__ == '__main__':
    check_women_ps()
