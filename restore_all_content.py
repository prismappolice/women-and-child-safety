#!/usr/bin/env python3
"""
Restore all missing content for pages
"""
import sqlite3

def restore_all_content():
    """Restore all missing content tables and data"""
    print("🔧 Restoring All Page Content...")
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # 1. Create and populate about_content
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS about_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            section_name TEXT NOT NULL,
            title TEXT,
            content TEXT NOT NULL,
            image_url TEXT,
            sort_order INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Clear existing about content and add fresh content
    cursor.execute('DELETE FROM about_content')
    
    about_sections = [
        ('mission', 'Our Mission', '''
        <div class="mission-content">
            <p>The AP Women & Child Safety Wing is committed to creating a safe and secure environment for women and children across Andhra Pradesh.</p>
            <h4>Our Objectives:</h4>
            <ul>
                <li>Prevent crimes against women and children through proactive measures</li>
                <li>Provide immediate response and support to victims</li>
                <li>Conduct awareness programs and educational initiatives</li>
                <li>Work with communities to build a protective ecosystem</li>
                <li>Ensure justice and rehabilitation for survivors</li>
            </ul>
        </div>
        ''', '', 1),
        
        ('vision', 'Our Vision', '''
        <div class="vision-content">
            <p>To build a society where every woman and child can live with dignity, safety, and freedom from fear.</p>
            <h4>We Envision:</h4>
            <ul>
                <li>A harassment-free environment in all public and private spaces</li>
                <li>Empowered communities that actively protect vulnerable members</li>
                <li>Swift and effective justice delivery systems</li>
                <li>Comprehensive support systems for survivors</li>
                <li>Zero tolerance for gender-based violence</li>
            </ul>
        </div>
        ''', '', 2),
        
        ('about', 'About Us', '''
        <div class="about-content">
            <p>The Andhra Pradesh Women & Child Safety Wing operates under the state police department to ensure the safety and security of women and children across the state.</p>
            
            <h4>Established for:</h4>
            <ul>
                <li>24/7 emergency response services</li>
                <li>Specialized investigation units</li>
                <li>Community outreach programs</li>
                <li>Legal aid and counseling services</li>
                <li>Digital safety initiatives</li>
            </ul>
            
            <p>We work closely with various government departments, NGOs, and community organizations to create a comprehensive safety network.</p>
        </div>
        ''', '', 3)
    ]
    
    for section_name, title, content, image_url, sort_order in about_sections:
        cursor.execute('''
            INSERT INTO about_content (section_name, title, content, image_url, sort_order, is_active)
            VALUES (?, ?, ?, ?, ?, 1)
        ''', (section_name, title, content, image_url, sort_order))
    
    print("✅ About content restored")
    
    # 2. Create and populate safety_tips
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS safety_tips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT,
            icon_class TEXT,
            is_featured BOOLEAN DEFAULT 0,
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Clear and add safety tips
    cursor.execute('DELETE FROM safety_tips')
    
    safety_tips = [
        ('Personal Safety', '''
        <ul>
            <li>Always inform someone about your whereabouts</li>
            <li>Avoid isolated areas, especially during late hours</li>
            <li>Keep emergency contact numbers handy</li>
            <li>Trust your instincts - if something feels wrong, leave immediately</li>
            <li>Learn basic self-defense techniques</li>
        </ul>
        ''', 'personal', 'fas fa-shield-alt', 1),
        
        ('Digital Safety', '''
        <ul>
            <li>Don't share personal information with strangers online</li>
            <li>Use strong, unique passwords for all accounts</li>
            <li>Be cautious about location sharing on social media</li>
            <li>Report cyberbullying or online harassment immediately</li>
            <li>Keep your software and apps updated</li>
        </ul>
        ''', 'digital', 'fas fa-laptop', 1),
        
        ('Public Transport Safety', '''
        <ul>
            <li>Sit near the driver or conductor in buses</li>
            <li>Avoid empty compartments in trains</li>
            <li>Keep your belongings secure</li>
            <li>Be alert and aware of your surroundings</li>
            <li>Have transportation apps with GPS tracking</li>
        </ul>
        ''', 'transport', 'fas fa-bus', 1),
        
        ('Workplace Safety', '''
        <ul>
            <li>Know your company's harassment policy</li>
            <li>Document any inappropriate behavior</li>
            <li>Report incidents to HR or authorities</li>
            <li>Build a support network with trusted colleagues</li>
            <li>Know your legal rights and options</li>
        </ul>
        ''', 'workplace', 'fas fa-building', 1)
    ]
    
    for title, content, category, icon_class, is_featured in safety_tips:
        cursor.execute('''
            INSERT INTO safety_tips (title, content, category, icon_class, is_featured, is_active)
            VALUES (?, ?, ?, ?, ?, 1)
        ''', (title, content, category, icon_class, is_featured))
    
    print("✅ Safety tips restored")
    
    # 3. Create and populate pdf_resources
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pdf_resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            file_path TEXT NOT NULL,
            file_size INTEGER,
            download_count INTEGER DEFAULT 0,
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Clear and add PDF resources
    cursor.execute('DELETE FROM pdf_resources')
    
    pdf_resources = [
        ('Women Safety Guidelines', 'Comprehensive safety guidelines for women in various situations', '/static/pdfs/safety_guidelines.pdf', 1024, 0),
        ('Emergency Contact Numbers', 'List of important emergency contact numbers across AP districts', '/static/pdfs/emergency_contacts.pdf', 512, 0),
        ('Legal Rights Handbook', 'Know your legal rights and available remedies', '/static/pdfs/legal_rights.pdf', 2048, 0),
        ('Self Defense Guide', 'Basic self-defense techniques and tips', '/static/pdfs/self_defense.pdf', 1536, 0)
    ]
    
    for title, description, file_path, file_size, download_count in pdf_resources:
        cursor.execute('''
            INSERT INTO pdf_resources (title, description, file_path, file_size, download_count, is_active)
            VALUES (?, ?, ?, ?, ?, 1)
        ''', (title, description, file_path, file_size, download_count))
    
    print("✅ PDF resources restored")
    
    # 4. Create and populate home_content
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS home_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            section_name TEXT NOT NULL,
            title TEXT,
            content TEXT NOT NULL,
            image_url TEXT,
            link_url TEXT,
            icon_class TEXT,
            display_order INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Clear and add home content
    cursor.execute('DELETE FROM home_content')
    
    home_content = [
        ('hero', 'Ensuring Women & Child Safety in Andhra Pradesh', 'Our dedicated team works 24/7 to protect and empower women and children across the state.', '/static/images/slide1.jpg', '', '', 1),
        ('feature', '24/7 Emergency Response', 'Round-the-clock emergency services for immediate assistance and support.', '', '', 'fas fa-phone', 2),
        ('feature', 'Community Programs', 'Awareness programs and community initiatives to build safer neighborhoods.', '', '', 'fas fa-users', 3),
        ('feature', 'Legal Support', 'Expert legal assistance and guidance for victims and their families.', '', '', 'fas fa-gavel', 4)
    ]
    
    for section_name, title, content, image_url, link_url, icon_class, display_order in home_content:
        cursor.execute('''
            INSERT INTO home_content (section_name, title, content, image_url, link_url, icon_class, display_order, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, 1)
        ''', (section_name, title, content, image_url, link_url, icon_class, display_order))
    
    print("✅ Home content restored")
    
    conn.commit()
    conn.close()
    
    print("🎉 All content successfully restored!")
    print("📋 Content Summary:")
    print("   ✅ About Us page content")
    print("   ✅ Safety Tips")
    print("   ✅ PDF Resources")  
    print("   ✅ Home page content")

if __name__ == "__main__":
    restore_all_content()
