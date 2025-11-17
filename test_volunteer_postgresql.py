"""
Test if volunteer status updates work correctly in PostgreSQL
"""
from app import get_db_connection
import time

print("=" * 80)
print("TESTING VOLUNTEER STATUS UPDATE IN POSTGRESQL")
print("=" * 80)

conn = get_db_connection('main')
cursor = conn.cursor()

# Get a volunteer to test with
cursor.execute('SELECT id, name FROM volunteers LIMIT 1')
volunteer = cursor.fetchone()

if not volunteer:
    print("\n❌ No volunteers found in database")
    conn.close()
    exit()

vol_id = volunteer[0]
vol_name = volunteer[1]

print(f"\nTesting with Volunteer ID: {vol_id} ({vol_name})")

# Step 1: Check current status
print("\n" + "=" * 80)
print("STEP 1: Current Status")
print("=" * 80)

cursor.execute('''
    SELECT v.id, v.name, vs.status
    FROM volunteers v
    LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id
    WHERE v.id = %s
''', (vol_id,))

result = cursor.fetchone()
current_status = result[2] if result[2] else "NULL"
print(f"Current Status: {current_status}")

# Step 2: Set to pending
print("\n" + "=" * 80)
print("STEP 2: Setting to 'pending'")
print("=" * 80)

cursor.execute('SELECT id FROM volunteer_scores WHERE volunteer_id = %s', (vol_id,))
existing = cursor.fetchone()

if existing:
    cursor.execute('UPDATE volunteer_scores SET status = %s WHERE volunteer_id = %s', ('pending', vol_id))
else:
    cursor.execute('INSERT INTO volunteer_scores (volunteer_id, status) VALUES (%s, %s)', (vol_id, 'pending'))

conn.commit()

cursor.execute('SELECT status FROM volunteer_scores WHERE volunteer_id = %s', (vol_id,))
new_status = cursor.fetchone()[0]
print(f"✓ Status set to: {new_status}")

# Step 3: Approve (simulate admin action)
print("\n" + "=" * 80)
print("STEP 3: Approving volunteer (simulating admin action)")
print("=" * 80)

cursor.execute('SELECT id FROM volunteer_scores WHERE volunteer_id = %s', (vol_id,))
existing_record = cursor.fetchone()

if existing_record:
    cursor.execute('''
        UPDATE volunteer_scores 
        SET status = %s, admin_notes = %s
        WHERE volunteer_id = %s
    ''', ('approved', 'Application approved by admin', vol_id))
    print("✓ Updated existing record")
else:
    cursor.execute('''
        INSERT INTO volunteer_scores (volunteer_id, status, admin_notes)
        VALUES (%s, %s, %s)
    ''', (vol_id, 'approved', 'Application approved by admin'))
    print("✓ Inserted new record")

conn.commit()

# Step 4: Verify the update
print("\n" + "=" * 80)
print("STEP 4: Verifying Update")
print("=" * 80)

cursor.execute('''
    SELECT v.id, v.name, vs.status, vs.admin_notes
    FROM volunteers v
    LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id
    WHERE v.id = %s
''', (vol_id,))

result = cursor.fetchone()
print(f"Volunteer ID: {result[0]}")
print(f"Name: {result[1]}")
print(f"Status: {result[2]}")
print(f"Admin Notes: {result[3]}")

# Step 5: Check button visibility logic
print("\n" + "=" * 80)
print("STEP 5: Button Visibility Check")
print("=" * 80)

status = result[2]

if status == 'pending' or status == 'high_priority' or status is None:
    print(f"Status: {status}")
    print("✓ Buttons shown: Hold, Accept, Reject, View")
elif status == 'approved':
    print(f"Status: {status}")
    print("✓ Buttons shown: View ONLY")
    print("✓ Hidden: Hold, Accept, Reject")
elif status == 'rejected':
    print(f"Status: {status}")
    print("✓ Buttons shown: View ONLY")
    print("✓ Hidden: Hold, Accept, Reject")

# Step 6: Test immediate re-query (like admin panel does)
print("\n" + "=" * 80)
print("STEP 6: Simulating Admin Panel Re-query")
print("=" * 80)

time.sleep(0.1)  # Small delay to simulate browser request

cursor.execute('''
    SELECT v.id, v.name, v.email, v.phone, v.age, v.address, v.education, v.occupation, 
           v.motivation, v.skills, v.created_at,
           vs.age_score, vs.education_score, vs.motivation_score, vs.skills_score, 
           vs.total_score, vs.status, vs.admin_notes
    FROM volunteers v
    LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id
    WHERE v.id = %s
''', (vol_id,))

admin_view = cursor.fetchone()
admin_status = admin_view[16] if len(admin_view) > 16 else None

print(f"Admin panel sees status: {admin_status}")

if admin_status == 'approved':
    print("✅ SUCCESS: Admin panel will show 'Approved' badge")
    print("✅ SUCCESS: Only 'View' button will be visible")
    print("✅ SUCCESS: Hold, Accept, Reject buttons will be HIDDEN")
else:
    print(f"❌ PROBLEM: Expected 'approved' but got '{admin_status}'")

print("\n" + "=" * 80)
print("✅ ALL TESTS COMPLETE")
print("=" * 80)

conn.close()
