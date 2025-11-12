"""
Simple text replacement for all cursor.execute with ? to add adapt_query
"""

with open('app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

modified_lines = []
i = 0
fixed_count = 0

while i < len(lines):
    line = lines[i]
    
    # Check if line has cursor.execute with ?
    if 'cursor.execute(' in line and '?' in line and 'adapt_query' not in line:
        # Extract the indentation
        indent = len(line) - len(line.lstrip())
        spaces = ' ' * indent
        
        # Find the query part (between quotes)
        import re
        # Match: cursor.execute('...' or "...", (...))
        match = re.search(r"cursor\.execute\((['\"])(.+?)\1,\s*(\(.+?\))\)", line)
        
        if match:
            quote = match.group(1)
            query_text = match.group(2)
            params = match.group(3)
            
            # Add two lines: query = adapt_query(...) and cursor.execute(query, ...)
            modified_lines.append(f"{spaces}query = adapt_query({quote}{query_text}{quote})\n")
            modified_lines.append(f"{spaces}cursor.execute(query, {params})\n")
            fixed_count += 1
        else:
            modified_lines.append(line)
    else:
        modified_lines.append(line)
    
    i += 1

with open('app.py', 'w', encoding='utf-8') as f:
    f.writelines(modified_lines)

print(f"✅ Fixed {fixed_count} queries!")
