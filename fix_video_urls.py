import sqlite3

print("Fixing Video URL for Testing")
print("="*40)

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Update video ID 69 to have a valid YouTube URL for testing
cursor.execute('''
UPDATE gallery_items 
SET video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' 
WHERE id = 69
''')

# Add a video URL to ID 68 as well
cursor.execute('''
UPDATE gallery_items 
SET video_url = 'https://www.youtube.com/watch?v=3JZ_D3ELwOQ' 
WHERE id = 68
''')

conn.commit()

# Verify the changes
cursor.execute('SELECT id, title, video_url FROM gallery_items WHERE category = "Videos"')
rows = cursor.fetchall()

print("Updated video entries:")
for row in rows:
    print(f"ID: {row[0]}, Title: {row[1]}, Video URL: {row[2]}")

conn.close()
print("\nVideo URLs fixed! Now videos should play on website.")
