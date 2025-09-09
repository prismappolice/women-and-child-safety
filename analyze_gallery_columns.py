import sqlite3

print("Gallery Route Query Column Analysis")
print("="*50)

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Run exact gallery route query
cursor.execute('''SELECT id, title, description, image_url, video_url, 
                 category, event_date, is_featured, is_active 
                 FROM gallery_items WHERE is_active = 1 AND category = "Videos"
                 ORDER BY category, is_featured DESC, event_date DESC''')
video_items = cursor.fetchall()

print("Gallery route query order:")
print("0: id")
print("1: title") 
print("2: description")
print("3: image_url")
print("4: video_url")
print("5: category")
print("6: event_date")
print("7: is_featured")
print("8: is_active")

print("\nVideo data:")
for item in video_items:
    print(f"Title: {item[1]}")
    print(f"  Category (index 5): {item[5]}")
    print(f"  Event Date (index 6): {item[6]}")
    print(f"  Video URL (index 4): {item[4]}")
    print()

print("Template should use:")
print("- item[4] for video_url ✅")
print("- item[5] for category ✅") 
print("- item[6] for event_date ✅")

conn.close()
