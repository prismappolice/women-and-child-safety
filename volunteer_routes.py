from flask import Blueprint, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime
from functools import wraps
from .volunteer_system import generate_registration_id

volunteer_bp = Blueprint('volunteer', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

@volunteer_bp.route('/volunteer-registration', methods=['GET', 'POST'])
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

        # Basic validation
        if not all([name, email, phone, age, address, occupation, education, motivation, availability, skills]):
            flash('Please fill in all required fields', 'error')
            return redirect(url_for('volunteer.volunteer_registration'))

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
            return redirect(url_for('volunteer.volunteer_registration'))
        finally:
            conn.close()

    return render_template('volunteer_registration.html')

@volunteer_bp.route('/check-status', methods=['GET', 'POST'])
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

@volunteer_bp.route('/admin/volunteers')
@admin_required
def admin_volunteers():
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
        return redirect(url_for('admin.dashboard'))
    finally:
        conn.close()

@volunteer_bp.route('/admin/volunteer/<int:volunteer_id>')
@admin_required
def admin_volunteer_detail(volunteer_id):
    try:
        conn = sqlite3.connect('volunteer_system.db')
        cursor = conn.cursor()

        cursor.execute('''
            SELECT v.*, vs.status, vs.admin_notes, vs.updated_at 
            FROM volunteers v 
            JOIN volunteer_status vs ON v.id = vs.volunteer_id 
            WHERE v.id = ?
        ''', (volunteer_id,))
        
        result = cursor.fetchone()
        
        if result:
            volunteer = {
                'id': result[0],
                'registration_id': result[1],
                'name': result[2],
                'email': result[3],
                'phone': result[4],
                'age': result[5],
                'address': result[6],
                'occupation': result[7],
                'education': result[8],
                'experience': result[9],
                'motivation': result[10],
                'availability': result[11],
                'skills': result[12],
                'created_at': result[13],
                'status': result[14],
                'admin_notes': result[15],
                'updated_at': result[16]
            }
            return render_template('admin_volunteer_detail.html', volunteer=volunteer)
        else:
            flash('Volunteer not found', 'error')
            return redirect(url_for('volunteer.admin_volunteers'))

    except Exception as e:
        print(f"Error: {e}")
        flash('An error occurred while fetching volunteer details', 'error')
        return redirect(url_for('volunteer.admin_volunteers'))
    finally:
        conn.close()

@volunteer_bp.route('/admin/volunteer/<int:volunteer_id>/update', methods=['POST'])
@admin_required
def update_volunteer_status(volunteer_id):
    status = request.form.get('status')
    admin_notes = request.form.get('admin_notes')

    if not status:
        flash('Status is required', 'error')
        return redirect(url_for('volunteer.admin_volunteer_detail', volunteer_id=volunteer_id))

    try:
        conn = sqlite3.connect('volunteer_system.db')
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE volunteer_status 
            SET status = ?, admin_notes = ?, updated_at = datetime('now') 
            WHERE volunteer_id = ?
        ''', (status, admin_notes, volunteer_id))

        conn.commit()
        flash('Volunteer status updated successfully', 'success')

    except Exception as e:
        print(f"Error: {e}")
        flash('An error occurred while updating status', 'error')
    finally:
        conn.close()

    return redirect(url_for('volunteer.admin_volunteer_detail', volunteer_id=volunteer_id))
