import sqlite3

print("FIXING EXISTING VIDEO ENTRIES")
print("="*40)

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Fix the existing broken video entries
cursor.execute('UPDATE gallery_items SET video_url = "https://www.youtube.com/watch?v=T7aNhNdaRUk", image_url = "/static/images/slide3.jpg" WHERE id = 68')
cursor.execute('UPDATE gallery_items SET video_url = "https://www.youtube.com/watch?v=E9RCpXMiLTA", image_url = "/static/images/slide4.jpg" WHERE id = 69')

conn.commit()

print("✅ Fixed existing video entries")

# Verify the fix
cursor.execute('SELECT id, title, image_url, video_url FROM gallery_items WHERE category = "Videos"')
videos = cursor.fetchall()

for video in videos:
    print(f"\nVideo ID: {video[0]} - {video[1]}")
    print(f"  Image: {video[2]}")
    print(f"  Video: {video[3]}")
    print(f"  Status: {'✅ Working' if video[3] and video[3].startswith('http') else '❌ Issue'}")

conn.close()
print("\n🎉 Database fixed! Now let's test the website.")
