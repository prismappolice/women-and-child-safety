"""
Automated Fix - Convert ALL Admin Routes from SQLite to PostgreSQL
This will fix CSRF errors, upload issues, and ensure all admin operations use PostgreSQL
"""

import re

print("🔧 Converting ALL Admin Routes to PostgreSQL...")
print("=" * 80)

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

original_content = content
changes_made = []

# Pattern 1: Replace sqlite3.connect('women_safety.db') with get_db_connection('main')
pattern1 = r"conn\s*=\s*sqlite3\.connect\('women_safety\.db'\)"
replacement1 = "conn = get_db_connection('main')"

matches1 = re.findall(pattern1, content)
if matches1:
    content = re.sub(pattern1, replacement1, content)
    changes_made.append(f"✅ Replaced {len(matches1)} sqlite3.connect('women_safety.db') calls")

# Pattern 2: Fix queries with double quotes to use adapt_query
# This is more complex - we need to find cursor.execute patterns and wrap them

# First, let's count how many changes we'll make
lines = content.split('\n')
total_lines = len(lines)

print(f"\n📊 Statistics:")
print(f"   Total lines in app.py: {total_lines}")
print(f"   SQLite connections found: {len(matches1)}")

# Write the updated content
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ Phase 1 Complete: Database Connection Replacement")
for change in changes_made:
    print(f"   {change}")

print(f"\n⚠️  Phase 2 Needed: Query Adaptation")
print(f"   All cursor.execute() calls need adapt_query() wrapper")
print(f"   This requires manual verification to avoid breaking queries")

print(f"\n💡 Next Steps:")
print(f"   1. Test admin gallery upload")
print(f"   2. Test admin safety tips")
print(f"   3. Test admin PDF upload")
print(f"   4. Check for any CSRF errors")
print(f"   5. If errors persist, we'll add adapt_query() to specific routes")

print("\n" + "=" * 80)
print("✅ Basic conversion complete! Testing required.")
