from db_config import get_db_connection

def fix_null_shakthi_team():
    """Fix NULL ID shakthi team"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    # Find NULL ID record
    cursor.execute("SELECT team_name, leader_name FROM shakthi_teams WHERE id IS NULL")
    null_team = cursor.fetchone()
    
    if null_team:
        print(f"Found NULL ID team: {null_team[0]}")
        
        # Get max ID
        cursor.execute("SELECT MAX(id) FROM shakthi_teams WHERE id IS NOT NULL")
        result = cursor.fetchone()
        max_id = result[0] if result and result[0] else 0
        next_id = max_id + 1
        
        print(f"Max ID: {max_id}, will assign ID: {next_id}")
        
        # Update NULL ID record
        cursor.execute("""
            UPDATE shakthi_teams 
            SET id = %s, is_active = '1'
            WHERE id IS NULL
        """, (next_id,))
        
        conn.commit()
        
        # Verify
        cursor.execute("SELECT id, team_name, is_active FROM shakthi_teams WHERE id = %s", (next_id,))
        fixed = cursor.fetchone()
        print(f"\nFixed!")
        print(f"  ID: {fixed[0]}")
        print(f"  Team: {fixed[1]}")
        print(f"  is_active: {fixed[2]}")
        
        # Check remaining NULL IDs
        cursor.execute("SELECT COUNT(*) FROM shakthi_teams WHERE id IS NULL")
        remaining = cursor.fetchone()[0]
        print(f"\nRemaining NULL IDs: {remaining}")
        
    else:
        print("No NULL IDs found!")
    
    conn.close()

if __name__ == '__main__':
    fix_null_shakthi_team()
