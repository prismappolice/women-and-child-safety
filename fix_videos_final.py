import sqlite3

print("VIDEO TROUBLESHOOTING")
print("="*25)

try:
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Get current videos
    cursor.execute("SELECT id, title, video_url FROM gallery_items WHERE category = 'Videos' AND is_active = 1")
    videos = cursor.fetchall()
    
    print("Current active videos:")
    for video in videos:
        print(f"{video[0]}: {video[1]} → {video[2]}")
    
    # Fix problematic videos
    fixed = 0
    
    # Self Defense Workshop
    cursor.execute("UPDATE gallery_items SET video_url = 'https://youtu.be/T7aNhNdaRUk' WHERE title LIKE '%self%defense%' OR title LIKE '%defense%'")
    if cursor.rowcount > 0:
        print("✅ Fixed Self Defense video")
        fixed += cursor.rowcount
    
    # Community Program  
    cursor.execute("UPDATE gallery_items SET video_url = 'https://youtu.be/E9RCpXMiLTA' WHERE title LIKE '%community%'")
    if cursor.rowcount > 0:
        print("✅ Fixed Community Program video")
        fixed += cursor.rowcount
    
    # Add Women's Day video if missing
    cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE title LIKE '%women%day%'")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO gallery_items 
            (title, description, image_url, video_url, category, is_featured, is_active)
            VALUES (?, ?, ?, ?, ?, 1, 1)
        ''', (
            "Women's Day Special",
            "Celebrating International Women's Day with special programs and initiatives.",
            "/static/images/slide5.jpg",
            "https://youtu.be/dQw4w9WgXcQ",
            "Videos"
        ))
        print("✅ Added Women's Day video")
        fixed += 1
    
    conn.commit()
    
    # Show updated videos
    cursor.execute("SELECT id, title, video_url FROM gallery_items WHERE category = 'Videos' AND is_active = 1")
    updated_videos = cursor.fetchall()
    
    print(f"\nUpdated videos ({len(updated_videos)} total):")
    for video in updated_videos:
        status = "✅" if video[2] and video[2].startswith('http') else "❌"
        print(f"{status} {video[1]}: {video[2]}")
    
    print(f"\n🔧 Fixed {fixed} video(s)")
    
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")

print("\n🎯 Test steps:")
print("1. Refresh the gallery page: http://localhost:5000/gallery")
print("2. Click on video buttons in Videos section")
print("3. YouTube videos should open in new tab")
print("4. Check browser console for any errors")

print("\n💡 If videos still don't work:")
print("- Check internet connection for YouTube")
print("- Try different YouTube URLs")
print("- Clear browser cache")
print("- Check browser console for JavaScript errors")
