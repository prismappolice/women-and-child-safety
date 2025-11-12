"""
Verification script to check all INSERT statements in app.py
to ensure they properly set is_active or use sequences correctly
"""

import re

def check_insert_statements():
    with open('e:/final ap women safety/app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all INSERT statements
    insert_pattern = r"INSERT INTO (\w+)\s*\([^)]+\)\s*VALUES\s*\([^)]+\)"
    matches = re.finditer(insert_pattern, content, re.IGNORECASE)
    
    issues = []
    good_inserts = []
    
    tables_with_is_active = [
        'district_sps', 'shakthi_teams', 'women_police_stations', 'one_stop_centers',
        'gallery_items', 'pdf_resources', 'safety_tips', 'initiatives', 
        'officers', 'success_stories', 'contact_info', 'events', 'home_content'
    ]
    
    for match in matches:
        table_name = match.group(1).lower()
        full_query = match.group(0)
        
        # Check if table should have is_active
        if table_name in tables_with_is_active:
            # Check if is_active is included in INSERT
            if 'is_active' not in full_query.lower():
                issues.append({
                    'table': table_name,
                    'query': full_query[:100] + '...',
                    'issue': 'Missing is_active field'
                })
            else:
                good_inserts.append(table_name)
    
    print("="*80)
    print("INSERT STATEMENT VERIFICATION")
    print("="*80)
    print()
    
    if issues:
        print(f"⚠ FOUND {len(issues)} POTENTIAL ISSUES:\n")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. Table: {issue['table']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Query: {issue['query']}")
            print()
    else:
        print("✅ NO ISSUES FOUND!")
        print()
    
    print(f"✓ Good INSERT statements: {len(good_inserts)}")
    print(f"  Tables: {set(good_inserts)}")
    print()
    
    # Also check if we already fixed the main ones
    print("="*80)
    print("CHECKING SPECIFICALLY FIXED ADD ROUTES:")
    print("="*80)
    
    routes_to_check = [
        ('admin_add_district_sp', 'district_sps'),
        ('admin_add_shakthi_team', 'shakthi_teams'),
        ('admin_add_women_station', 'women_police_stations'),
        ('admin_add_one_stop_center', 'one_stop_centers'),
    ]
    
    for route_name, table in routes_to_check:
        if route_name in content:
            # Find the INSERT for this route
            route_start = content.find(f'def {route_name}')
            route_section = content[route_start:route_start+2000]
            
            if f"INSERT INTO {table}" in route_section and "is_active" in route_section:
                print(f"✓ {route_name}: Properly includes is_active")
            else:
                print(f"⚠ {route_name}: May not include is_active")
        else:
            print(f"? {route_name}: Route not found")
    
    print("\n" + "="*80)

if __name__ == '__main__':
    check_insert_statements()
