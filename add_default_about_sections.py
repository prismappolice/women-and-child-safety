import sqlite3

# Connect to database
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Default content for different sections
default_sections = [
    {
        'section_name': 'mission',
        'title': 'Our Mission',
        'content': '''<div class="mission-content">
            <p>The AP Women & Child Safety Wing is committed to creating a safe and secure environment for women and children across Andhra Pradesh. Our mission is to:</p>
            <ul>
                <li>Prevent crimes against women and children through proactive measures</li>
                <li>Provide immediate response and support to victims</li>
                <li>Conduct awareness programs and educational initiatives</li>
                <li>Work with communities to build a protective ecosystem</li>
                <li>Ensure justice and rehabilitation for survivors</li>
            </ul>
        </div>''',
        'image_url': '',
        'sort_order': 1
    },
    {
        'section_name': 'vision',
        'title': 'Our Vision',
        'content': '''<div class="vision-content">
            <p>To build a society where every woman and child can live with dignity, safety, and freedom from fear. We envision:</p>
            <ul>
                <li>Zero tolerance for crimes against women and children</li>
                <li>Empowered communities that protect their most vulnerable members</li>
                <li>Swift and effective justice delivery systems</li>
                <li>Comprehensive support services for survivors</li>
                <li>A culture of respect and equality for all</li>
            </ul>
        </div>''',
        'image_url': '',
        'sort_order': 2
    },
    {
        'section_name': 'officers',
        'title': 'Our Leadership Team',
        'content': '''<div class="officers-content">
            <div class="officer-card">
                <h4>IPS Officer Name</h4>
                <p><strong>Position:</strong> Superintendent of Police, Women & Child Safety</p>
                <p><strong>Experience:</strong> 15+ years in law enforcement</p>
                <p><strong>Specialization:</strong> Women and child protection, community policing</p>
                <p>Brief description of the officer's background and commitment to women's safety.</p>
            </div>
            
            <div class="officer-card">
                <h4>Deputy SP Name</h4>
                <p><strong>Position:</strong> Deputy Superintendent of Police</p>
                <p><strong>Experience:</strong> 12+ years in law enforcement</p>
                <p><strong>Specialization:</strong> Investigation and victim support</p>
                <p>Brief description of the officer's role and achievements.</p>
            </div>
            
            <p><em>Note: You can edit this section to add actual officer details, photos, and contact information.</em></p>
        </div>''',
        'image_url': '',
        'sort_order': 3
    },
    {
        'section_name': 'success_stories',
        'title': 'Success Stories & Impact',
        'content': '''<div class="success-stories">
            <div class="story-highlight">
                <h4>🏆 Major Achievements in 2024</h4>
                <ul>
                    <li>Prevented 500+ cases of domestic violence through timely intervention</li>
                    <li>Conducted 200+ awareness programs reaching 50,000+ women</li>
                    <li>Established 25 new women help desks across districts</li>
                    <li>Achieved 95% conviction rate in crimes against women</li>
                    <li>Trained 1,000+ community volunteers in women safety protocols</li>
                </ul>
            </div>
            
            <div class="impact-metrics">
                <h4>📊 Our Impact</h4>
                <ul>
                    <li><strong>Response Time:</strong> Average 15 minutes for emergency calls</li>
                    <li><strong>Helpline Calls:</strong> 10,000+ calls handled monthly</li>
                    <li><strong>Counseling Sessions:</strong> 3,000+ sessions conducted</li>
                    <li><strong>Legal Aid:</strong> Free legal support to 2,000+ women</li>
                </ul>
            </div>
            
            <p><em>Note: You can add specific success stories, case studies, and current statistics here.</em></p>
        </div>''',
        'image_url': '',
        'sort_order': 4
    }
]

# Insert default sections
for section in default_sections:
    # Check if section already exists
    cursor.execute('SELECT id FROM about_content WHERE section_name = ?', (section['section_name'],))
    existing = cursor.fetchone()
    
    if not existing:
        cursor.execute('''
            INSERT INTO about_content (section_name, title, content, image_url, sort_order, is_active)
            VALUES (?, ?, ?, ?, ?, 1)
        ''', (section['section_name'], section['title'], section['content'], section['image_url'], section['sort_order']))
        print(f"Added default content for: {section['title']}")
    else:
        print(f"Section '{section['title']}' already exists, skipping...")

conn.commit()
conn.close()

print("\nDefault about sections have been created!")
print("You can now edit these sections through the admin panel to add your specific content.")
print("\nTo access the admin panel:")
print("1. Go to: http://127.0.0.1:5000/admin-login")
print("2. Login with: admin / admin123")
print("3. Navigate to About Page management")
