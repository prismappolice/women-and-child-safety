from db_config import get_db_connection

def check_recent_teams():
    """Check recently added teams"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    # Get all teams with NULL or problematic is_active
    cursor.execute("""
        SELECT id, team_name, leader_name, district_id, is_active, created_at
        FROM shakthi_teams
        WHERE district_id = 1
        ORDER BY id DESC
    """)
    teams = cursor.fetchall()
    
    print(f"All Shakthi Teams for ASR (District ID = 1):\n")
    
    for team in teams:
        print(f"ID: {team[0]}")
        print(f"Team: {team[1]}")
        print(f"Leader: {team[2]}")
        print(f"District ID: {team[3]}")
        print(f"is_active: '{team[4]}' (Type: {type(team[4])}, Value: {repr(team[4])})")
        print(f"Created: {team[5]}")
        print("-" * 70)
    
    # Check for NULL or invalid is_active
    print("\n" + "="*70)
    print("Checking for problematic is_active values:\n")
    
    cursor.execute("""
        SELECT id, team_name, is_active
        FROM shakthi_teams
        WHERE district_id = 1 AND (is_active IS NULL OR is_active NOT IN ('0', '1'))
    """)
    problem_teams = cursor.fetchall()
    
    if problem_teams:
        print(f"Found {len(problem_teams)} teams with problematic is_active:")
        for team in problem_teams:
            print(f"  ID {team[0]}: {team[1]} - is_active = {repr(team[2])}")
    else:
        print("No problematic is_active values found")
    
    conn.close()

if __name__ == '__main__':
    check_recent_teams()
