import sqlite3

def add_sample_home_content():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Clear existing home content
    cursor.execute('DELETE FROM home_content')
    
    # Add sample Hero content
    cursor.execute('''
        INSERT INTO home_content (section_name, title, content, image_url, link_url, icon_class, sort_order, is_active)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', ('hero', 'Andhra Pradesh Women & Child Safety Wing', 
          'Dedicated to ensuring the safety and security of women and children across Andhra Pradesh. Join us in creating a safer community for everyone.',
          '/static/images/hero-bg.jpg', '#contact', 'fas fa-shield-alt', 1, 1))
    
    # Add sample Features
    features = [
        ('Emergency Response', '24/7 emergency helpline and rapid response system for women in distress.', 'fas fa-phone-alt', 1),
        ('Safety Education', 'Comprehensive safety awareness programs and self-defense training workshops.', 'fas fa-graduation-cap', 2),
        ('Community Support', 'Building strong community networks to support and protect women and children.', 'fas fa-hands-helping', 3),
        ('Legal Assistance', 'Free legal aid and counseling services for victims of violence and harassment.', 'fas fa-gavel', 4)
    ]
    
    for title, content, icon, order in features:
        cursor.execute('''
            INSERT INTO home_content (section_name, title, content, icon_class, sort_order, is_active)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('features', title, content, icon, order, 1))
    
    # Add sample Statistics
    statistics = [
        ('10,000+', 'Women Helped', 'fas fa-female', 1),
        ('50+', 'Safety Programs', 'fas fa-clipboard-list', 2),
        ('100+', 'Volunteers', 'fas fa-users', 3),
        ('24/7', 'Emergency Support', 'fas fa-clock', 4)
    ]
    
    for title, content, icon, order in statistics:
        cursor.execute('''
            INSERT INTO home_content (section_name, title, content, icon_class, sort_order, is_active)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('statistics', title, content, icon, order, 1))
    
    # Add sample Testimonials
    testimonials = [
        ('Life-Changing Support', 'The safety wing helped me when I needed it most. Their quick response and compassionate support changed my life. - Priya, Hyderabad', 'fas fa-quote-left', 1),
        ('Excellent Training', 'The self-defense workshop gave me confidence and practical skills to protect myself. Highly recommended! - Sunitha, Vijayawada', 'fas fa-star', 2)
    ]
    
    for title, content, icon, order in testimonials:
        cursor.execute('''
            INSERT INTO home_content (section_name, title, content, icon_class, sort_order, is_active)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('testimonials', title, content, icon, order, 1))
    
    conn.commit()
    conn.close()
    print("Sample home content added successfully!")

if __name__ == '__main__':
    add_sample_home_content()
