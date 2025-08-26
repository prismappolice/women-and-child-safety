import sqlite3
from datetime import datetime

def add_comprehensive_content_tables():
    """Add comprehensive content management tables for all pages"""
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Table for managing About page content
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS about_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            section_name TEXT NOT NULL, -- 'intro', 'mission', 'vision', 'team_member'
            title TEXT,
            content TEXT NOT NULL,
            image_url TEXT,
            sort_order INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Table for managing home page content
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS home_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            section_name TEXT NOT NULL, -- 'hero', 'feature', 'statistic', 'news'
            title TEXT,
            content TEXT NOT NULL,
            image_url TEXT,
            link_url TEXT,
            icon_class TEXT,
            sort_order INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Table for managing contact information
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contact_type TEXT NOT NULL, -- 'office', 'helpline', 'email', 'social'
            title TEXT NOT NULL,
            value TEXT NOT NULL,
            description TEXT,
            icon_class TEXT,
            is_primary INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Table for managing gallery items
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gallery_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            image_url TEXT NOT NULL,
            event_date DATE,
            category TEXT, -- 'event', 'training', 'awareness', 'ceremony'
            is_featured INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Table for managing website settings
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS site_settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            setting_key TEXT UNIQUE NOT NULL,
            setting_value TEXT NOT NULL,
            setting_type TEXT DEFAULT 'text', -- 'text', 'number', 'boolean', 'json'
            description TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Table for managing navigation menu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS navigation_menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            menu_title TEXT NOT NULL,
            menu_url TEXT NOT NULL,
            parent_id INTEGER DEFAULT NULL,
            sort_order INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    print("Comprehensive content management tables created successfully!")
    conn.commit()
    conn.close()

def insert_default_content_for_all_pages():
    """Insert default content for all pages"""
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Default About page content
    about_content = [
        ('intro', 'About Our Wing', 'The AP Women Safety Wing stands as a beacon of hope and protection for women across Andhra Pradesh. We are committed to creating a safer environment where every woman can live, work, and thrive without fear.', '', 1),
        ('mission', 'Our Mission', 'To eliminate violence against women and ensure their safety and empowerment through innovative initiatives, community engagement, and unwavering dedication.', '', 2),
        ('vision', 'Our Vision', 'A society where every woman feels safe, empowered, and can reach her full potential without fear of violence or discrimination.', '', 3),
        ('values', 'Our Values', 'Integrity, Compassion, Excellence, Transparency, Community Service, and Gender Equality guide everything we do.', '', 4)
    ]
    
    for content in about_content:
        cursor.execute('''
            INSERT OR IGNORE INTO about_content (section_name, title, content, image_url, sort_order)
            VALUES (?, ?, ?, ?, ?)
        ''', content)
    
    # Default Home page content
    home_content = [
        ('hero', 'Welcome to AP Women Safety Wing', 'Empowering women through safety, support, and solidarity. Your safety is our priority.', '/static/images/hero-banner.jpg', '', 'fas fa-shield-alt', 1),
        ('feature', 'SHE Teams', 'Special teams for women safety in public places', '/static/images/she-teams.jpg', '/initiatives', 'fas fa-users', 1),
        ('feature', '24/7 Helpline', 'Round the clock support for women in distress', '', 'tel:181', 'fas fa-phone', 2),
        ('feature', 'Legal Support', 'Complete legal assistance and guidance', '', '/contact', 'fas fa-gavel', 3),
        ('statistic', '500+', 'Women helped this year', '', '', 'fas fa-heart', 1),
        ('statistic', '50+', 'Districts covered', '', '', 'fas fa-map', 2),
        ('statistic', '1000+', 'Volunteers active', '', '', 'fas fa-users', 3)
    ]
    
    for content in home_content:
        cursor.execute('''
            INSERT OR IGNORE INTO home_content (section_name, title, content, image_url, link_url, icon_class, sort_order)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', content)
    
    # Default Contact information
    contact_info = [
        ('office', 'Head Office', 'DGP Office, Mangalagiri, Andhra Pradesh - 522503', 'Complete address of main office', 'fas fa-building', 1),
        ('helpline', 'Women Helpline', '181', '24/7 emergency helpline for women in distress', 'fas fa-phone', 1),
        ('helpline', 'Police Emergency', '100', 'General police emergency number', 'fas fa-shield-alt', 0),
        ('email', 'Official Email', 'womensafety@appolice.gov.in', 'For official communications and queries', 'fas fa-envelope', 1),
        ('social', 'Facebook', 'https://facebook.com/apwomensafety', 'Follow us on Facebook for updates', 'fab fa-facebook', 0),
        ('social', 'Twitter', 'https://twitter.com/apwomensafety', 'Follow us on Twitter for news', 'fab fa-twitter', 0)
    ]
    
    for contact in contact_info:
        cursor.execute('''
            INSERT OR IGNORE INTO contact_info (contact_type, title, value, description, icon_class, is_primary)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', contact)
    
    # Default Gallery items
    gallery_items = [
        ('Self Defense Workshop', 'Monthly self-defense training for college students', '/static/images/gallery/workshop1.jpg', '2024-08-15', 'training', 1),
        ('Awareness Campaign', 'Women safety awareness program in rural areas', '/static/images/gallery/awareness1.jpg', '2024-08-10', 'awareness', 0),
        ('SHE Team Training', 'Training program for new SHE team members', '/static/images/gallery/training1.jpg', '2024-08-05', 'training', 1),
        ('Community Meeting', 'Interactive session with community leaders', '/static/images/gallery/community1.jpg', '2024-07-30', 'event', 0)
    ]
    
    for item in gallery_items:
        cursor.execute('''
            INSERT OR IGNORE INTO gallery_items (title, description, image_url, event_date, category, is_featured)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', item)
    
    # Default Site settings
    site_settings = [
        ('site_title', 'AP Police Women & Child Safety Wing', 'text', 'Main website title'),
        ('site_description', 'Empowering women through safety, support, and solidarity', 'text', 'Website description'),
        ('contact_phone', '181', 'text', 'Primary contact phone number'),
        ('contact_email', 'womensafety@appolice.gov.in', 'text', 'Primary contact email'),
        ('office_hours', '24/7 Emergency Services Available', 'text', 'Office working hours'),
        ('social_facebook', 'https://facebook.com/apwomensafety', 'text', 'Facebook page URL'),
        ('social_twitter', 'https://twitter.com/apwomensafety', 'text', 'Twitter page URL'),
        ('enable_chatbot', 'true', 'boolean', 'Enable/disable chatbot'),
        ('maintenance_mode', 'false', 'boolean', 'Enable maintenance mode')
    ]
    
    for setting in site_settings:
        cursor.execute('''
            INSERT OR IGNORE INTO site_settings (setting_key, setting_value, setting_type, description)
            VALUES (?, ?, ?, ?)
        ''', setting)
    
    print("Default content for all pages inserted successfully!")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_comprehensive_content_tables()
    insert_default_content_for_all_pages()
    print("Comprehensive content management system setup complete!")
