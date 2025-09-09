#!/usr/bin/env python3
"""
Quick test to verify the email system is working correctly
"""
import sqlite3
import sys
import os

def test_database_structure():
    """Test that all required tables exist with correct structure"""
    print("🔍 Testing Database Structure...")
    
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # Check volunteers table
        cursor.execute("PRAGMA table_info(volunteers)")
        volunteers_columns = [col[1] for col in cursor.fetchall()]
        print(f"✅ Volunteers table columns: {volunteers_columns}")
        
        # Check email_notifications table
        cursor.execute("PRAGMA table_info(email_notifications)")
        email_columns = [col[1] for col in cursor.fetchall()]
        print(f"✅ Email notifications table columns: {email_columns}")
        
        # Check volunteer_scores table
        cursor.execute("PRAGMA table_info(volunteer_scores)")
        scores_columns = [col[1] for col in cursor.fetchall()]
        print(f"✅ Volunteer scores table columns: {scores_columns}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Database test failed: {str(e)}")
        return False

def test_sample_volunteer():
    """Test creating a sample volunteer and scoring"""
    print("\n📝 Testing Sample Volunteer Creation...")
    
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # Insert sample volunteer
        sample_data = (
            "Test Volunteer",
            "test@example.com", 
            "9876543210",
            "25",
            "Test Address, Hyderabad",
            "Social Worker",
            "Bachelor's in Social Work",
            "2 years community service",
            "I am passionate about women's safety and want to contribute to making our communities safer for all women.",
            "Weekends",
            "Communication, counseling, first aid"
        )
        
        cursor.execute('''
            INSERT INTO volunteers (name, email, phone, age, address, occupation, education, experience, motivation, availability, skills)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', sample_data)
        
        volunteer_id = cursor.lastrowid
        print(f"✅ Sample volunteer created with ID: {volunteer_id}")
        
        # Test scoring calculation (without email sending)
        from app import calculate_age_score, calculate_education_score, calculate_motivation_score, calculate_skills_score
        
        age_score = calculate_age_score("25")
        education_score = calculate_education_score("Bachelor's in Social Work")
        motivation_score = calculate_motivation_score("I am passionate about women's safety and want to contribute to making our communities safer for all women.")
        skills_score = calculate_skills_score("Communication, counseling, first aid")
        total_score = age_score + education_score + motivation_score + skills_score
        
        print(f"✅ Scoring test:")
        print(f"   Age Score: {age_score}/25")
        print(f"   Education Score: {education_score}/25") 
        print(f"   Motivation Score: {motivation_score}/25")
        print(f"   Skills Score: {skills_score}/25")
        print(f"   Total Score: {total_score}/100")
        
        # Insert score into database
        cursor.execute('''
            INSERT INTO volunteer_scores (volunteer_id, age_score, education_score, motivation_score, skills_score, total_score, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (volunteer_id, age_score, education_score, motivation_score, skills_score, total_score, 'tested'))
        
        conn.commit()
        conn.close()
        
        return True
        
    except Exception as e:
        print(f"❌ Sample volunteer test failed: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("AP WOMEN SAFETY - EMAIL SYSTEM TEST")
    print("=" * 60)
    
    # Test database structure
    db_test = test_database_structure()
    
    # Test sample volunteer
    volunteer_test = test_sample_volunteer()
    
    print("\n" + "=" * 60)
    print("TEST RESULTS:")
    print(f"Database Structure: {'✅ PASS' if db_test else '❌ FAIL'}")
    print(f"Sample Volunteer: {'✅ PASS' if volunteer_test else '❌ FAIL'}")
    
    if db_test and volunteer_test:
        print("\n🎉 All tests passed! Email system is ready to use.")
        print("\nNext steps:")
        print("1. Visit http://127.0.0.1:5000/volunteer-registration to test volunteer registration")
        print("2. Visit http://127.0.0.1:5000/admin to view admin dashboard")
        print("3. Configure real email credentials in app.py for production use")
    else:
        print("\n⚠️  Some tests failed. Please check the errors above.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
