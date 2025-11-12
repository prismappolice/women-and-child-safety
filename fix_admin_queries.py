"""
Fix High-Priority Admin Routes - Add adapt_query to critical operations
Focus on: Safety Tips, PDF Resources, Volunteers, Officers, Success Stories
"""

import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)

# Pattern to find cursor.execute without adapt_query in admin routes
# This is a simple pattern - looks for cursor.execute('...')

patterns_to_fix = [
    # Pattern: cursor.execute('SELECT
    (r"cursor\.execute\('(SELECT[^']+)'\)", r"query = adapt_query('\1')\n        cursor.execute(query)"),
    # Pattern: cursor.execute('INSERT
    (r"cursor\.execute\('(INSERT[^']+)'\s*,\s*\(([^)]+)\)\)", r"query = adapt_query('\1')\n        cursor.execute(query, (\2))"),
    # Pattern: cursor.execute('UPDATE
    (r"cursor\.execute\('(UPDATE[^']+)'\s*,\s*\(([^)]+)\)\)", r"query = adapt_query('\1')\n        cursor.execute(query, (\2))"),
    # Pattern: cursor.execute('DELETE
    (r"cursor\.execute\('(DELETE[^']+)'\s*,\s*\(([^)]+)\)\)", r"query = adapt_query('\1')\n        cursor.execute(query, (\2))"),
]

print("🔧 Adding adapt_query() to admin route queries...")
print("=" * 80)

changes = 0
for pattern, replacement in patterns_to_fix:
    matches = re.findall(pattern, content)
    if matches:
        content = re.sub(pattern, replacement, content)
        changes += len(matches)
        print(f"✅ Fixed {len(matches)} {pattern.split('(')[0]} queries")

# Also fix triple-quoted queries
pattern_triple = r"cursor\.execute\('''(.*?)'''\s*,\s*\(([^)]+)\)\)"
matches_triple = re.findall(pattern_triple, content, re.DOTALL)
if matches_triple:
    print(f"\n⚠️  Found {len(matches_triple)} triple-quoted queries")
    print(f"   These require manual review for multi-line SQL")

# Write back
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

new_len = len(content)

print(f"\n📊 Statistics:")
print(f"   Original file size: {original_len} characters")
print(f"   New file size: {new_len} characters")
print(f"   Changes made: {changes}")

print("\n" + "=" * 80)
print("✅ High-priority routes fixed!")
print("\n💡 Note: Some complex queries may need manual review")
print("   Test each admin function to ensure it works correctly")
