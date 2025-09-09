import sqlite3

print("Video Upload Analysis - Local vs YouTube")
print("="*50)

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check all video entries
cursor.execute('SELECT id, title, image_url, video_url, category FROM gallery_items WHERE category = "Videos"')
videos = cursor.fetchall()

print("Current video entries:")
for video in videos:
    print(f"\nVideo ID: {video[0]}")
    print(f"Title: {video[1]}")
    print(f"Image URL: {video[2]}")
    print(f"Video URL: {video[3]}")
    
    if not video[3]:
        print("❌ Status: No video URL - Won't play")
    elif video[3].startswith('http'):
        print("✅ Status: YouTube/Online URL - Will play")
    elif video[3].startswith('C:') or video[3].startswith('/'):
        print("❌ Status: Local file path - Won't play on website")
    else:
        print("⚠️ Status: Unknown URL format")

print("\n" + "="*50)
print("ISSUE ANALYSIS:")
print("✅ YouTube links work on main website")
print("❌ Local file paths (C:/Users/...) don't work on website")
print("💡 Local videos need to be uploaded to /static/uploads/ folder")

conn.close()
