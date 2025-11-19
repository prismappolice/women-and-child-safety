"""
Create upcoming_events table and add sample events
Admin can add/edit/delete events from dashboard
"""
import psycopg2
from datetime import datetime, timedelta

conn = psycopg2.connect(
    host='localhost',
    database='women_safety_db',
    user='postgres',
    password='postgres123',
    port='5432'
)
cursor = conn.cursor()

print("Creating upcoming_events table...")

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS upcoming_events (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        event_date DATE NOT NULL,
        event_time VARCHAR(50),
        location VARCHAR(255),
        organizer VARCHAR(100),
        contact_number VARCHAR(20),
        image_url VARCHAR(500),
        registration_link VARCHAR(500),
        is_featured BOOLEAN DEFAULT FALSE,
        is_active BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()
print("✅ Table created successfully!")

# Add sample upcoming events
sample_events = [
    {
        'title': 'Self Defense Training Workshop',
        'description': 'Free self-defense training workshop for women and girls. Learn basic self-defense techniques from certified trainers.',
        'event_date': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'),
        'event_time': '10:00 AM - 1:00 PM',
        'location': 'Police Training Center, Vijayawada',
        'organizer': 'AP Women Safety Wing',
        'contact_number': '0866-2424242',
        'image_url': '/static/images/self-defense-workshop.jpg',
        'registration_link': '/volunteer-registration',
        'is_featured': True,
        'is_active': True
    },
    {
        'title': 'Women Empowerment Seminar',
        'description': 'Interactive seminar on women rights, legal awareness, and available support systems.',
        'event_date': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d'),
        'event_time': '3:00 PM - 5:00 PM',
        'location': 'Community Hall, Visakhapatnam',
        'organizer': 'Shakthi Team - Visakhapatnam',
        'contact_number': '0891-2545454',
        'image_url': '/static/images/empowerment-seminar.jpg',
        'registration_link': '#',
        'is_featured': True,
        'is_active': True
    },
    {
        'title': 'Legal Aid Awareness Camp',
        'description': 'Free legal consultation and awareness about women-related laws, domestic violence act, and child protection.',
        'event_date': (datetime.now() + timedelta(days=21)).strftime('%Y-%m-%d'),
        'event_time': '11:00 AM - 4:00 PM',
        'location': 'District Court Complex, Guntur',
        'organizer': 'Legal Aid Cell',
        'contact_number': '0863-2323232',
        'image_url': '/static/images/legal-aid-camp.jpg',
        'registration_link': '#',
        'is_featured': False,
        'is_active': True
    }
]

print(f"\nAdding {len(sample_events)} sample events...")

for event in sample_events:
    cursor.execute("""
        INSERT INTO upcoming_events 
        (title, description, event_date, event_time, location, organizer, 
         contact_number, image_url, registration_link, is_featured, is_active)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        event['title'],
        event['description'],
        event['event_date'],
        event['event_time'],
        event['location'],
        event['organizer'],
        event['contact_number'],
        event['image_url'],
        event['registration_link'],
        event['is_featured'],
        event['is_active']
    ))
    print(f"   ✅ Added: {event['title']}")

conn.commit()

# Verify
cursor.execute("SELECT COUNT(*) FROM upcoming_events")
count = cursor.fetchone()[0]
print(f"\n✅ Total events in database: {count}")

# Show all events
cursor.execute("""
    SELECT id, title, event_date, location, is_featured 
    FROM upcoming_events 
    ORDER BY event_date
""")
events = cursor.fetchall()

print(f"\n📅 Upcoming Events:")
print("-" * 80)
for event_id, title, event_date, location, is_featured in events:
    featured = "⭐" if is_featured else "  "
    print(f"{featured} [{event_id}] {title}")
    print(f"      Date: {event_date} | Location: {location}")

print("\n" + "=" * 80)
print("✅ upcoming_events table ready!")
print("✅ Admin can now Add/Edit/Delete events from dashboard")
print("=" * 80)

conn.close()
