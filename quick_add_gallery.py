import sqlite3

# Simple script to add gallery items directly
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check if table exists, create if not
cursor.execute('''CREATE TABLE IF NOT EXISTS gallery_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    image_url TEXT,
    video_url TEXT,
    event_date DATE,
    category TEXT NOT NULL,
    is_featured INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1
)''')

# Sample data
items = [
    ('Basic Self Defence Training', 'Learn essential self-defence techniques for personal safety', '/static/images/slide1.jpg', '', '2024-12-15', 'Self Defence Programme', 1, 1),
    ('Advanced Martial Arts', 'Advanced defensive moves and techniques', '/static/images/slide2.jpg', '', '2024-12-12', 'Self Defence Programme', 0, 1),
    ('Safety Training Video', 'Comprehensive safety awareness video', '/static/images/slide3.jpg', '/static/videos/safety.mp4', '2024-12-10', 'Training Videos', 1, 1),
    ('Community Outreach', 'Village-level safety awareness program', '/static/images/slide4.jpg', '', '2024-12-08', 'Community Programmes', 0, 1),
    ('Safety Week Launch', 'Official launch of safety awareness week', '/static/images/slide5.jpg', '', '2024-12-05', 'News & Events', 1, 1)
]

for item in items:
    cursor.execute('''INSERT OR IGNORE INTO gallery_items 
                     (title, description, image_url, video_url, event_date, category, is_featured, is_active) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', item)

conn.commit()
cursor.execute("SELECT COUNT(*) FROM gallery_items")
count = cursor.fetchone()[0]
print(f"Total gallery items: {count}")
conn.close()
print("Done!")
