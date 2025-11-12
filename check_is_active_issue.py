from app import get_db_connection

conn = get_db_connection('main')
cursor = conn.cursor()

print("Recent Women Police Stations:")
cursor.execute('SELECT id, station_name, is_active FROM women_police_stations ORDER BY id DESC LIMIT 3')
for row in cursor.fetchall():
    print(f"  ID {row[0]}: {row[1]} - is_active={repr(row[2])} (type: {type(row[2])})")

print("\nRecent One Stop Centers:")
cursor.execute('SELECT id, center_name, is_active FROM one_stop_centers ORDER BY id DESC LIMIT 3')
for row in cursor.fetchall():
    print(f"  ID {row[0]}: {row[1]} - is_active={repr(row[2])} (type: {type(row[2])})")

print("\nChecking if ::integer cast works:")
cursor.execute("SELECT id, station_name FROM women_police_stations WHERE is_active::integer = 1 ORDER BY id DESC LIMIT 3")
print(f"Women PS with is_active::integer = 1: {len(cursor.fetchall())} records")

cursor.execute("SELECT id, center_name FROM one_stop_centers WHERE is_active::integer = 1 ORDER BY id DESC LIMIT 3")
print(f"One Stop Centers with is_active::integer = 1: {len(cursor.fetchall())} records")

conn.close()
