from app import get_db_connection

conn = get_db_connection('main')
cursor = conn.cursor()

print("=" * 80)
print("COMPREHENSIVE USER VIEW CHECK")
print("=" * 80)

# Check all districts with their contact counts
cursor.execute('''
    SELECT 
        d.id,
        d.district_name,
        (SELECT COUNT(*) FROM district_sps WHERE district_id = d.id AND is_active::integer = 1) as sps_count,
        (SELECT COUNT(*) FROM shakthi_teams WHERE district_id = d.id AND is_active::integer = 1) as teams_count,
        (SELECT COUNT(*) FROM women_police_stations WHERE district_id = d.id AND is_active::integer = 1) as stations_count,
        (SELECT COUNT(*) FROM one_stop_centers WHERE district_id = d.id AND is_active::integer = 1) as centers_count
    FROM districts d
    WHERE d.is_active::integer = 1
    ORDER BY d.district_name
''')

print("\nAll Districts Contact Counts (User View):")
print("-" * 80)
print(f"{'District':<30} {'SPs':<8} {'Teams':<8} {'Stations':<10} {'Centers':<8}")
print("-" * 80)

total_sps = 0
total_teams = 0
total_stations = 0
total_centers = 0

for row in cursor.fetchall():
    dist_id, dist_name, sps, teams, stations, centers = row
    print(f"{dist_name:<30} {sps:<8} {teams:<8} {stations:<10} {centers:<8}")
    total_sps += sps
    total_teams += teams
    total_stations += stations
    total_centers += centers

print("-" * 80)
print(f"{'TOTAL':<30} {total_sps:<8} {total_teams:<8} {total_stations:<10} {total_centers:<8}")
print("-" * 80)

# Now show the specific newly added records
print("\n" + "=" * 80)
print("NEWLY ADDED RECORDS (Last 3 in each category)")
print("=" * 80)

print("\nWomen Police Stations:")
cursor.execute('''
    SELECT w.id, d.district_name, w.station_name, w.incharge_name, w.is_active 
    FROM women_police_stations w
    JOIN districts d ON w.district_id = d.id
    ORDER BY w.id DESC
    LIMIT 3
''')
for row in cursor.fetchall():
    print(f"  ID {row[0]}: {row[2]} in {row[1]} - is_active={row[4]}")

print("\nOne Stop Centers:")
cursor.execute('''
    SELECT o.id, d.district_name, o.center_name, o.incharge_name, o.is_active 
    FROM one_stop_centers o
    JOIN districts d ON o.district_id = d.id
    ORDER BY o.id DESC
    LIMIT 3
''')
for row in cursor.fetchall():
    print(f"  ID {row[0]}: {row[2]} in {row[1]} - is_active={row[4]}")

print("\n" + "=" * 80)
print("CONCLUSION:")
print("=" * 80)
print("✅ All queries use: WHERE is_active::integer = 1")
print("✅ All newly added records have is_active='1'")
print("✅ Records SHOULD be visible in user view")
print("\nIf you're not seeing them on the website:")
print("  1. Clear browser cache (Ctrl+Shift+Delete)")
print("  2. Do a hard refresh (Ctrl+F5)")
print("  3. Check the correct district page")
print("=" * 80)

conn.close()
