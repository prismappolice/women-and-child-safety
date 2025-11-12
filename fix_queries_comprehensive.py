"""
Fix ALL remaining queries with ? placeholders - comprehensive version
"""
import re

def fix_all_queries_comprehensive():
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find cursor.execute with ? placeholder
    # This regex finds: cursor.execute('...?...' or "...?...", (...))
    pattern = r"cursor\.execute\((['\"])([^'\"]+\?[^'\"]+)\1,\s*(\([^)]+\))\)"
    
    def replace_func(match):
        quote = match.group(1)
        query = match.group(2)
        params = match.group(3)
        
        return f"query = adapt_query({quote}{query}{quote})\n        cursor.execute(query, {params})"
    
    original_content = content
    content = re.sub(pattern, replace_func, content)
    
    changes = content.count('adapt_query(') - original_content.count('adapt_query(')
    
    # Write back
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    return changes

if __name__ == '__main__':
    print("🔧 Comprehensive fix for ALL ? placeholder queries...")
    print("=" * 80)
    changes = fix_all_queries_comprehensive()
    print(f"✅ Added {changes} adapt_query() calls!")
    print("=" * 80)
    print("✅ All queries should now use adapt_query()!")
