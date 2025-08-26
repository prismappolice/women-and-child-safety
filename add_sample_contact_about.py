import sqlite3

def add_sample_contact_and_about():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Clear existing data
    cursor.execute('DELETE FROM contact_info')
    cursor.execute('DELETE FROM about_content')
    
    # Add sample contact information
    contact_data = [
        ('phone', 'Emergency Helpline', '112', '24/7 Emergency services for immediate assistance'),
        ('phone', 'Women Helpline', '1091', 'Dedicated helpline for women in distress'),
        ('phone', 'Child Helpline', '1098', 'Support for child-related emergencies'),
        ('email', 'General Info', 'info@apwomensafety.gov.in', 'General inquiries and information'),
        ('email', 'Complaints', 'complaints@apwomensafety.gov.in', 'File complaints and grievances'),
        ('address', 'Main Office', 'AP Police Headquarters, Hyderabad', 'Main office address'),
        ('office', 'Regional Office', 'Women & Child Safety Wing Office, Sector 1, Vijayawada - 520001', 'Regional office location')
    ]
    
    for contact_type, title, value, description in contact_data:
        cursor.execute('''
            INSERT INTO contact_info (contact_type, title, value, description)
            VALUES (?, ?, ?, ?)
        ''', (contact_type, title, value, description))
    
    # Add sample about content
    about_data = [
        ('vision', 'Our Vision', 'To create a safe and secure environment for women and children in Andhra Pradesh, ensuring their dignity, safety, and empowerment through proactive policing and community engagement.'),
        ('mission', 'Our Mission', 'We are committed to preventing crimes against women and children, providing swift justice, and creating awareness about safety measures through education and community outreach programs.'),
        ('officers', 'Leadership Team', 'Our dedicated team of experienced officers works tirelessly to ensure the safety and security of women and children across Andhra Pradesh.'),
        ('success_stories', 'Success Stories', 'Over the past year, we have successfully handled over 10,000 cases, provided assistance to thousands of women, and conducted numerous awareness programs across the state.')
    ]
    
    for section_name, title, content in about_data:
        cursor.execute('''
            INSERT INTO about_content (section_name, title, content)
            VALUES (?, ?, ?)
        ''', (section_name, title, content))
    
    conn.commit()
    conn.close()
    print("Sample contact and about content added successfully!")

if __name__ == '__main__':
    add_sample_contact_and_about()
