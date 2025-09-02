import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check if table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gallery_items'")
result = cursor.fetchone()

if result:
    print("Gallery items table exists")
    cursor.execute("SELECT COUNT(*) FROM gallery_items")
    count = cursor.fetchone()[0]
    print(f"Current items: {count}")
else:
    print("Creating gallery_items table...")
    cursor.execute('''
        CREATE TABLE gallery_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            image_url TEXT,
            video_url TEXT,
            event_date DATE,
            category TEXT NOT NULL,
            is_featured INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    print("Table created successfully")

conn.commit()
conn.close()
print("Done!")
