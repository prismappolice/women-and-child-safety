from db_config import get_db_connection

def check_shakthi_teams():
    """Check shakthi teams data"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    # Check all shakthi teams
    cursor.execute("""
        SELECT id, team_name, leader_name, contact_number, district_id, is_active, created_at
        FROM shakthi_teams
        ORDER BY created_at DESC
    """)
    teams = cursor.fetchall()
    
    print(f"Total Shakthi Teams: {len(teams)}\n")
    
    for team in teams:
        print(f"ID: {team[0]}")
        print(f"Team Name: {team[1]}")
        print(f"Leader: {team[2]}")
        print(f"Contact: {team[3]}")
        print(f"District ID: {team[4]}")
        print(f"Is Active: {team[5]} (Type: {type(team[5])})")
        print(f"Created: {team[6]}")
        print("-" * 70)
    
    # Check districts table for ASR
    print("\n" + "="*70)
    print("Checking Districts table for ASR:\n")
    cursor.execute("SELECT id, district_name FROM districts WHERE district_name ILIKE '%alluri%' OR district_name ILIKE '%asr%'")
    districts = cursor.fetchall()
    
    for d in districts:
        print(f"District ID: {d[0]}, Name: {d[1]}")
    
    conn.close()

if __name__ == '__main__':
    check_shakthi_teams()
