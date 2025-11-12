from db_config import get_db_connection

def check_upcoming_events():
    """Check upcoming events in database"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, title, description, image_url, video_url, event_date, category, is_active
        FROM gallery_items
        WHERE category = 'upcoming_events'
        ORDER BY event_date
    """)
    events = cursor.fetchall()
    
    print(f"Total upcoming events: {len(events)}\n")
    
    for e in events:
        print(f"ID: {e[0]}")
        print(f"Title: {e[1]}")
        print(f"Description: {e[2][:50]}...")
        print(f"Image URL: {e[3]}")
        print(f"Video URL: {e[4]}")
        print(f"Event Date: {e[5]} (Type: {type(e[5])})")
        print(f"Category: {e[6]}")
        print(f"Active: {e[7]}")
        print("-" * 70)
    
    conn.close()

if __name__ == '__main__':
    check_upcoming_events()
