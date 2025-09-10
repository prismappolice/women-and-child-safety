from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from datetime import datetime
from volunteer_db import generate_registration_id

from flask import Blueprint

app = Blueprint('volunteer', __name__)

@app.route('/')
@app.route('/registration', methods=['GET', 'POST'])
def volunteer_registration():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        age = request.form.get('age')
        address = request.form.get('address')
        occupation = request.form.get('occupation')
        education = request.form.get('education')
        experience = request.form.get('experience')
        motivation = request.form.get('motivation')
        availability = request.form.get('availability')
        skills = request.form.get('skills')

        # Validate form data
        errors = []
        
        # Name validation    
        if not name:
            errors.append('Name is required')
        elif len(name.strip()) < 3:
            errors.append('Name must be at least 3 characters')
        elif not all(x.isalpha() or x.isspace() for x in name):
            errors.append('Name should only contain letters and spaces')
            
        # Email validation
        if not email:
            errors.append('Email is required')
        elif '@' not in email or '.' not in email:
            errors.append('Please enter a valid email address')
            
        # Phone validation
        if not phone:
            errors.append('Phone number is required')
        elif len(phone) != 10 or not phone.isdigit():
            errors.append('Phone number must be exactly 10 digits')
        elif phone.startswith('0'):
            errors.append('Phone number cannot start with 0')
        elif all(d == phone[0] for d in phone):
            errors.append('Invalid phone number - cannot be all same digits')
            
        # Age validation
        if not age:
            errors.append('Age is required')
        else:
            try:
                age_num = int(age)
                if age_num < 18:
                    errors.append('You must be at least 18 years old to volunteer')
                elif age_num > 65:
                    errors.append('Age must be 65 or below')
            except:
                errors.append('Please enter a valid age number')
            
        # Address validation
        if not address:
            errors.append('Address is required')
        elif len(address.strip()) < 10:
            errors.append('Please enter your complete address (minimum 10 characters)')
            
        # Occupation validation
        if not occupation:
            errors.append('Occupation is required')
        elif len(occupation.strip()) < 3:
            errors.append('Please enter a valid occupation')
            
        # Education validation
        if not education:
            errors.append('Education details are required')
        elif len(education.strip()) < 5:
            errors.append('Please provide complete education details')
            
        # Experience validation (optional but if provided should be valid)
        if experience and len(experience.strip()) < 5:
            errors.append('If providing experience, please give more details')
            
        # Motivation validation
        if not motivation:
            errors.append('Please tell us why you want to volunteer')
        elif len(motivation.strip()) < 30:
            errors.append('Please provide more details about your motivation (minimum 30 characters)')
            
        # Availability validation
        if not availability:
            errors.append('Please specify your availability')
        elif len(availability.strip()) < 5:
            errors.append('Please provide more details about your availability')
            
        # Skills validation
        if not skills:
            errors.append('Please list your relevant skills')
        elif len(skills.strip()) < 5:
            errors.append('Please provide more details about your skills')

        # If there are any validation errors
        if errors:
            for error in errors:
                flash(error, 'error')
            return redirect(url_for('registration'))

        try:
            conn = sqlite3.connect('volunteer_system.db')
            cursor = conn.cursor()

            # Check if phone number already exists
            cursor.execute('SELECT id FROM volunteers WHERE phone = ?', (phone,))
            if cursor.fetchone():
                flash('This phone number is already registered', 'error')
                return redirect(url_for('volunteer.volunteer_registration'))

            # Generate registration ID
            registration_id = generate_registration_id()

            # Insert volunteer data
            cursor.execute('''
                INSERT INTO volunteers (
                    registration_id, name, email, phone, age, address, 
                    occupation, education, experience, motivation, 
                    availability, skills
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (registration_id, name, email, phone, age, address, 
                  occupation, education, experience, motivation, 
                  availability, skills))
            
            volunteer_id = cursor.lastrowid

            # Create initial status entry
            cursor.execute('''
                INSERT INTO volunteer_status (volunteer_id, status)
                VALUES (?, 'pending')
            ''', (volunteer_id,))

            conn.commit()
            flash(f'Registration successful! Your Registration ID is {registration_id}', 'success')
            return render_template('volunteer_success.html', registration_id=registration_id)

        except Exception as e:
            print(f"Error: {e}")
            flash('An error occurred during registration', 'error')
            return redirect(url_for('volunteer_registration'))
        finally:
            conn.close()

    return render_template('volunteer_registration.html')

@app.route('/check-status', methods=['GET', 'POST'])
def check_status():
    if request.method == 'POST':
        identifier = request.form.get('identifier')
        
        try:
            conn = sqlite3.connect('volunteer_system.db')
            cursor = conn.cursor()

            # Check if identifier is registration ID or phone
            if identifier.startswith('VOL-'):
                query = 'registration_id = ?'
            else:
                query = 'phone = ?'

            cursor.execute(f'''
                SELECT v.*, vs.status, vs.updated_at 
                FROM volunteers v 
                JOIN volunteer_status vs ON v.id = vs.volunteer_id 
                WHERE v.{query}
            ''', (identifier,))
            
            result = cursor.fetchone()
            
            if result:
                application = {
                    'registration_id': result[1],
                    'name': result[2],
                    'status': result[-2],
                    'created_at': result[-3],
                    'updated_at': result[-1]
                }
                return render_template('check_status.html', application=application)
            else:
                flash('No application found with the provided details', 'error')

        except Exception as e:
            print(f"Error: {e}")
            flash('An error occurred while checking status', 'error')
        finally:
            conn.close()

    return render_template('check_status.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'admin123':  # Change these credentials
            session['admin_logged_in'] = True
            return redirect(url_for('admin_volunteers'))
        
        flash('Invalid credentials', 'error')
    return render_template('admin_login.html')

@app.route('/admin/volunteers')
def admin_volunteers():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
        
    try:
        conn = sqlite3.connect('volunteer_system.db')
        cursor = conn.cursor()

        status_filter = request.args.get('status')
        
        query = '''
            SELECT v.*, vs.status 
            FROM volunteers v 
            JOIN volunteer_status vs ON v.id = vs.volunteer_id
        '''
        
        if status_filter:
            query += ' WHERE vs.status = ?'
            cursor.execute(query, (status_filter,))
        else:
            cursor.execute(query)

        results = cursor.fetchall()
        volunteers = []
        for row in results:
            volunteers.append({
                'id': row[0],
                'registration_id': row[1],
                'name': row[2],
                'phone': row[4],
                'status': row[-1],
                'created_at': row[-2]
            })

        return render_template('admin_volunteers.html', volunteers=volunteers)

    except Exception as e:
        print(f"Error: {e}")
        flash('An error occurred while fetching volunteer data', 'error')
        return redirect(url_for('admin_login'))
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Running on different port to avoid conflict
