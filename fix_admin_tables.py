import sqlite3
from datetime import datetime

def create_content_tables():
    """Create tables for dynamic content management"""
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Table for managing safety tips
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS safety_tips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            title TEXT NOT NULL,
            icon TEXT NOT NULL,
            tips TEXT NOT NULL,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Table for managing initiatives
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS initiatives (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            image_url TEXT,
            is_featured INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Table for managing PDF resources
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pdf_resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            file_name TEXT NOT NULL,
            file_path TEXT NOT NULL,
            icon TEXT DEFAULT 'fas fa-file-pdf',
            download_count INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Table for managing events
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            event_date DATE,
            location TEXT,
            image_url TEXT,
            is_upcoming INTEGER DEFAULT 1,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Table for managing general content (about, contact info, etc.)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS page_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            page_name TEXT NOT NULL,
            section_name TEXT NOT NULL,
            content_type TEXT NOT NULL, -- 'text', 'html', 'image', 'video'
            content_value TEXT NOT NULL,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Table for emergency numbers
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emergency_numbers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT NOT NULL,
            label TEXT NOT NULL,
            description TEXT,
            is_active INTEGER DEFAULT 1,
            sort_order INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    print("Content management tables created successfully!")
    conn.commit()
    conn.close()

def insert_default_data():
    """Insert default content data"""
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Insert default safety tips
    safety_tips_data = [
        ('Home Safety', 'Home Safety', 'fas fa-home', '''Always lock doors and windows when leaving home
Install proper lighting around your home
Know your neighbors and maintain good relationships
Keep emergency numbers readily available
Don't open doors to strangers
Have a safety plan and emergency contact list'''),
        
        ('Transportation Safety', 'Transportation Safety', 'fas fa-car', '''Always book verified cab services
Share your ride details with family/friends
Sit behind the driver, not next to them
Keep emergency contacts on speed dial
Trust your instincts if something feels wrong
Avoid traveling alone late at night'''),
        
        ('Digital Safety', 'Digital Safety', 'fas fa-mobile-alt', '''Keep your social media profiles private
Don't share personal information online
Be cautious about meeting online friends
Report cyberbullying immediately
Use strong passwords and two-factor authentication
Be aware of online predators and scams'''),
        
        ('Workplace Safety', 'Workplace Safety', 'fas fa-graduation-cap', '''Know your company's harassment policy
Report inappropriate behavior immediately
Maintain professional boundaries
Document any incidents of harassment
Seek support from HR or management
Know your rights and legal protections'''),
        
        ('Public Places', 'Public Places', 'fas fa-users', '''Stay in well-lit, populated areas
Walk confidently and stay alert
Avoid wearing expensive jewelry in public
Keep your phone charged and accessible
Trust your instincts about people and situations
Learn basic self-defense techniques'''),
        
        ('Emergency Preparedness', 'Emergency Preparedness', 'fas fa-phone', '''Save emergency numbers: 181, 1091, 100
Install safety apps on your phone
Inform family about your whereabouts
Keep local police station numbers handy
Know the nearest hospital locations
Have a personal safety plan''')
    ]
    
    for tip in safety_tips_data:
        cursor.execute('''
            INSERT OR IGNORE INTO safety_tips (category, title, icon, tips)
            VALUES (?, ?, ?, ?)
        ''', tip)
    
    # Insert default emergency numbers
    emergency_numbers_data = [
        ('181', 'Women Helpline', 'National women helpline for immediate assistance', 1),
        ('100', 'Police Emergency', 'Police emergency number for immediate help', 2),
        ('112', 'National Emergency', 'Universal emergency number for all emergencies', 3),
        ('1091', 'Women\'s Helpline', 'Dedicated women\'s helpline for support and guidance', 4)
    ]
    
    for num in emergency_numbers_data:
        cursor.execute('''
            INSERT OR IGNORE INTO emergency_numbers (number, label, description, sort_order)
            VALUES (?, ?, ?, ?)
        ''', num)
    
    # Insert default PDF resources
    pdf_resources_data = [
        ('Safety Guidelines', 'Comprehensive safety guidelines for women in various situations including home, workplace, and public spaces.', 'safety_guidelines.pdf', '/static/pdfs/safety_guidelines.pdf', 'fas fa-file-pdf'),
        ('Legal Rights Handbook', 'Know your legal rights and protections under various laws related to women\'s safety and empowerment.', 'legal_rights.pdf', '/static/pdfs/legal_rights.pdf', 'fas fa-gavel'),
        ('Emergency Contact Directory', 'Complete directory of emergency contacts, helplines, and support services across Andhra Pradesh.', 'emergency_contacts.pdf', '/static/pdfs/emergency_contacts.pdf', 'fas fa-phone'),
        ('Self Defense Manual', 'Basic self-defense techniques and personal safety tips for women of all ages.', 'self_defense.pdf', '/static/pdfs/self_defense.pdf', 'fas fa-shield-alt'),
        ('Cyber Safety Guide', 'Essential tips for staying safe online, protecting privacy, and avoiding cyber crimes.', 'cyber_safety.pdf', '/static/pdfs/cyber_safety.pdf', 'fas fa-laptop'),
        ('Community Support Programs', 'Information about various community support programs and how to access them.', 'community_support.pdf', '/static/pdfs/community_support.pdf', 'fas fa-users')
    ]
    
    for pdf in pdf_resources_data:
        cursor.execute('''
            INSERT OR IGNORE INTO pdf_resources (title, description, file_name, file_path, icon)
            VALUES (?, ?, ?, ?, ?)
        ''', pdf)
    
    print("Default data inserted successfully!")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_content_tables()
    insert_default_data()
    print("Database setup complete!")
