import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check videos and fix them
cursor.execute("SELECT id, title, video_url FROM gallery_items WHERE category = 'Videos'")
videos = cursor.fetchall()

print("Current Videos:")
for v in videos:
    print(f"ID {v[0]}: {v[1]} - {v[2]}")

# Fix videos with proper YouTube URLs
cursor.execute("UPDATE gallery_items SET video_url = 'https://youtu.be/T7aNhNdaRUk' WHERE id = 68")
cursor.execute("UPDATE gallery_items SET video_url = 'https://youtu.be/E9RCpXMiLTA' WHERE id = 69") 

# Add a Women's Day video if it doesn't exist
cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE title LIKE '%women%day%'")
count = cursor.fetchone()[0]

if count == 0:
    cursor.execute('''
        INSERT INTO gallery_items (title, description, image_url, video_url, category, is_featured, is_active)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', ("Women's Day Celebration", "Special Women's Day celebration video", 
          "/static/images/slide5.jpg", "https://youtu.be/dQw4w9WgXcQ", "Videos", 1, 1))
    print("Added Women's Day video")

conn.commit()

# Verify updates
cursor.execute("SELECT id, title, video_url FROM gallery_items WHERE category = 'Videos'")
updated_videos = cursor.fetchall()

print("\nUpdated Videos:")
for v in updated_videos:
    print(f"ID {v[0]}: {v[1]} - {v[2]}")

conn.close()
print("Database updated successfully!")
