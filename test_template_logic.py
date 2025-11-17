#!/usr/bin/env python3

def test_template_logic():
    """Test the template logic for different volunteer statuses"""
    
    # Simulate volunteer data with different statuses
    test_volunteers = [
        ['id', 'name', 'email', 'phone', 'age', 'address', 'education', 'occupation', 
         'motivation', 'skills', 'created_at', 'age_score', 'education_score', 
         'motivation_score', 'skills_score', 'total_score', 'approved'],  # index 16 = approved
        
        ['id', 'name', 'email', 'phone', 'age', 'address', 'education', 'occupation', 
         'motivation', 'skills', 'created_at', 'age_score', 'education_score', 
         'motivation_score', 'skills_score', 'total_score', 'accepted'],  # index 16 = accepted
         
        ['id', 'name', 'email', 'phone', 'age', 'address', 'education', 'occupation', 
         'motivation', 'skills', 'created_at', 'age_score', 'education_score', 
         'motivation_score', 'skills_score', 'total_score', 'rejected'],  # index 16 = rejected
         
        ['id', 'name', 'email', 'phone', 'age', 'address', 'education', 'occupation', 
         'motivation', 'skills', 'created_at', 'age_score', 'education_score', 
         'motivation_score', 'skills_score', 'total_score', 'pending'],   # index 16 = pending
         
        ['id', 'name', 'email', 'phone', 'age', 'address', 'education', 'occupation', 
         'motivation', 'skills', 'created_at', 'age_score', 'education_score', 
         'motivation_score', 'skills_score', 'total_score', None]         # index 16 = None
    ]
    
    print("=== Template Logic Test ===")
    
    for i, volunteer in enumerate(test_volunteers):
        status = volunteer[16]
        
        # Badge logic test
        if status:
            badge_class = 'approved' if status in ['approved', 'accepted'] else ('rejected' if status == 'rejected' else 'pending')
            if status in ['approved', 'accepted']:
                badge_text = 'Accepted'
            elif status == 'rejected':
                badge_text = 'Rejected'
            elif status == 'high_priority':
                badge_text = 'On Hold'
            else:
                badge_text = status.title()
        else:
            badge_class = 'pending'
            badge_text = 'Pending'
        
        # Action buttons logic test
        show_action_buttons = status not in ['approved', 'accepted', 'rejected']
        
        print(f"Volunteer {i+1}: Status = {status}")
        print(f"  Badge: class='status-{badge_class}', text='{badge_text}'")
        print(f"  Action Buttons: {'SHOW' if show_action_buttons else 'HIDE'}")
        print()
    
    print("=== Test Complete ===")

if __name__ == "__main__":
    test_template_logic()