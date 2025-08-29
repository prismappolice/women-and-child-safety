import sqlite3

# Test database update functionality
def test_update_description():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Check if there are any success stories
    cursor.execute('SELECT id, title, description FROM success_stories LIMIT 1')
    story = cursor.fetchone()
    
    if story:
        print(f"Testing with story ID: {story[0]}")
        print(f"Current title: {story[1]}")
        print(f"Current description: {story[2][:100]}...")
        
        # Try updating the description
        test_description = f"UPDATED TEST DESCRIPTION - {story[2]}"
        cursor.execute('''
            UPDATE success_stories 
            SET description=?
            WHERE id=?
        ''', (test_description, story[0]))
        conn.commit()
        
        # Verify the update
        cursor.execute('SELECT description FROM success_stories WHERE id=?', (story[0],))
        updated_story = cursor.fetchone()
        
        if updated_story:
            print(f"Updated description: {updated_story[0][:100]}...")
            print("✅ Database update working correctly!")
        else:
            print("❌ Failed to retrieve updated story")
    else:
        print("No success stories found in database")
    
    conn.close()

if __name__ == "__main__":
    test_update_description()
