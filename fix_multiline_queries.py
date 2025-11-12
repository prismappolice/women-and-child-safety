"""
Fix ALL multi-line queries with ? placeholders
"""
import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match multi-line cursor.execute with ''' or """
# Pattern: cursor.execute(''' ... ? ... ''', (...))
pattern = r"cursor\.execute\(('''|\"\"\")([^'\"]+?)\1,\s*(\([^)]+\))\)"

def replace_multiline(match):
    quote = match.group(1)
    query = match.group(2)
    params = match.group(3)
    
    # Check if query contains ? placeholder
    if '?' in query:
        return f"query = adapt_query({quote}{query}{quote})\n        cursor.execute(query, {params})"
    else:
        # No placeholder, keep as is
        return match.group(0)

original_count = content.count('cursor.execute(')
content = re.sub(pattern, replace_multiline, content, flags=re.DOTALL)
new_count = content.count('adapt_query(')

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Processed multi-line queries!")
print(f"   Total adapt_query() calls: {new_count}")
