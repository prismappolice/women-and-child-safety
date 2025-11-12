"""
Fix ALL remaining queries with ? placeholders to use adapt_query()
"""
import re

def fix_all_queries():
    with open('app.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    changes_made = 0
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Pattern: cursor.execute('...?...', (...))
        # Match single or double quoted strings with ? placeholder
        pattern = r"(\s*)cursor\.execute\((['\"])(.+?\?.+?)\2,\s*(\([^)]+\))\)"
        match = re.search(pattern, line)
        
        if match:
            indent = match.group(1)
            quote = match.group(2)
            query = match.group(3)
            params = match.group(4)
            
            # Replace with adapt_query version
            new_lines = [
                f"{indent}query = adapt_query({quote}{query}{quote})\n",
                f"{indent}cursor.execute(query, {params})\n"
            ]
            
            lines[i:i+1] = new_lines
            changes_made += 1
            i += 2  # Skip the lines we just added
            continue
        
        i += 1
    
    # Write back
    with open('app.py', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    return changes_made

if __name__ == '__main__':
    print("🔧 Fixing ALL remaining ? placeholder queries...")
    print("=" * 80)
    changes = fix_all_queries()
    print(f"✅ Fixed {changes} queries!")
    print("=" * 80)
    print("✅ All queries now use adapt_query()!")
