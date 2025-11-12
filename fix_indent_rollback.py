import re

# Read app.py
with open('e:/final ap women safety/app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the specific indentation issue: conn.rollback() after except Exception:
# Pattern: except Exception:\nconn.rollback() (wrong indent)
# Replace with: except Exception:\n            conn.rollback() (correct indent)

content = content.replace(
    'except Exception:\n        conn.rollback()',
    'except Exception:\n            conn.rollback()'
)

# Also handle case without leading spaces on conn.rollback line
content = content.replace(
    'except Exception:\nconn.rollback()',
    'except Exception:\n            conn.rollback()'
)

# Write back
with open('e:/final ap women safety/app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed indentation for conn.rollback() statements!")
