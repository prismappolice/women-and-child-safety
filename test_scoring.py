#!/usr/bin/env python3
"""
Test script for the volunteer scoring algorithm
Run this to test how the scoring system works with sample data
"""
import re

def calculate_age_score(age_str):
    """Calculate score based on age (0-25 points)"""
    try:
        age = int(age_str)
        if 18 <= age <= 25:
            return 25
        elif 26 <= age <= 35:
            return 20
        elif 36 <= age <= 45:
            return 15
        elif 46 <= age <= 55:
            return 10
        else:
            return 5
    except:
        return 0

def calculate_education_score(education):
    """Calculate score based on education level (0-25 points)"""
    education = education.lower()
    if any(word in education for word in ['phd', 'doctorate', 'post graduate', 'masters', 'mba']):
        return 25
    elif any(word in education for word in ['graduate', 'bachelor', 'degree', 'b.tech', 'b.sc', 'b.com']):
        return 20
    elif any(word in education for word in ['diploma', 'intermediate', '12th', 'plus two']):
        return 15
    elif any(word in education for word in ['10th', 'ssc', 'high school']):
        return 10
    else:
        return 5

def calculate_motivation_score(motivation):
    """Calculate score based on motivation quality (0-25 points)"""
    if not motivation:
        return 0
    
    motivation = motivation.lower()
    positive_keywords = ['help', 'support', 'community', 'safety', 'women', 'service', 'contribute', 
                        'volunteer', 'society', 'make difference', 'social', 'empower', 'protect']
    
    word_count = len(motivation.split())
    keyword_matches = sum(1 for keyword in positive_keywords if keyword in motivation)
    
    score = 0
    # Length bonus (up to 10 points)
    if word_count >= 50:
        score += 10
    elif word_count >= 30:
        score += 8
    elif word_count >= 20:
        score += 6
    elif word_count >= 10:
        score += 4
    
    # Keyword matches (up to 15 points)
    score += min(keyword_matches * 2, 15)
    
    return min(score, 25)

def calculate_skills_score(skills):
    """Calculate score based on relevant skills (0-25 points)"""
    if not skills:
        return 0
    
    skills = skills.lower()
    relevant_skills = ['communication', 'counseling', 'first aid', 'computer', 'teaching', 
                      'social work', 'psychology', 'law', 'legal', 'management', 'leadership',
                      'public speaking', 'training', 'organizing', 'coordination']
    
    matches = sum(1 for skill in relevant_skills if skill in skills)
    return min(matches * 3, 25)

def test_scoring_system():
    print("=" * 60)
    print("VOLUNTEER SCORING SYSTEM TEST")
    print("=" * 60)
    
    # Test cases
    test_volunteers = [
        {
            "name": "High Priority Candidate",
            "age": "22",
            "education": "Bachelor's Degree in Social Work",
            "motivation": "I am deeply passionate about women's safety and empowerment. Having grown up in a community where I witnessed the challenges women face, I feel a strong calling to contribute to their protection and support. I believe that every woman deserves to feel safe and secure, and I want to use my skills in communication and community organizing to make a meaningful difference. I am committed to volunteering my time and energy to help create safer spaces for women and to support those who need assistance.",
            "skills": "Communication, counseling, first aid, public speaking, social work experience"
        },
        {
            "name": "Medium Priority Candidate", 
            "age": "35",
            "education": "12th pass",
            "motivation": "I want to help women in my community. Safety is important and I can contribute.",
            "skills": "Basic computer skills, teaching"
        },
        {
            "name": "Needs Review Candidate",
            "age": "60", 
            "education": "10th pass",
            "motivation": "I want to volunteer",
            "skills": "Cooking"
        }
    ]
    
    for i, volunteer in enumerate(test_volunteers, 1):
        print(f"\n{i}. Testing: {volunteer['name']}")
        print("-" * 40)
        
        age_score = calculate_age_score(volunteer['age'])
        education_score = calculate_education_score(volunteer['education'])
        motivation_score = calculate_motivation_score(volunteer['motivation'])
        skills_score = calculate_skills_score(volunteer['skills'])
        total_score = age_score + education_score + motivation_score + skills_score
        
        print(f"Age ({volunteer['age']}): {age_score}/25")
        print(f"Education: {education_score}/25")
        print(f"Motivation: {motivation_score}/25")
        print(f"Skills: {skills_score}/25")
        print(f"TOTAL SCORE: {total_score}/100")
        
        # Determine priority
        if total_score >= 75:
            priority = "HIGH PRIORITY"
            action = "Contact within 2-3 days"
        elif total_score >= 50:
            priority = "MEDIUM PRIORITY"  
            action = "Contact within 5-7 days"
        else:
            priority = "NEEDS REVIEW"
            action = "May need additional information"
            
        print(f"Priority: {priority}")
        print(f"Action: {action}")
        print()

if __name__ == "__main__":
    try:
        test_scoring_system()
        print("✅ Scoring system test completed successfully!")
    except Exception as e:
        print(f"❌ Error testing scoring system: {str(e)}")
