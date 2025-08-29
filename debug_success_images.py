import sqlite3

# Connect to database
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check success stories
cursor.execute('SELECT id, title, image_url FROM success_stories ORDER BY id')
stories = cursor.fetchall()

print("Success Stories in Database:")
print("-" * 50)
for story in stories:
    print(f"ID: {story[0]}")
    print(f"Title: {story[1]}")
    print(f"Image URL: {story[2]}")
    print("-" * 30)

conn.close()

# Check actual uploaded files
import os
uploads_dir = "static/uploads"
if os.path.exists(uploads_dir):
    print("\nFiles in uploads directory:")
    for file in os.listdir(uploads_dir):
        if file.startswith('success_story'):
            print(f"  {file}")
            # Check file size
            file_path = os.path.join(uploads_dir, file)
            size = os.path.getsize(file_path)
            print(f"    Size: {size} bytes")
