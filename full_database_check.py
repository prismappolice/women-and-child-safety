import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

print("=== SUCCESS STORIES DATABASE CHECK ===")
print()

# Check table structure
cursor.execute("PRAGMA table_info(success_stories)")
columns = cursor.fetchall()
print("Table Structure:")
for i, col in enumerate(columns):
    print(f"  {i}: {col[1]} ({col[2]})")
print()

# Check all success stories
cursor.execute('SELECT * FROM success_stories ORDER BY id')
stories = cursor.fetchall()

print(f"Total Success Stories: {len(stories)}")
print("-" * 60)

for story in stories:
    print(f"ID: {story[0]}")
    print(f"Title: {story[1]}")
    print(f"Description: {story[2][:100]}...")
    print(f"Date: {story[3]}")
    print(f"Stats: {story[4]},{story[5]} | {story[6]},{story[7]} | {story[8]},{story[9]}")
    print(f"Image URL: {story[10]}")
    print(f"Sort Order: {story[11]}")
    print(f"Is Active: {story[12]}")
    print("-" * 60)

conn.close()
