import re

# Read app.py
with open('e:/final ap women safety/app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all sqlite3.OperationalError with Exception and add rollback
replacements = [
    (r'except sqlite3\.OperationalError( as \w+)?:', r'except Exception\1:\n        conn.rollback()'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

# Write back
with open('e:/final ap women safety/app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed all sqlite3.OperationalError references!")
print("Added conn.rollback() to handle failed transactions properly")
