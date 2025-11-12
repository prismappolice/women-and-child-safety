import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

TABLES = [
    ('district_sps', 'district_sps_id_seq', True),
    ('shakthi_teams', 'shakthi_teams_id_seq', True),
    ('women_police_stations', 'women_police_stations_id_seq', True),
    ('one_stop_centers', 'one_stop_centers_id_seq', True),
    ('volunteers', 'volunteers_id_seq', False),
    ('gallery_items', 'gallery_items_id_seq', True),
    ('pdf_resources', 'pdf_resources_id_seq', True),
    ('safety_tips', 'safety_tips_id_seq', True),
    ('initiatives', 'initiatives_id_seq', True),
    ('officers', 'officers_id_seq', True),
    ('success_stories', 'success_stories_id_seq', True),
    ('contact_info', 'contact_info_id_seq', True),
    ('events', 'events_id_seq', True),
    ('home_content', 'home_content_id_seq', True),
]

print("=" * 80)
print("FINAL VERIFICATION - ALL TABLES")
print("=" * 80)

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

all_passed = True
total = 0

for table, seq, has_is_active in TABLES:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    total += count
    
    cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE id IS NULL")
    null_ids = cursor.fetchone()[0]
    
    null_active = 0
    if has_is_active:
        cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE is_active IS NULL")
        null_active = cursor.fetchone()[0]
    
    cursor.execute(f"SELECT nextval('{seq}')")
    next_id = cursor.fetchone()[0]
    cursor.execute(f"SELECT setval('{seq}', {next_id - 1})")
    
    if null_ids > 0 or null_active > 0:
        print(f"❌ {table}: NULL IDs={null_ids}, NULL is_active={null_active}")
        all_passed = False
    else:
        print(f"✅ {table}: {count} records, next ID: {next_id}")

conn.close()

print("=" * 80)
print(f"Total records: {total}")
if all_passed:
    print("✅ ALL TABLES READY FOR UNLIMITED ADD/DELETE!")
else:
    print("❌ Issues found")
print("=" * 80)
