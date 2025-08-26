# AP Police Women & Child Safety Wing Website

A comprehensive web application for the Andhra Pradesh Police Women & Child Safety Wing, providing information about initiatives, safety tips, volunteer registration, and admin management capabilities.

## Features

### Public Pages
- **Home Page**: Welcome page with navigation and emergency contacts
- **About Us**: Information about the organization and mission
- **Initiatives**: Details about various women safety programs
- **Safety Tips**: Comprehensive safety guidelines for women
- **Volunteer Registration**: Form for community volunteers to register
- **Contact Us**: Office locations and emergency contact information
- **Media & Events**: Gallery of events and activities
- **PDF Resources**: Downloadable safety resources and documents

### Interactive Features
- **Chatbot**: AI-powered assistance on all pages (except admin login)
- **Emergency Numbers**: Quick access to helpline numbers
- **Responsive Design**: Mobile-friendly interface
- **Beautiful UI**: Professional gradient design with consistent branding

### Admin Panel
- **Secure Login**: Admin authentication system
- **Dashboard**: Overview of volunteer registrations and statistics
- **Content Management**: Future expansion for dynamic content

## Technology Stack
- **Backend**: Flask (Python web framework)
- **Database**: SQLite for data storage
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Font Awesome icons
- **Chatbot**: Custom JavaScript implementation

## Installation & Setup

1. **Clone/Download the project**
   ```
   Navigate to project directory: d:\new ap women safety
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the Website**
   - Public Site: http://127.0.0.1:5000
   - Admin Login: http://127.0.0.1:5000/admin-login
   - Admin Credentials: Username: `admin`, Password: `admin123`

## Project Structure
```
d:\new ap women safety/
├── app.py                 # Main Flask application
├── women_safety.db        # SQLite database
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── static/               # Static files
│   ├── chatbot.css       # Chatbot styling
│   ├── chatbot.js        # Chatbot functionality
│   ├── images/           # Image files
│   ├── uploads/          # File uploads
│   └── pdfs/             # PDF resources
└── templates/            # HTML templates
    ├── index.html        # Home page
    ├── about.html        # About page
    ├── initiatives.html  # Initiatives page
    ├── safety_tips.html  # Safety tips page
    ├── volunteer_registration.html # Volunteer form
    ├── contact.html      # Contact page
    ├── gallery.html      # Media & events
    ├── pdf_resources.html # PDF resources
    ├── admin_login.html  # Admin login
    └── admin_dashboard.html # Admin dashboard
```

## Database Schema

### Volunteers Table
- id (PRIMARY KEY)
- name, email, phone, age
- address, occupation, education
- experience, motivation, availability, skills
- created_at (timestamp)

## Key Features

### Chatbot System
- Floating chat widget on all pages
- Emergency number integration
- Smart responses for common queries
- Professional blue gradient design

### Security
- Session-based admin authentication
- Input validation and sanitization
- Secure file upload handling

### Responsive Design
- Mobile-first approach
- Cross-browser compatibility
- Professional gradient color scheme

## Admin Functionality
- Secure login system
- Volunteer management dashboard
- Registration statistics
- Future expansion ready for content management

## Future Enhancements
- Dynamic content management system
- Advanced reporting and analytics
- Multi-language support
- Enhanced chatbot with AI integration
- File upload and management system

## Support
For technical support or questions, contact the development team.

---
© 2024 AP Police Women & Child Safety Wing. All rights reserved.