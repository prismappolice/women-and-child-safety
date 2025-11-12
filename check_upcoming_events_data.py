from db_config import get_db_connection

def check_upcoming_events_data():
    """Check Upcoming Events data"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, title, event_date, image_url, video_url, is_active
        FROM gallery_items
        WHERE category = 'Upcoming Events'
        ORDER BY event_date
    """)
    events = cursor.fetchall()
    
    print(f"Total Upcoming Events: {len(events)}\n")
    
    for e in events:
        print(f"ID: {e[0]}")
        print(f"Title: {e[1]}")
        print(f"Event Date: '{e[2]}'")
        print(f"Image URL: {e[3]}")
        print(f"Video URL: {e[4]}")
        print(f"Active: {e[5]}")
        print("-" * 70)
    
    conn.close()

if __name__ == '__main__':
    check_upcoming_events_data()
