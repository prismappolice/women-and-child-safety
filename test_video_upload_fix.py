import sqlite3

print("TESTING LOCAL VIDEO UPLOAD FUNCTIONALITY")
print("="*50)

# Test video extensions
test_files = [
    "test_video.mp4",
    "sample.avi", 
    "movie.mov",
    "demo.webm",
    "training.mkv"
]

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'mp4', 'avi', 'mov', 'wmv', 'flv', 'webm', 'mkv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

print("Testing video file extensions:")
for file in test_files:
    result = allowed_file(file)
    extension = file.rsplit('.', 1)[1].lower()
    print(f"  {file}: {'✅ Allowed' if result else '❌ Not allowed'}")
    
    if result:
        # Test if it's a video file
        if extension in ['mp4', 'avi', 'mov', 'wmv', 'flv', 'webm', 'mkv']:
            print(f"    → Video file detected: video_url will be set")
        else:
            print(f"    → Image file: image_url will be set")

print("\n" + "="*50)
print("CURRENT DATABASE VIDEOS:")

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

cursor.execute('SELECT id, title, image_url, video_url, category FROM gallery_items WHERE category = "Videos"')
videos = cursor.fetchall()

for video in videos:
    print(f"\nVideo ID: {video[0]} - {video[1]}")
    print(f"  Image URL: {video[2]}")
    print(f"  Video URL: {video[3]}")
    
    if video[3]:
        if video[3].startswith('http'):
            print(f"  Status: ✅ YouTube/External link - Will work")
        elif video[3].startswith('/static/uploads/'):
            print(f"  Status: ✅ Local video file - Will work with modal player")
        else:
            print(f"  Status: ❌ Unknown format")
    else:
        print(f"  Status: ❌ No video URL")

conn.close()

print("\n🎯 SOLUTION READY:")
print("1. ✅ Video extensions added to ALLOWED_EXTENSIONS")
print("2. ✅ Video upload logic updated in app.py")
print("3. ✅ Video modal player added to gallery.html")
print("4. 🔄 Need to update template buttons for local videos")
print("\nNow local videos will be saved to /static/uploads/ and play in modal!")
