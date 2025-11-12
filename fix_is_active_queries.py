"""
Fix all is_active comparison queries for PostgreSQL type compatibility
Replaces: WHERE is_active = 1
With: WHERE is_active::integer = 1
"""

import re

def fix_is_active_queries():
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match "WHERE is_active = 1" (and similar patterns)
    # This handles various spacing and line breaks
    patterns = [
        (r'WHERE is_active = 1', r'WHERE is_active::integer = 1'),
        (r'WHERE is_active = 0', r'WHERE is_active::integer = 0'),
        (r'is_active=1', r'is_active::integer=1'),
        (r'is_active=0', r'is_active::integer=0'),
    ]
    
    changes_made = 0
    for old_pattern, new_pattern in patterns:
        count = content.count(old_pattern)
        if count > 0:
            content = content.replace(old_pattern, new_pattern)
            changes_made += count
            print(f"✅ Fixed {count} occurrences: {old_pattern} → {new_pattern}")
    
    # Write back
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Total changes: {changes_made}")
    return changes_made

if __name__ == '__main__':
    print("🔧 Fixing is_active queries for PostgreSQL type compatibility...")
    print("=" * 80)
    changes = fix_is_active_queries()
    print("=" * 80)
    print("✅ All is_active queries fixed!")
