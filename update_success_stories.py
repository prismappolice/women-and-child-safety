import sqlite3
from datetime import datetime

def add_enhanced_success_stories():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Enhanced success stories with statistics
    success_stories = [
        {
            'title': 'SHE Teams Rescue Operation in Visakhapatnam',
            'description': 'A 24-year-old IT professional was being stalked near her workplace in Visakhapatnam. She contacted SHE Teams through the mobile app. Within 15 minutes, our team arrived at the location and apprehended the stalker. The victim was provided immediate counseling support and legal guidance. The perpetrator was counseled and warned, and the case was resolved without further incidents.',
            'date': 'December 2024',
            'stat1_number': '15',
            'stat1_label': 'Minutes Response Time',
            'stat2_number': '100%',
            'stat2_label': 'Case Resolution',
            'stat3_number': '1',
            'stat3_label': 'Life Protected',
            'image_url': '/static/images/success-visakha.jpg',
            'sort_order': 1
        },
        {
            'title': 'Domestic Violence Prevention in Guntur',
            'description': 'A housewife from Guntur district contacted our helpline 181 regarding continuous domestic violence. Our trained counselors provided immediate emotional support and connected her with legal aid services. Through proper mediation and family counseling sessions, the domestic violence was stopped. The family is now living peacefully with regular follow-up support.',
            'date': 'November 2024',
            'stat1_number': '24/7',
            'stat1_label': 'Helpline Support',
            'stat2_number': '3',
            'stat2_label': 'Counseling Sessions',
            'stat3_number': '95%',
            'stat3_label': 'Success Rate',
            'image_url': '/static/images/success-guntur.jpg',
            'sort_order': 2
        },
        {
            'title': 'Cyber Crime Prevention in Hyderabad',
            'description': 'A college student from Hyderabad was being blackmailed through social media with morphed photos. She approached the Cyber Crime Wing through the women safety portal. Our cyber experts traced the perpetrator within 48 hours and recovered all compromised content. The blackmailer was arrested and the victim received psychological counseling support.',
            'date': 'January 2025',
            'stat1_number': '48',
            'stat1_label': 'Hours to Trace',
            'stat2_number': '100%',
            'stat2_label': 'Content Recovered',
            'stat3_number': '1',
            'stat3_label': 'Arrest Made',
            'image_url': '/static/images/success-cyber.jpg',
            'sort_order': 3
        },
        {
            'title': 'Workplace Harassment Resolution in Vijayawada',
            'description': 'A software engineer working in Vijayawada reported workplace sexual harassment through our online complaint system. Our team immediately coordinated with the company\'s Internal Complaints Committee (ICC). The harassment was investigated thoroughly, and appropriate action was taken against the perpetrator. The victim received legal support and counseling throughout the process.',
            'date': 'October 2024',
            'stat1_number': '7',
            'stat1_label': 'Days Resolution',
            'stat2_number': '100%',
            'stat2_label': 'Justice Served',
            'stat3_number': '1',
            'stat3_label': 'Career Protected',
            'image_url': '/static/images/success-workplace.jpg',
            'sort_order': 4
        },
        {
            'title': 'Public Transport Safety Initiative Success',
            'description': 'During a routine patrol by SHE Teams in RTC buses across Amaravati, our team prevented a potential molestation incident. The victim, a college student, was immediately assisted and the perpetrator was apprehended. This incident led to enhanced security measures in public transport and awareness campaigns for passengers.',
            'date': 'September 2024',
            'stat1_number': '500+',
            'stat1_label': 'Daily Bus Patrols',
            'stat2_number': '30%',
            'stat2_label': 'Crime Reduction',
            'stat3_number': '24/7',
            'stat3_label': 'Monitoring',
            'image_url': '/static/images/success-transport.jpg',
            'sort_order': 5
        },
        {
            'title': 'Rural Area Women Empowerment in Anantapur',
            'description': 'Women from remote villages in Anantapur district were being denied their basic rights and facing discrimination. Through our outreach programs and legal awareness camps, we educated the community about women\'s rights. Local women were trained as legal volunteers and now serve as first responders for women in distress in their villages.',
            'date': 'August 2024',
            'stat1_number': '50',
            'stat1_label': 'Villages Covered',
            'stat2_number': '200+',
            'stat2_label': 'Women Trained',
            'stat3_number': '80%',
            'stat3_label': 'Awareness Increase',
            'image_url': '/static/images/success-rural.jpg',
            'sort_order': 6
        }
    ]
    
    # Clear existing success stories and add new ones
    print("Adding enhanced success stories to database...")
    
    for i, story in enumerate(success_stories, 1):
        cursor.execute('''
            INSERT OR REPLACE INTO success_stories 
            (id, title, description, date, stat1_number, stat1_label, 
             stat2_number, stat2_label, stat3_number, stat3_label, 
             image_url, sort_order, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
        ''', (i, story['title'], story['description'], story['date'],
              story['stat1_number'], story['stat1_label'],
              story['stat2_number'], story['stat2_label'],
              story['stat3_number'], story['stat3_label'],
              story['image_url'], story['sort_order']))
        
        print(f"Added: {story['title']}")
    
    conn.commit()
    
    # Display current success stories
    cursor.execute('SELECT id, title, date, sort_order FROM success_stories ORDER BY sort_order')
    stories = cursor.fetchall()
    
    print(f"\nTotal success stories in database: {len(stories)}")
    print("\nCurrent Success Stories:")
    for story in stories:
        print(f"{story[0]}. {story[1]} ({story[2]}) - Sort Order: {story[3]}")
    
    conn.close()
    print("\nSuccess stories database updated successfully!")
    print("\nNow you can:")
    print("1. Visit http://127.0.0.1:5000/admin/success-stories to manage stories")
    print("2. View the stories on http://127.0.0.1:5000/about")
    print("3. Add new stories or edit existing ones through admin panel")

if __name__ == "__main__":
    add_enhanced_success_stories()
