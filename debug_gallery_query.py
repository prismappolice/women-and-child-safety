import sqlite3

print("Checking Gallery Route Query vs Template Expectations")
print("="*60)

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Run the same query as gallery route
cursor.execute('''SELECT id, title, description, image_url, video_url, 
                 category, event_date, is_featured, is_active 
                 FROM gallery_items WHERE is_active = 1 
                 ORDER BY category, is_featured DESC, event_date DESC''')
gallery_items = cursor.fetchall()

print("Gallery route query returns data in this order:")
print("Index 0: id")
print("Index 1: title") 
print("Index 2: description")
print("Index 3: image_url")
print("Index 4: video_url")  # This is the issue!
print("Index 5: category")
print("Index 6: event_date")
print("Index 7: is_featured")
print("Index 8: is_active")

print("\nBut template expects video_url at index 10!")
print("Template issue: item[10] won't work with this query!")

# Check video data
video_items = [item for item in gallery_items if item[5] == 'Videos']
print(f"\nFound {len(video_items)} videos:")
for item in video_items:
    print(f"Title: {item[1]}, Video URL at index 4: {item[4]}")

conn.close()

print("\nFIX NEEDED: Template should use item[4] for video_url, not item[10]!")
