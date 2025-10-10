# Database connection helper function
def get_db_connection():
    conn = sqlite3.connect('women_safety.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/event/<int:event_id>')
def event_details(event_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get event details
    cursor.execute('SELECT * FROM gallery_items WHERE id = ? AND category = "upcoming_events"', (event_id,))
    event = cursor.fetchone()
    
    if event is None:
        conn.close()
        flash('Event not found', 'error')
        return redirect(url_for('gallery'))
    
    # Convert tuple to dictionary for easier template access
    event_dict = {
        'id': event[0],
        'title': event[1],
        'image_url': event[2],
        'description': event[3],
        'category': event[4],
        'date': event[5],
        'location': event[6] if len(event) > 6 else None,
        'additional_details': event[7] if len(event) > 7 else None
    }
    
    conn.close()
    return render_template('event_details.html', event=event_dict)