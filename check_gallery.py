import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

try:
    cursor.execute('SELECT * FROM gallery_items')
    items = cursor.fetchall()
    print(f'Gallery items count: {len(items)}')
    
    if items:
        cursor.execute('PRAGMA table_info(gallery_items)')
        columns = cursor.fetchall()
        print('Columns:', [col[1] for col in columns])
        
        for item in items:
            print(item)
    else:
        print('No gallery items found')
        
    # Check table structure
    cursor.execute('PRAGMA table_info(gallery_items)')
    columns = cursor.fetchall()
    print('\nTable structure:')
    for col in columns:
        print(f'{col[1]} ({col[2]})')
        
except Exception as e:
    print(f'Error: {e}')
finally:
    conn.close()
