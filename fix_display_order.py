import sqlite3

def check_success_stories_order():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Check current stories and their sort order
    cursor.execute('SELECT id, title, sort_order, is_active FROM success_stories ORDER BY sort_order, id')
    stories = cursor.fetchall()
    
    print("Current Success Stories Order:")
    print("ID | Title | Sort Order | Active")
    print("-" * 50)
    for story in stories:
        title = story[1][:30] + "..." if len(story[1]) > 30 else story[1]
        print(f"{story[0]} | {title} | {story[2]} | {story[3]}")
    
    # Update sort order to fix display
    print("\nUpdating sort order...")
    
    # Set proper sort order (1, 2, 3, etc.)
    updates = [
        (1, 1),  # First story - sort order 1
        (2, 2),  # Second story - sort order 2  
        (3, 3),  # Third story - sort order 3
    ]
    
    for story_id, new_sort_order in updates:
        cursor.execute('UPDATE success_stories SET sort_order = ? WHERE id = ?', (new_sort_order, story_id))
    
    conn.commit()
    
    # Check updated order
    cursor.execute('SELECT id, title, sort_order FROM success_stories ORDER BY sort_order, id')
    updated_stories = cursor.fetchall()
    
    print("\nUpdated Success Stories Order:")
    print("ID | Title | Sort Order")
    print("-" * 40)
    for story in updated_stories:
        title = story[1][:30] + "..." if len(story[1]) > 30 else story[1]
        print(f"{story[0]} | {title} | {story[2]}")
    
    conn.close()
    print("\nSuccess stories order fixed!")

if __name__ == "__main__":
    check_success_stories_order()
