from db_config import get_db_connection

conn = get_db_connection('main')
cursor = conn.cursor()

# Check video items
cursor.execute("SELECT id, title, category, event_date, video_url FROM gallery_items WHERE category = 'Videos' LIMIT 3")
items = cursor.fetchall()
print("\nVideo items:")
for item in items:
    print(f"  ID: {item[0]}, Title: {item[1]}, Date: {item[3]}, Video: {item[4]}")

conn.close()
