import re

# Read app.py
with open('e:/final ap women safety/app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all instances of "is_active = 1" with "is_active::integer = 1"
# for district-related tables
district_tables = [
    'district_sps',
    'shakthi_teams', 
    'women_police_stations',
    'one_stop_centers'
]

for table in district_tables:
    # Pattern: table_name WHERE ... AND is_active = 1
    pattern = f'FROM {table} WHERE (.*?) AND is_active = 1'
    replacement = f'FROM {table} WHERE \\1 AND is_active::integer = 1'
    content = re.sub(pattern, replacement, content)
    
    # Pattern: table_name WHERE ... AND is_active = 0
    pattern = f'FROM {table} WHERE (.*?) AND is_active = 0'
    replacement = f'FROM {table} WHERE \\1 AND is_active::integer = 0'
    content = re.sub(pattern, replacement, content)

# Write back
with open('e:/final ap women safety/app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed all is_active comparisons in district tables!")
print("Added ::integer type cast to avoid PostgreSQL type mismatch errors")
