# EMAIL SYSTEM CONFIGURATION GUIDE
# AP Women Safety Website - Email Notification System

## Overview
The email system has been successfully implemented with the following features:
- Automatic scoring of volunteer applications
- Email notifications to volunteers based on their scores
- Admin notifications for new applications
- Email management dashboard
- Reply system for admins

## Features Implemented

### 1. Automatic Scoring System
- **Age Score (0-25 points)**: Based on age ranges with preference for younger volunteers
- **Education Score (0-25 points)**: Higher scores for advanced education
- **Motivation Score (0-25 points)**: Analysis of motivation text quality and keywords
- **Skills Score (0-25 points)**: Relevance of skills to women safety work

### 2. Email Notifications
- **High Priority (75+ score)**: Immediate priority processing email
- **Medium Priority (50-74 score)**: Standard review process email
- **Needs Review (<50 score)**: Additional information required email
- **Admin Notifications**: Automatic alerts to admin with score breakdown

### 3. Admin Dashboard Features
- Volunteer list sorted by score (highest first)
- Score badges (High/Medium/Low/Not Scored)
- Status management (Pending/High Priority/Approved/Rejected/Contacted)
- Email history tracking
- Direct email communication from admin panel
- Admin notes system

## Email Configuration

### SMTP Settings (Currently in app.py)
```python
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'womensafety@appolice.gov.in'  # Replace with real email
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with real password
app.config['MAIL_DEFAULT_SENDER'] = 'womensafety@appolice.gov.in'
```

### How to Configure Real Email:

1. **For Gmail:**
   - Enable 2-factor authentication
   - Generate an App Password
   - Use the App Password instead of regular password

2. **For Official Government Email:**
   - Contact your IT department for SMTP settings
   - Usually uses different server settings than Gmail

3. **Update Configuration:**
   ```python
   app.config['MAIL_USERNAME'] = 'your-real-email@appolice.gov.in'
   app.config['MAIL_PASSWORD'] = 'your-app-password-or-real-password'
   ```

## Database Tables Added

### 1. email_notifications
Tracks all emails sent to volunteers and admins.

### 2. volunteer_scores  
Stores automatic scoring results for each volunteer.

### 3. admin_settings
For future email configuration settings.

## Scoring Algorithm Details

### Age Scoring:
- 18-25 years: 25 points (ideal age for active volunteering)
- 26-35 years: 20 points
- 36-45 years: 15 points
- 46-55 years: 10 points
- Other ages: 5 points

### Education Scoring:
- PhD/Masters/Post Graduate: 25 points
- Bachelor's Degree: 20 points
- Diploma/12th: 15 points
- 10th/SSC: 10 points
- Others: 5 points

### Motivation Scoring:
- Length bonus (10 points max based on word count)
- Keyword matching (15 points max for relevant terms)
- Keywords: help, support, community, safety, women, service, contribute, volunteer, society, make difference, social, empower, protect

### Skills Scoring:
- 3 points per relevant skill (max 25)
- Relevant skills: communication, counseling, first aid, computer, teaching, social work, psychology, law, legal, management, leadership, public speaking, training, organizing, coordination

## How to Use the System

### 1. Volunteer Registration
- Volunteers fill the form on /volunteer-registration
- System automatically scores the application
- Sends appropriate email based on score
- Notifies admin with score breakdown

### 2. Admin Management
- Login to admin panel
- Go to Volunteers section
- View sorted list by score
- Click "View Details" for full volunteer information
- Send direct emails to volunteers
- Update status and add notes

### 3. Email Templates
The system uses three email templates based on score:
- **High Priority (75+)**: Contact within 2-3 days
- **Medium Priority (50-74)**: Contact within 5-7 days  
- **Needs Review (<50)**: May need additional information

## Testing the System

### To Test Without Real Email:
1. The system is designed to gracefully handle email failures
2. Volunteer registration will work even if email fails
3. Check terminal/console for email error messages

### To Test With Real Email:
1. Update email configuration in app.py
2. Test with a real volunteer registration
3. Check admin panel for scoring results
4. Verify emails are received

## Security Considerations

1. **Email Credentials**: Store in environment variables, not in code
2. **Rate Limiting**: Consider adding rate limiting for email sending
3. **Email Validation**: Current system validates email format
4. **Spam Prevention**: Monitor email sending rates

## Future Enhancements

1. **Email Templates**: Move to separate template files
2. **Bulk Email**: System for sending bulk communications
3. **Email Analytics**: Track email open rates and responses
4. **Automated Follow-ups**: Send follow-up emails based on status
5. **WhatsApp Integration**: Add WhatsApp notifications alongside email

## Troubleshooting

### Common Issues:
1. **Email not sending**: Check SMTP credentials and internet connection
2. **Database errors**: Ensure all tables are created (run init_db())
3. **Template errors**: Check that admin_volunteer_detail.html exists
4. **Score calculation errors**: Check volunteer form field names match database

### Error Checking:
- Check Flask console for error messages
- Verify database has all required tables
- Test email configuration with a simple email first

## Current Status
✅ Email system fully implemented
✅ Automatic scoring working
✅ Admin dashboard with email features
✅ Database tables created
✅ Templates updated
✅ Error handling implemented

The system is ready for production use once real email credentials are configured.
