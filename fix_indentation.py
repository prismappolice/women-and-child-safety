"""
Fix indentation issues caused by multi-line query replacement
"""
import re

with open('app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

fixed_lines = []
i = 0

while i < len(lines):
    line = lines[i]
    
    # Check if this is a query = adapt_query line
    if 'query = adapt_query(' in line and "'''" in line:
        # Get the indentation of this line
        indent = len(line) - len(line.lstrip())
        
        # Add this line
        fixed_lines.append(line)
        i += 1
        
        # Process the multi-line query
        while i < len(lines) and "'''" not in lines[i]:
            fixed_lines.append(lines[i])
            i += 1
        
        # Add the closing '''
        if i < len(lines):
            fixed_lines.append(lines[i])
            i += 1
        
        # Check next line - should be cursor.execute with same indentation
        if i < len(lines) and 'cursor.execute(' in lines[i]:
            next_line = lines[i]
            # Fix indentation to match the query line
            spaces = ' ' * indent
            fixed_line = spaces + next_line.lstrip()
            fixed_lines.append(fixed_line)
            i += 1
        continue
    
    fixed_lines.append(line)
    i += 1

with open('app.py', 'w', encoding='utf-8') as f:
    f.writelines(fixed_lines)

print("✅ Fixed indentation issues!")
