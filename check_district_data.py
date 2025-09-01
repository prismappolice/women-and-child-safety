import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check district tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%district%'")
tables = cursor.fetchall()
print('District tables:', [t[0] for t in tables])

# Check data in main districts table
try:
    cursor.execute('SELECT * FROM districts LIMIT 5')
    districts = cursor.fetchall()
    print(f'\nDistricts table has {len(districts)} records:')
    for district in districts:
        print(district)
except Exception as e:
    print(f'Error accessing districts table: {e}')

# Check district_sps table
try:
    cursor.execute('SELECT * FROM district_sps LIMIT 5')
    sps = cursor.fetchall()
    print(f'\nDistrict SPs table has {len(sps)} records:')
    for sp in sps:
        print(sp)
except Exception as e:
    print(f'Error accessing district_sps table: {e}')

# Check shakthi_teams table
try:
    cursor.execute('SELECT * FROM shakthi_teams LIMIT 5')
    teams = cursor.fetchall()
    print(f'\nShakthi teams table has {len(teams)} records:')
    for team in teams:
        print(team)
except Exception as e:
    print(f'Error accessing shakthi_teams table: {e}')

conn.close()
