import sqlite3
import os
import requests

print("CHECKING VIDEO PLAYBACK ISSUES")
print("="*40)

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

cursor.execute('SELECT id, title, video_url FROM gallery_items WHERE category = "Videos" AND is_active = 1')
videos = cursor.fetchall()

print("Current videos in database:")
for video in videos:
    print(f"\nID: {video[0]} - {video[1]}")
    print(f"URL: {video[2]}")
    
    if video[2]:
        if video[2].startswith('http'):
            print("Type: YouTube/External link")
            # Test if YouTube link is accessible
            try:
                response = requests.head(video[2], timeout=5)
                print(f"Status: ✅ Accessible (HTTP {response.status_code})")
            except Exception as e:
                print(f"Status: ❌ Error - {str(e)}")
        elif video[2].startswith('/static/uploads/'):
            print("Type: Local video file")
            local_path = video[2].replace('/static/uploads/', 'static/uploads/')
            if os.path.exists(local_path):
                file_size = os.path.getsize(local_path)
                size_mb = file_size / (1024 * 1024)
                print(f"File size: {size_mb:.2f} MB")
                
                if size_mb > 50:
                    print("⚠️  WARNING: Large file (>50MB) - May cause slow loading")
                elif size_mb > 100:
                    print("❌ ERROR: Very large file (>100MB) - Will likely fail to play")
                else:
                    print("✅ File size OK for web playback")
            else:
                print("❌ ERROR: File not found on server")
        else:
            print("Type: Unknown format")

conn.close()

print("\n" + "="*40)
print("TESTING SPECIFIC VIDEOS:")

# Test the problematic videos
test_urls = [
    "https://www.youtube.com/watch?v=T7aNhNdaRUk",  # Self defense
    "https://www.youtube.com/watch?v=E9RCpXMiLTA"   # Community program
]

for i, url in enumerate(test_urls):
    video_name = ["Self Defense", "Community Program"][i]
    print(f"\n{video_name} video:")
    try:
        response = requests.head(url, timeout=10)
        print(f"  ✅ YouTube link working - HTTP {response.status_code}")
    except Exception as e:
        print(f"  ❌ YouTube link issue: {str(e)}")

print("\n💡 SOLUTIONS for video issues:")
print("1. For large files: Compress video or use external hosting")
print("2. For YouTube issues: Try different YouTube URLs")
print("3. For local files: Ensure files are in /static/uploads/")
print("4. Browser cache: Clear cache and try again")
