import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check for videos
cursor.execute('SELECT * FROM gallery_items WHERE category = "Videos"')
video_rows = cursor.fetchall()

print(f"Found {len(video_rows)} video entries in database:")
for row in video_rows:
    print(f"ID: {row[0]}, Title: {row[1]}, Category: {row[5]}, Video URL: {row[4]}")

conn.close()
