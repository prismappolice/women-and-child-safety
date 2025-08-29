import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

cursor.execute('SELECT id, title, image_url FROM success_stories')
stories = cursor.fetchall()

print("Success Stories Image URLs:")
for story in stories:
    print(f"ID: {story[0]}")
    print(f"Title: {story[1]}")
    print(f"Image URL: {story[2]}")
    print("-" * 50)

conn.close()
