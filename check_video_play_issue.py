import sqlite3

print("Video Play Issue Check")
print("="*50)

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check video entries
cursor.execute('SELECT id, title, image_url, video_url, category FROM gallery_items WHERE category = "Videos"')
rows = cursor.fetchall()

print(f"Found {len(rows)} video entries:")
print()

for row in rows:
    print(f"Video ID: {row[0]}")
    print(f"Title: {row[1]}")
    print(f"Image URL: {row[2]}")
    print(f"Video URL: {row[3]}")
    print(f"Category: {row[4]}")
    print("-" * 30)

print("\nIssue Analysis:")
if len(rows) > 0:
    empty_video_urls = [row for row in rows if not row[3] or row[3].strip() == ""]
    if empty_video_urls:
        print(f"❌ {len(empty_video_urls)} videos have EMPTY video URLs")
        print("This is why videos are not playing on main website!")
    else:
        print("✅ All videos have video URLs")
else:
    print("❌ No video entries found")

conn.close()
