from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import sqlite3
import os
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Database initialization
def init_db():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Create volunteers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            age TEXT,
            address TEXT NOT NULL,
            occupation TEXT,
            education TEXT,
            experience TEXT,
            motivation TEXT,
            availability TEXT,
            skills TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create home_content table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS home_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            section_name TEXT NOT NULL,
            title TEXT NOT NULL,
            content TEXT,
            image_url TEXT,
            link_url TEXT,
            icon_class TEXT,
            sort_order INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create contact_info table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            value TEXT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create pdf_resources table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pdf_resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            file_name TEXT NOT NULL,
            file_path TEXT NOT NULL,
            icon TEXT,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create about_content table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS about_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            section_type TEXT NOT NULL,
            title TEXT NOT NULL,
            content TEXT,
            image_url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create initiatives table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS initiatives (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            location TEXT,
            date TEXT,
            image_path TEXT,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create safety_tips table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS safety_tips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database when app starts
init_db()

@app.route('/')
def home():
    # Get dynamic home page content
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active FROM home_content WHERE is_active = 1 ORDER BY section_name, sort_order')
    home_content = cursor.fetchall()
    conn.close()
    
    return render_template('index.html', home_content=home_content)

@app.route('/about')
def about():
    # Get dynamic about page content
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, section_name, title, content, image_url, sort_order, is_active FROM about_content WHERE is_active = 1 ORDER BY sort_order, section_name')
    about_sections = cursor.fetchall()
    conn.close()
    
    return render_template('about.html', about_sections=about_sections)

@app.route('/initiatives')
def initiatives():
    # Get dynamic initiatives from database
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, description, image_url, is_featured FROM initiatives WHERE is_active = 1 ORDER BY is_featured DESC, id')
    initiatives_data = cursor.fetchall()
    conn.close()
    
    return render_template('initiatives.html', initiatives_data=initiatives_data)

@app.route('/volunteer-registration', methods=['GET', 'POST'])
def volunteer_registration():
    if request.method == 'POST':
        # Handle form submission
        full_name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        district = request.form.get('district', 'Not Specified')
        occupation = request.form.get('occupation')
        education = request.form.get('education')
        interests = request.form.get('interests')
        
        # Store in database
        try:
            conn = sqlite3.connect('women_safety.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO volunteers (full_name, email, phone, district, occupation, education, interests, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'pending')
            ''', (full_name, email, phone, district, occupation, education, interests))
            conn.commit()
            conn.close()
            
            flash('Thank you for registering as a volunteer! We will contact you soon.', 'success')
            return redirect(url_for('volunteer_registration'))
        except Exception as e:
            flash('An error occurred. Please try again.', 'error')
            return redirect(url_for('volunteer_registration'))
    
    return render_template('volunteer_registration.html')

@app.route('/safety-tips')
def safety_tips():
    # Get dynamic safety tips from database
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Get safety tips
    cursor.execute('SELECT title, icon, tips FROM safety_tips WHERE is_active = 1 ORDER BY id')
    tips_data = cursor.fetchall()
    
    # Get emergency numbers
    cursor.execute('SELECT number, label FROM emergency_numbers WHERE is_active = 1 ORDER BY sort_order')
    emergency_numbers = cursor.fetchall()
    
    conn.close()
    
    return render_template('safety_tips.html', tips_data=tips_data, emergency_numbers=emergency_numbers)

@app.route('/pdf-resources')
def pdf_resources():
    # Get dynamic PDF resources from database
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, description, file_path, icon FROM pdf_resources WHERE is_active = 1 ORDER BY id')
    pdf_data = cursor.fetchall()
    conn.close()
    
    return render_template('pdf_resources.html', pdf_data=pdf_data)

@app.route('/contact')
def contact():
    # Get dynamic contact information
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, contact_type, value, description FROM contact_info ORDER BY contact_type')
    contact_info = cursor.fetchall()
    conn.close()
    
    return render_template('contact.html', contact_info=contact_info)

@app.route('/gallery')
def gallery():
    # Get dynamic gallery items
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, description, image_url, event_date, category, is_featured FROM gallery_items WHERE is_active = 1 ORDER BY is_featured DESC, event_date DESC')
    gallery_items = cursor.fetchall()
    conn.close()
    
    return render_template('gallery.html', gallery_items=gallery_items)

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Simple admin check (replace with proper authentication)
        if username == 'admin' and password == 'admin123':
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials', 'error')
    
    return render_template('admin_login.html')

@app.route('/admin-dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    # Get statistics for dashboard
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Count volunteers
    cursor.execute('SELECT COUNT(*) FROM volunteers')
    volunteer_count = cursor.fetchone()[0]
    
    # Count active safety tips
    cursor.execute('SELECT COUNT(*) FROM safety_tips WHERE is_active = 1')
    tips_count = cursor.fetchone()[0]
    
    # Count active PDF resources
    cursor.execute('SELECT COUNT(*) FROM pdf_resources WHERE is_active = 1')
    pdf_count = cursor.fetchone()[0]
    
    # Count active initiatives
    cursor.execute('SELECT COUNT(*) FROM initiatives WHERE is_active = 1')
    initiatives_count = cursor.fetchone()[0]
    
    # Get recent volunteers
    cursor.execute('SELECT full_name, email, phone, registration_date FROM volunteers ORDER BY registration_date DESC LIMIT 5')
    recent_volunteers = cursor.fetchall()
    
    conn.close()
    
    stats = {
        'volunteers': volunteer_count,
        'tips': tips_count,
        'pdfs': pdf_count,
        'initiatives': initiatives_count
    }
    
    return render_template('admin_dashboard.html', stats=stats, recent_volunteers=recent_volunteers)

# Admin Safety Tips Management
@app.route('/admin-safety-tips')
def admin_safety_tips():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, category, title, icon, tips, is_active FROM safety_tips ORDER BY id')
    tips = cursor.fetchall()
    conn.close()
    
    return render_template('admin_safety_tips.html', tips=tips)

@app.route('/admin-safety-tips/add', methods=['GET', 'POST'])
def admin_add_safety_tip():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        category = request.form.get('category')
        title = request.form.get('title')
        icon = request.form.get('icon')
        tips = request.form.get('tips')
        
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO safety_tips (category, title, icon, tips)
            VALUES (?, ?, ?, ?)
        ''', (category, title, icon, tips))
        conn.commit()
        conn.close()
        
        flash('Safety tip added successfully!', 'success')
        return redirect(url_for('admin_safety_tips'))
    
    return render_template('admin_add_safety_tip.html')

@app.route('/admin-safety-tips/edit/<int:tip_id>', methods=['GET', 'POST'])
def admin_edit_safety_tip(tip_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        category = request.form.get('category')
        title = request.form.get('title')
        icon = request.form.get('icon')
        tips = request.form.get('tips')
        is_active = 1 if request.form.get('is_active') else 0
        
        cursor.execute('''
            UPDATE safety_tips 
            SET category=?, title=?, icon=?, tips=?, is_active=?, updated_at=?
            WHERE id=?
        ''', (category, title, icon, tips, is_active, datetime.now(), tip_id))
        conn.commit()
        conn.close()
        
        flash('Safety tip updated successfully!', 'success')
        return redirect(url_for('admin_safety_tips'))
    
    cursor.execute('SELECT * FROM safety_tips WHERE id=?', (tip_id,))
    tip = cursor.fetchone()
    conn.close()
    
    return render_template('admin_edit_safety_tip.html', tip=tip)

@app.route('/admin-safety-tips/delete/<int:tip_id>')
def admin_delete_safety_tip(tip_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM safety_tips WHERE id=?', (tip_id,))
    conn.commit()
    conn.close()
    
    flash('Safety tip deleted successfully!', 'success')
    return redirect(url_for('admin_safety_tips'))

# Admin PDF Resources Management
@app.route('/admin-pdf-resources')
def admin_pdf_resources():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, description, file_name, icon, is_active FROM pdf_resources ORDER BY id')
    pdfs = cursor.fetchall()
    conn.close()
    
    return render_template('admin_pdf_resources.html', pdfs=pdfs)

@app.route('/admin-pdf-resources/add', methods=['GET', 'POST'])
def admin_add_pdf_resource():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        icon = request.form.get('icon')
        
        # Handle file upload
        if 'pdf_file' in request.files:
            file = request.files['pdf_file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join('static/pdfs', filename)
                
                # Create pdfs directory if it doesn't exist
                if not os.path.exists('static/pdfs'):
                    os.makedirs('static/pdfs')
                
                file.save(file_path)
                
                conn = sqlite3.connect('women_safety.db')
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO pdf_resources (title, description, file_name, file_path, icon)
                    VALUES (?, ?, ?, ?, ?)
                ''', (title, description, filename, f'/static/pdfs/{filename}', icon))
                conn.commit()
                conn.close()
                
                flash('PDF resource added successfully!', 'success')
                return redirect(url_for('admin_pdf_resources'))
    
    return render_template('admin_add_pdf_resource.html')

@app.route('/admin/pdf-resources/edit/<int:pdf_id>', methods=['GET', 'POST'])
def admin_edit_pdf_resource(pdf_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        icon = request.form.get('icon')
        is_active = 1 if request.form.get('is_active') else 0
        
        # Handle file upload if new file is provided
        if 'pdf_file' in request.files:
            file = request.files['pdf_file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join('static/pdfs', filename)
                
                # Create pdfs directory if it doesn't exist
                if not os.path.exists('static/pdfs'):
                    os.makedirs('static/pdfs')
                
                file.save(file_path)
                
                cursor.execute('''
                    UPDATE pdf_resources 
                    SET title = ?, description = ?, file_name = ?, file_path = ?, icon = ?, is_active = ?
                    WHERE id = ?
                ''', (title, description, filename, f'/static/pdfs/{filename}', icon, is_active, pdf_id))
            else:
                # Update without changing file
                cursor.execute('''
                    UPDATE pdf_resources 
                    SET title = ?, description = ?, icon = ?, is_active = ?
                    WHERE id = ?
                ''', (title, description, icon, is_active, pdf_id))
        else:
            # Update without changing file
            cursor.execute('''
                UPDATE pdf_resources 
                SET title = ?, description = ?, icon = ?, is_active = ?
                WHERE id = ?
            ''', (title, description, icon, is_active, pdf_id))
        
        conn.commit()
        conn.close()
        
        flash('PDF resource updated successfully!', 'success')
        return redirect(url_for('admin_pdf_resources'))
    
    # GET request - fetch PDF data
    cursor.execute('SELECT id, title, description, file_name, icon, is_active FROM pdf_resources WHERE id = ?', (pdf_id,))
    pdf_resource = cursor.fetchone()
    conn.close()
    
    if not pdf_resource:
        flash('PDF resource not found!', 'error')
        return redirect(url_for('admin_pdf_resources'))
    
    return render_template('admin_edit_pdf_resource.html', pdf_resource=pdf_resource)

@app.route('/admin/pdf-resources/delete/<int:pdf_id>', methods=['POST'])
def admin_delete_pdf_resource(pdf_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Get file path before deleting record
    cursor.execute('SELECT file_path FROM pdf_resources WHERE id = ?', (pdf_id,))
    result = cursor.fetchone()
    
    if result:
        file_path = result[0]
        # Delete the file from filesystem
        full_path = f"static/pdfs/{file_path.split('/')[-1]}"
        if os.path.exists(full_path):
            os.remove(full_path)
    
    cursor.execute('DELETE FROM pdf_resources WHERE id = ?', (pdf_id,))
    conn.commit()
    conn.close()
    
    flash('PDF resource deleted successfully!', 'success')
    return redirect(url_for('admin_pdf_resources'))

# Admin Initiatives Management  
@app.route('/admin/initiatives')
def admin_initiatives():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, description, image_url, is_featured, is_active FROM initiatives ORDER BY id')
    initiatives = cursor.fetchall()
    conn.close()
    
    return render_template('admin_initiatives.html', initiatives=initiatives)

@app.route('/admin/initiatives/add', methods=['GET', 'POST'])
def admin_add_initiative():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        image_url = request.form.get('image_url')
        is_featured = 1 if request.form.get('is_featured') else 0
        
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO initiatives (title, description, image_url, is_featured)
            VALUES (?, ?, ?, ?)
        ''', (title, description, image_url, is_featured))
        conn.commit()
        conn.close()
        
        flash('Initiative added successfully!', 'success')
        return redirect(url_for('admin_initiatives'))

    return render_template('admin_add_initiative.html')

@app.route('/admin/initiatives/edit/<int:initiative_id>', methods=['GET', 'POST'])
def admin_edit_initiative(initiative_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        image_url = request.form.get('image_url')
        is_featured = 1 if request.form.get('is_featured') else 0
        is_active = 1 if request.form.get('is_active') else 0
        
        cursor.execute('''
            UPDATE initiatives 
            SET title = ?, description = ?, image_url = ?, is_featured = ?, is_active = ?
            WHERE id = ?
        ''', (title, description, image_url, is_featured, is_active, initiative_id))
        conn.commit()
        conn.close()
        
        flash('Initiative updated successfully!', 'success')
        return redirect(url_for('admin_initiatives'))
    
    # GET request - fetch initiative data
    cursor.execute('SELECT id, title, description, image_url, is_featured, is_active FROM initiatives WHERE id = ?', (initiative_id,))
    initiative = cursor.fetchone()
    conn.close()
    
    if not initiative:
        flash('Initiative not found!', 'error')
        return redirect(url_for('admin_initiatives'))
    
    return render_template('admin_edit_initiative.html', initiative=initiative)

@app.route('/admin/initiatives/delete/<int:initiative_id>', methods=['POST'])
def admin_delete_initiative(initiative_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM initiatives WHERE id = ?', (initiative_id,))
    conn.commit()
    conn.close()
    
    flash('Initiative deleted successfully!', 'success')
    return redirect(url_for('admin_initiatives'))

# Admin About Page Management
@app.route('/admin/about')
def admin_about():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, section_name, title, content, image_url, sort_order, is_active FROM about_content ORDER BY sort_order, section_name')
    about_sections = cursor.fetchall()
    conn.close()
    
    return render_template('admin_about.html', about_sections=about_sections)

@app.route('/admin/about/add', methods=['GET', 'POST'])
def admin_add_about_section():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        section_name = request.form.get('section_name')
        title = request.form.get('title')
        content = request.form.get('content')
        image_url = request.form.get('image_url')
        sort_order = request.form.get('sort_order', 0)
        
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO about_content (section_name, title, content, image_url, sort_order)
            VALUES (?, ?, ?, ?, ?)
        ''', (section_name, title, content, image_url, sort_order))
        conn.commit()
        conn.close()
        
        flash('About section added successfully!', 'success')
        return redirect(url_for('admin_about'))
    
    return render_template('admin_add_about_section.html')

@app.route('/admin/about/edit/<int:section_id>', methods=['GET', 'POST'])
def admin_edit_about_section(section_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        section_name = request.form.get('section_name')
        title = request.form.get('title')
        content = request.form.get('content')
        image_url = request.form.get('image_url')
        sort_order = request.form.get('sort_order', 0)
        is_active = 1 if request.form.get('is_active') else 0
        
        cursor.execute('''
            UPDATE about_content 
            SET section_name = ?, title = ?, content = ?, image_url = ?, sort_order = ?, is_active = ?
            WHERE id = ?
        ''', (section_name, title, content, image_url, sort_order, is_active, section_id))
        conn.commit()
        conn.close()
        
        flash('About section updated successfully!', 'success')
        return redirect(url_for('admin_about'))
    
    # GET request - fetch section data
    cursor.execute('SELECT id, section_name, title, content, image_url, sort_order, is_active FROM about_content WHERE id = ?', (section_id,))
    section = cursor.fetchone()
    conn.close()
    
    if not section:
        flash('Section not found!', 'error')
        return redirect(url_for('admin_about'))
    
    return render_template('admin_edit_about_section.html', section=section)

@app.route('/admin/about/delete/<int:section_id>', methods=['POST'])
def admin_delete_about_section(section_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM about_content WHERE id = ?', (section_id,))
    conn.commit()
    conn.close()
    
    flash('About section deleted successfully!', 'success')
    return redirect(url_for('admin_about'))

# Admin Home Page Management
@app.route('/admin/home')
def admin_home():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active FROM home_content ORDER BY section_name, sort_order')
    home_content = cursor.fetchall()
    conn.close()
    
    return render_template('admin_home.html', home_content=home_content)

@app.route('/admin/home/edit/<int:content_id>', methods=['GET', 'POST'])
def admin_edit_home_content(content_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        section_name = request.form.get('section_name')
        title = request.form.get('title')
        content = request.form.get('content')
        image_url = request.form.get('image_url')
        link_url = request.form.get('link_url')
        icon_class = request.form.get('icon_class')
        sort_order = request.form.get('sort_order')
        is_active = 1 if request.form.get('is_active') else 0
        
        cursor.execute('''
            UPDATE home_content 
            SET section_name = ?, title = ?, content = ?, image_url = ?, link_url = ?, icon_class = ?, sort_order = ?, is_active = ?
            WHERE id = ?
        ''', (section_name, title, content, image_url, link_url, icon_class, sort_order, is_active, content_id))
        
        conn.commit()
        conn.close()
        
        flash('Home content updated successfully!', 'success')
        return redirect(url_for('admin_home'))
    
    # GET request - fetch content data
    cursor.execute('SELECT id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active FROM home_content WHERE id = ?', (content_id,))
    home_content = cursor.fetchone()
    conn.close()
    
    if not home_content:
        flash('Home content not found!', 'error')
        return redirect(url_for('admin_home'))
    
    return render_template('admin_edit_home_content.html', home_content=home_content)

@app.route('/admin/home/delete/<int:content_id>', methods=['POST'])
def admin_delete_home_content(content_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM home_content WHERE id = ?', (content_id,))
    conn.commit()
    conn.close()
    
    flash('Home content deleted successfully!', 'success')
    return redirect(url_for('admin_home'))

@app.route('/admin/home/add/<section>', methods=['GET', 'POST'])
def admin_add_home_content(section):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        section_name = request.form.get('section_name')
        title = request.form.get('title')
        content = request.form.get('content')
        image_url = request.form.get('image_url')
        sort_order = request.form.get('display_order', 1)
        extra_info = request.form.get('extra_info')
        is_active = request.form.get('is_active') == 'on'
        
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO home_content (section_name, title, content, image_url, link_url, sort_order, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (section_name, title, content, image_url, extra_info, sort_order, is_active))
        conn.commit()
        conn.close()
        
        flash(f'{section.title()} content added successfully!', 'success')
        return redirect(url_for('admin_home'))
    
    return render_template('admin_add_home_content.html', section=section)

# Admin Contact Management
@app.route('/admin/contact')
def admin_contact():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, contact_type, title, value, description, icon_class, is_primary, is_active FROM contact_info ORDER BY contact_type, is_primary DESC')
    contact_info = cursor.fetchall()
    conn.close()
    
    return render_template('admin_contact.html', contact_info=contact_info)

@app.route('/admin/contact/add', methods=['GET', 'POST'])
def admin_add_contact_info():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        contact_type = request.form.get('contact_type')
        title = request.form.get('title')
        value = request.form.get('value')
        description = request.form.get('description')
        is_active = request.form.get('is_active') == 'on'
        
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO contact_info (contact_type, title, value, description, is_active)
            VALUES (?, ?, ?, ?, ?)
        ''', (contact_type, title, value, description, is_active))
        conn.commit()
        conn.close()
        
        flash('Contact information added successfully!', 'success')
        return redirect(url_for('admin_contact'))
    
    return render_template('admin_add_contact_info.html')

@app.route('/admin/contact/office/add', methods=['GET', 'POST'])
def admin_add_office_location():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        address = request.form.get('address')
        is_active = request.form.get('is_active') == 'on'
        
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO contact_info (contact_type, title, value, is_active)
            VALUES ('office', ?, ?, ?)
        ''', (title, address, is_active))
        conn.commit()
        conn.close()
        
        flash('Office location added successfully!', 'success')
        return redirect(url_for('admin_contact'))
    
    return render_template('admin_add_office_location.html')

@app.route('/admin/contact/form/update', methods=['POST'])
def admin_update_contact_form():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    flash('Contact form settings updated successfully!', 'success')
    return redirect(url_for('admin_contact'))

@app.route('/admin/contact/edit/<int:contact_id>', methods=['GET', 'POST'])
def admin_edit_contact_info(contact_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        contact_type = request.form.get('contact_type')
        label = request.form.get('label')
        value = request.form.get('value')
        additional_info = request.form.get('additional_info')
        is_active = 1 if request.form.get('is_active') else 0
        
        cursor.execute('''
            UPDATE contact_info 
            SET contact_type = ?, label = ?, value = ?, additional_info = ?, is_active = ?
            WHERE id = ?
        ''', (contact_type, label, value, additional_info, is_active, contact_id))
        conn.commit()
        conn.close()
        
        flash('Contact information updated successfully!', 'success')
        return redirect(url_for('admin_contact'))
    
    # GET request - fetch contact data
    cursor.execute('SELECT id, contact_type, label, value, additional_info, is_active FROM contact_info WHERE id = ?', (contact_id,))
    contact = cursor.fetchone()
    conn.close()
    
    if not contact:
        flash('Contact information not found!', 'error')
        return redirect(url_for('admin_contact'))
    
    return render_template('admin_edit_contact.html', contact=contact)

@app.route('/admin/contact/delete/<int:contact_id>', methods=['POST'])
def admin_delete_contact_info(contact_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contact_info WHERE id = ?', (contact_id,))
    conn.commit()
    conn.close()
    
    flash('Contact information deleted successfully!', 'success')
    return redirect(url_for('admin_contact'))

# Admin Gallery Management
@app.route('/admin/gallery')
def admin_gallery():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, description, image_url, event_date, category, is_featured, is_active FROM gallery_items ORDER BY event_date DESC')
    gallery_items = cursor.fetchall()
    conn.close()
    
    return render_template('admin_gallery.html', gallery_items=gallery_items)

@app.route('/admin/gallery/add', methods=['GET', 'POST'])
def admin_add_gallery_item():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        image_url = request.form.get('image_url')
        category = request.form.get('category')
        is_active = request.form.get('is_active') == 'on'
        
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO gallery_items (title, description, image_url, category, is_active)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, description, image_url, category, is_active))
        conn.commit()
        conn.close()
        
        flash('Gallery item added successfully!', 'success')
        return redirect(url_for('admin_gallery'))
    
    return render_template('admin_add_gallery_item.html')

@app.route('/admin/volunteers')
def admin_volunteers():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, full_name, email, phone, district, education, occupation, interests, status, registration_date FROM volunteers ORDER BY registration_date DESC')
    volunteers = cursor.fetchall()
    conn.close()
    
    return render_template('admin_volunteers.html', volunteers=volunteers)

@app.route('/admin/volunteers/update/<int:volunteer_id>', methods=['POST'])
def admin_update_volunteer_status(volunteer_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    status = request.form.get('status')
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE volunteers SET status = ? WHERE id = ?', (status, volunteer_id))
    conn.commit()
    conn.close()
    
    flash('Volunteer status updated successfully!', 'success')
    return redirect(url_for('admin_volunteers'))

@app.route('/admin/volunteers/delete/<int:volunteer_id>', methods=['POST'])
def admin_delete_volunteer(volunteer_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM volunteers WHERE id = ?', (volunteer_id,))
    conn.commit()
    conn.close()
    
    flash('Volunteer deleted successfully!', 'success')
    return redirect(url_for('admin_volunteers'))

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    app.run(debug=True)
