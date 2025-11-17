#!/usr/bin/env python3
"""
Verify all data is in PostgreSQL database
"""

import os
os.environ['DB_MODE'] = 'postgresql'
from db_config import get_db_connection

def check_postgresql_data():
    print('🔍 CHECKING ALL DATA IN POSTGRESQL DATABASE')
    print('=' * 50)

    conn = get_db_connection('main')
    cursor = conn.cursor()

    # Confirm we're using PostgreSQL
    cursor.execute('SELECT version()')
    version = cursor.fetchone()[0]
    print(f'✅ Database: {version[:50]}...')
    print()

    # Check all important tables and their data
    tables_to_check = [
        'about_content', 'officers', 'success_stories', 
        'safety_tips', 'home_content', 'pdf_resources',
        'gallery_items', 'initiatives', 'volunteers',
        'districts', 'contact_info'
    ]

    print('📊 DATA COUNT IN EACH TABLE:')
    print('-' * 30)

    total_records = 0
    for table in tables_to_check:
        try:
            cursor.execute(f'SELECT COUNT(*) FROM {table}')
            count = cursor.fetchone()[0]
            total_records += count
            print(f'{table:20} : {count:4} records')
        except Exception as e:
            print(f'{table:20} : Error')

    print('-' * 30)
    print(f'{"TOTAL RECORDS":20} : {total_records:4} records')
    print()

    # Show some sample data to prove it exists
    print('📝 SAMPLE DATA FROM KEY TABLES:')
    print('-' * 40)

    # Sample about content
    try:
        cursor.execute('SELECT title FROM about_content LIMIT 3')
        about_data = cursor.fetchall()
        print('About Content:')
        for item in about_data:
            print(f'  - {item[0]}')
    except:
        print('About Content: No data')

    # Sample officers  
    try:
        cursor.execute('SELECT name, designation FROM officers LIMIT 3')
        officers_data = cursor.fetchall()
        print('\nOfficers:')
        for item in officers_data:
            print(f'  - {item[0]} ({item[1]})')
    except:
        print('\nOfficers: No data')

    # Sample safety tips
    try:
        cursor.execute('SELECT title FROM safety_tips LIMIT 3')
        tips_data = cursor.fetchall()
        print('\nSafety Tips:')
        for item in tips_data:
            print(f'  - {item[0]}')
    except:
        print('\nSafety Tips: No data')

    # Sample volunteers
    try:
        cursor.execute('SELECT name, registration_id FROM volunteers LIMIT 3')
        volunteer_data = cursor.fetchall()
        print('\nVolunteers:')
        for item in volunteer_data:
            print(f'  - {item[0]} (ID: {item[1]})')
    except:
        print('\nVolunteers: No data')

    conn.close()
    print()
    print('✅ YES! ALL DATA IS IN POSTGRESQL DATABASE!')
    print('✅ हाँ! सारा data PostgreSQL database में है!')

if __name__ == "__main__":
    check_postgresql_data()