import sqlite3

def fix_success_stories_table():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Check if the new columns exist
    cursor.execute("PRAGMA table_info(success_stories)")
    columns = [col[1] for col in cursor.fetchall()]
    
    # Add missing columns if they don't exist
    missing_columns = []
    expected_columns = {
        'description': 'TEXT',
        'date': 'TEXT',
        'stat1_number': 'TEXT',
        'stat1_label': 'TEXT',
        'stat2_number': 'TEXT',
        'stat2_label': 'TEXT',
        'stat3_number': 'TEXT',
        'stat3_label': 'TEXT',
        'is_active': 'INTEGER DEFAULT 1',
        'sort_order': 'INTEGER DEFAULT 0',
        'created_at': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
    }
    
    for column, col_type in expected_columns.items():
        if column not in columns:
            missing_columns.append((column, col_type))
    
    # Add missing columns
    for column, col_type in missing_columns:
        try:
            cursor.execute(f"ALTER TABLE success_stories ADD COLUMN {column} {col_type}")
            print(f"Added column: {column}")
        except sqlite3.OperationalError as e:
            print(f"Error adding column {column}: {e}")
    
    # Update existing stories with proper data mapping
    if 'story_content' in columns and 'description' in [col[0] for col in missing_columns]:
        cursor.execute("UPDATE success_stories SET description = story_content WHERE description IS NULL")
        print("Mapped story_content to description")
    
    if 'date_occurred' in columns and 'date' in [col[0] for col in missing_columns]:
        cursor.execute("UPDATE success_stories SET date = date_occurred WHERE date IS NULL")
        print("Mapped date_occurred to date")
    
    if 'position_order' in columns and 'sort_order' in [col[0] for col in missing_columns]:
        cursor.execute("UPDATE success_stories SET sort_order = position_order WHERE sort_order IS NULL")
        print("Mapped position_order to sort_order")
    
    conn.commit()
    
    # Show current data
    cursor.execute("SELECT * FROM success_stories")
    stories = cursor.fetchall()
    print(f"\nCurrent success stories in DB: {len(stories)}")
    for story in stories:
        print(story)
    
    conn.close()
    print("Success stories table structure fixed!")

if __name__ == "__main__":
    fix_success_stories_table()
