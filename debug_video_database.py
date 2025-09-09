import sqlite3

print("VIDEO DATABASE ANALYSIS")
print("="*30)

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Get all videos
cursor.execute('SELECT * FROM gallery_items WHERE category = "Videos"')
videos = cursor.fetchall()

print("All video entries:")
for video in videos:
    print(f"\nID: {video[0]}")
    print(f"Title: {video[1]}")
    print(f"Description: {video[2]}")
    print(f"Image URL: {video[3]}")
    print(f"Event Date: {video[4]}")
    print(f"Category: {video[5]}")
    print(f"Is Featured: {video[6]}")
    print(f"Is Active: {video[7]}")
    print(f"Created: {video[8]}")
    print(f"Updated: {video[9]}")
    print(f"Video URL: {video[10]}")
    print("-" * 30)

# Check if there are working YouTube URLs
working_videos = []
broken_videos = []

for video in videos:
    if video[10] and video[10].startswith('http'):
        working_videos.append(video)
    else:
        broken_videos.append(video)

print(f"\n✅ Working videos: {len(working_videos)}")
print(f"❌ Broken videos: {len(broken_videos)}")

if broken_videos:
    print("\nFixing broken videos with working YouTube URLs...")
    
    # Update broken videos with working URLs
    for video in broken_videos:
        if "self" in video[1].lower() or "defense" in video[1].lower():
            new_url = "https://youtu.be/T7aNhNdaRUk"  # Self defense - shorter YouTube URL
            print(f"Fixing: {video[1]} → {new_url}")
            cursor.execute('UPDATE gallery_items SET video_url = ? WHERE id = ?', (new_url, video[0]))
        elif "community" in video[1].lower():
            new_url = "https://youtu.be/E9RCpXMiLTA"  # Community program - shorter YouTube URL
            print(f"Fixing: {video[1]} → {new_url}")
            cursor.execute('UPDATE gallery_items SET video_url = ? WHERE id = ?', (new_url, video[0]))

conn.commit()
conn.close()

print("\n🎯 Try these YouTube URLs manually:")
print("Self Defense: https://youtu.be/T7aNhNdaRUk")
print("Community Program: https://youtu.be/E9RCpXMiLTA")
print("Women's Day: https://youtu.be/dQw4w9WgXcQ")  # Example URL
