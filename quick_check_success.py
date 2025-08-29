import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check success stories with images
cursor.execute('SELECT id, title, image_url, is_active FROM success_stories ORDER BY id')
stories = cursor.fetchall()

print(f"Found {len(stories)} success stories:")
for story in stories:
    print(f"ID: {story[0]}, Title: {story[1][:30]}..., Image: {story[2]}, Active: {story[3]}")

conn.close()
