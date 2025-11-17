from app import get_db_connection

conn = get_db_connection('main')
cursor = conn.cursor()

print("=" * 80)
print("VOLUNTEER STATUS CHECK")
print("=" * 80)

# Check all volunteers and their statuses
cursor.execute('''
    SELECT v.id, v.name, v.email, vs.status
    FROM volunteers v
    LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id
    ORDER BY v.id
''')

volunteers = cursor.fetchall()

print(f"\nTotal Volunteers: {len(volunteers)}\n")

for vol in volunteers:
    vol_id, name, email, status = vol
    status_display = status if status else "NULL (No status)"
    print(f"ID {vol_id}: {name}")
    print(f"  Email: {email}")
    print(f"  Status: {status_display}")
    print()

# Check volunteer_scores table structure
print("=" * 80)
print("VOLUNTEER_SCORES TABLE STRUCTURE")
print("=" * 80)
cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name='volunteer_scores'")
columns = cursor.fetchall()
print("Columns:", [c[0] for c in columns])

conn.close()
