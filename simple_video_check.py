import sqlite3
import os

# Simple database check
db_path = "women_safety.db"
if os.path.exists(db_path):
    print(f"✅ Database found: {db_path}")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get all gallery items
    cursor.execute("SELECT COUNT(*) FROM gallery_items")
    total = cursor.fetchone()[0]
    print(f"Total gallery items: {total}")
    
    # Get videos specifically
    cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = 'Videos'")
    video_count = cursor.fetchone()[0]
    print(f"Total videos: {video_count}")
    
    # List all videos
    cursor.execute("SELECT id, title, video_url FROM gallery_items WHERE category = 'Videos'")
    videos = cursor.fetchall()
    
    print("\nAll videos:")
    for v in videos:
        print(f"ID:{v[0]} | {v[1][:30]}... | URL: {v[2]}")
    
    # Quick fix for known issues
    cursor.execute("UPDATE gallery_items SET video_url = 'https://youtu.be/T7aNhNdaRUk' WHERE id = 68")
    cursor.execute("UPDATE gallery_items SET video_url = 'https://youtu.be/E9RCpXMiLTA' WHERE id = 69")
    conn.commit()
    
    print("\n✅ Applied quick fixes")
    
    conn.close()
else:
    print("❌ Database not found!")

print("\n🔍 File size issue analysis:")
print("Large video files (>10MB) may not play smoothly in browsers")
print("Best practices:")
print("- Keep videos under 10MB for web")
print("- Use MP4 format with H.264 codec")
print("- Consider YouTube hosting for large files")
print("- Compress videos before uploading")

print("\n🎯 Next steps:")
print("1. Check if videos play in browser directly")
print("2. Test with smaller video files")
print("3. Use YouTube for large content")
print("4. Clear browser cache and try again")
