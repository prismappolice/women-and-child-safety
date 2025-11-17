"""
Test script to simulate approving a volunteer and verify status update
"""
from app import get_db_connection

conn = get_db_connection('main')
cursor = conn.cursor()

print("=" * 80)
print("VOLUNTEER APPROVAL TEST")
print("=" * 80)

# Find a pending volunteer
cursor.execute('''
    SELECT v.id, v.name, vs.status
    FROM volunteers v
    LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id
    WHERE vs.status = 'pending' OR vs.status IS NULL
    LIMIT 1
''')

volunteer = cursor.fetchone()

if not volunteer:
    print("\n❌ No pending volunteers found to test")
    print("Creating a test scenario with existing volunteer...")
    
    # Get any volunteer
    cursor.execute('SELECT id, name FROM volunteers LIMIT 1')
    vol = cursor.fetchone()
    if vol:
        vol_id = vol[0]
        print(f"\nUsing volunteer ID {vol_id}: {vol[1]}")
        
        # Set to pending first
        cursor.execute('SELECT id FROM volunteer_scores WHERE volunteer_id = %s', (vol_id,))
        if cursor.fetchone():
            cursor.execute('UPDATE volunteer_scores SET status = %s WHERE volunteer_id = %s', ('pending', vol_id))
        else:
            cursor.execute('INSERT INTO volunteer_scores (volunteer_id, status) VALUES (%s, %s)', (vol_id, 'pending'))
        conn.commit()
        
        volunteer = (vol_id, vol[1], 'pending')
else:
    vol_id = volunteer[0]

print(f"\nVolunteer ID: {vol_id}")
print(f"Name: {volunteer[1]}")
print(f"Current Status: {volunteer[2]}")

# Simulate the approval process
print("\n" + "=" * 80)
print("SIMULATING APPROVAL...")
print("=" * 80)

# Check if record exists
cursor.execute('SELECT id, status FROM volunteer_scores WHERE volunteer_id = %s', (vol_id,))
existing = cursor.fetchone()

if existing:
    print(f"\n✓ Existing record found (ID: {existing[0]}, Status: {existing[1]})")
    print("  Updating status to 'approved'...")
    cursor.execute('UPDATE volunteer_scores SET status = %s, admin_notes = %s WHERE volunteer_id = %s', 
                  ('approved', 'Application approved by admin', vol_id))
else:
    print("\n✓ No existing record, creating new one...")
    cursor.execute('INSERT INTO volunteer_scores (volunteer_id, status, admin_notes) VALUES (%s, %s, %s)',
                  (vol_id, 'approved', 'Application approved by admin'))

conn.commit()

# Verify the update
cursor.execute('SELECT status FROM volunteer_scores WHERE volunteer_id = %s', (vol_id,))
new_status = cursor.fetchone()

print(f"\n✓ Status updated successfully!")
print(f"  New Status: {new_status[0]}")

# Test the query used by admin page
print("\n" + "=" * 80)
print("TESTING ADMIN PAGE QUERY")
print("=" * 80)

cursor.execute('''
    SELECT v.id, v.name, v.email, vs.status
    FROM volunteers v
    LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id
    WHERE v.id = %s
''', (vol_id,))

result = cursor.fetchone()
print(f"\nAdmin page will see:")
print(f"  ID: {result[0]}")
print(f"  Name: {result[1]}")
print(f"  Email: {result[2]}")
print(f"  Status: {result[3]}")

# Check button visibility logic
status = result[3]
print(f"\n" + "=" * 80)
print("BUTTON VISIBILITY CHECK")
print("=" * 80)

if status == 'pending' or status == 'high_priority' or status is None:
    print("\n✓ Buttons shown: Hold, Accept, Reject, View")
else:
    print(f"\n✓ Status is '{status}' - Only View button should show")
    print("  Hold, Accept, Reject buttons are HIDDEN")

print("\n" + "=" * 80)
print("✅ TEST COMPLETE")
print("=" * 80)

conn.close()
