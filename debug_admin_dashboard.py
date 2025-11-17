#!/usr/bin/env python3

from db_config import get_db_connection, adapt_query
import time

def debug_admin_dashboard_issue():
    """Deep debug of admin dashboard vs user status discrepancy"""
    
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    print("=== DEBUGGING ADMIN DASHBOARD DATA SOURCE ===")
    print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 1. Check if multiple tables exist
    print("\n1. CHECKING ALL TABLES:")
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_name LIKE '%volunteer%' 
        ORDER BY table_name
    """)
    tables = cursor.fetchall()
    for table in tables:
        print(f"   - {table[0]}")
    
    # 2. Check for any old volunteer_status table (from SQLite migration)
    try:
        cursor.execute("SELECT COUNT(*) FROM volunteer_status")
        old_table_count = cursor.fetchone()[0]
        print(f"\n2. OLD volunteer_status table exists with {old_table_count} records")
        
        cursor.execute("SELECT volunteer_id, status FROM volunteer_status ORDER BY volunteer_id")
        old_data = cursor.fetchall()
        print("   Old table data:")
        for row in old_data:
            print(f"   - volunteer_id: {row[0]}, status: {row[1]}")
            
    except Exception as e:
        print(f"\n2. OLD volunteer_status table: Does not exist ({e})")
    
    # 3. Exact admin dashboard simulation
    print("\n3. SIMULATING ADMIN DASHBOARD REQUEST:")
    
    # This is the EXACT query used in admin_volunteers() route
    admin_query = adapt_query('''
        SELECT v.id, v.name, v.email, v.phone, v.age, v.address, v.education, v.occupation, 
               v.motivation, v.skills, v.created_at,
               vs.age_score, vs.education_score, vs.motivation_score, vs.skills_score, 
               vs.total_score, vs.status, vs.admin_notes
        FROM volunteers v
        LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id
        ORDER BY v.created_at DESC
    ''')
    
    print("   Query being executed:")
    print(f"   {admin_query}")
    
    cursor.execute(admin_query)
    volunteers = cursor.fetchall()
    
    print("\n   Results (exactly as template will receive):")
    for i, vol in enumerate(volunteers):
        reg_id = f"VOL-2025-{vol[0]:04d}"  # Generate reg ID for display
        status_at_index_16 = vol[16]  # This is volunteer[16] in template
        print(f"   Row {i}: {reg_id} - {vol[1]} - Status[16]: '{status_at_index_16}'")
        
        # Check what template logic will show
        if status_at_index_16:
            if status_at_index_16 in ['approved', 'accepted']:
                badge_text = 'Accepted'
                show_buttons = False
            elif status_at_index_16 == 'rejected':
                badge_text = 'Rejected'  
                show_buttons = False
            elif status_at_index_16 == 'high_priority':
                badge_text = 'On Hold'
                show_buttons = True
            else:
                badge_text = status_at_index_16.title()
                show_buttons = True
        else:
            badge_text = 'Pending'
            show_buttons = True
            
        print(f"        Template will show: '{badge_text}', Buttons: {'YES' if show_buttons else 'NO'}")
    
    # 4. Check for any database connection issues
    print(f"\n4. DATABASE CONNECTION INFO:")
    print(f"   Connection type: {type(conn)}")
    cursor.execute("SELECT version()")
    db_version = cursor.fetchone()[0]
    print(f"   Database version: {db_version}")
    
    # 5. Check app.py route name conflicts
    print("\n5. CHECKING FOR ROUTE CONFLICTS:")
    print("   Current admin_volunteers() route should be at line ~3064 in app.py")
    print("   Template path: templates/admin_volunteers.html")
    
    conn.close()
    
    print("\n=== DEBUG COMPLETE ===")
    print("If admin dashboard still shows wrong data, the issue is:")
    print("1. Browser cache (despite our cache-busting)")
    print("2. Different route being called")  
    print("3. JavaScript/Template not updating")
    print("4. Old volunteer_status table being used somewhere")

if __name__ == "__main__":
    debug_admin_dashboard_issue()