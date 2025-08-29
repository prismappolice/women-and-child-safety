import sqlite3

# Connect to database
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Add new success story
cursor.execute('''
    INSERT INTO success_stories 
    (title, description, date, stat1_number, stat1_label, 
     stat2_number, stat2_label, stat3_number, stat3_label, 
     image_url, sort_order, is_active)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (
    'Enhanced Women Safety Initiative in Tirupati',
    'A comprehensive safety drive was launched in Tirupati district covering educational institutions, workplaces, and public spaces. Through coordinated efforts of SHE Teams, local police, and community volunteers, we achieved a significant reduction in crimes against women. The initiative included safety workshops, self-defense training, and installation of emergency help points.',
    'December 2024',
    '25',
    'Safety Workshops',
    '500+',
    'Women Trained',
    '85%',
    'Crime Reduction',
    '/static/images/success-tirupati.jpg',
    7,
    1
))

conn.commit()
conn.close()

print("New success story added successfully!")
