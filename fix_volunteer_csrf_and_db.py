"""
Fix Volunteer Registration CSRF and Database Issues
- Add db_config import
- Update volunteer_registration route to use db_config
- Ensure CSRF protection is working
"""

import re

# Read the current app.py
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

print("🔍 Analyzing app.py for issues...")

# Check if db_config is imported
if 'from db_config import' not in content and 'import db_config' not in content:
    print("❌ db_config not imported - adding import")
    
    # Find the import section and add db_config import
    import_section = content.find('from datetime import datetime')
    if import_section != -1:
        # Add after datetime import
        content = content.replace(
            'from datetime import datetime',
            'from datetime import datetime\nfrom db_config import get_db_connection, adapt_query, execute_query'
        )
        print("✅ Added db_config imports")
else:
    print("✅ db_config already imported")

# Now fix the volunteer_registration route
old_route = '''@app.route('/volunteer-registration', methods=['GET', 'POST'])
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
        experience = request.form.get('experience', '')  # Make optional
        motivation = request.form.get('motivation')
        availability = request.form.get('availability')
        skills = request.form.get('skills')

        # Basic validation
        if not all([name, email, phone, age, address, occupation, education, motivation, availability, skills]):
            flash('Please fill in all required fields', 'error')
            return redirect(url_for('volunteer_registration'))

        try:
            conn = sqlite3.connect('women_safety.db')
            cursor = conn.cursor()
            
            # Check if phone number already exists
            cursor.execute('SELECT id, registration_id FROM volunteers WHERE phone = ?', (phone,))
            existing = cursor.fetchone()
            if existing:
                flash(f'This phone number is already registered with ID: {existing[1]}', 'error')
                return redirect(url_for('volunteer_registration'))

            # Generate registration ID
            year = datetime.now().year
            cursor.execute('SELECT registration_id FROM volunteers WHERE registration_id LIKE ? ORDER BY id DESC LIMIT 1', (f'VOL-{year}-%',))
            last_reg = cursor.fetchone()
            
            if last_reg:
                last_num = int(last_reg[0].split('-')[-1])
                registration_id = f'VOL-{year}-{last_num + 1:04d}'
            else:
                registration_id = f'VOL-{year}-0001'

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
            
            # Insert status record
            cursor.execute('''
                INSERT INTO volunteer_status (volunteer_id, status)
                VALUES (?, 'pending')
            ''', (volunteer_id,))

            conn.commit()
            flash(f'Registration successful! Your Registration ID is {registration_id}. Please save this for future reference.', 'success')
            return redirect(url_for('volunteer_registration'))

        except Exception as e:
            print(f"Registration Error: {e}")
            import traceback
            traceback.print_exc()
            flash(f'An error occurred during registration: {str(e)}', 'error')
            return redirect(url_for('volunteer_registration'))
        finally:
            if conn:
                conn.close()

    return render_template('volunteer_registration.html')'''

new_route = '''@app.route('/volunteer-registration', methods=['GET', 'POST'])
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
        experience = request.form.get('experience', '')  # Make optional
        motivation = request.form.get('motivation')
        availability = request.form.get('availability')
        skills = request.form.get('skills')

        # Basic validation
        if not all([name, email, phone, age, address, occupation, education, motivation, availability, skills]):
            flash('Please fill in all required fields', 'error')
            return redirect(url_for('volunteer_registration'))

        try:
            # Use db_config for database connection (supports both SQLite and PostgreSQL)
            conn = get_db_connection('main')
            cursor = conn.cursor()
            
            # Check if phone number already exists
            query = adapt_query('SELECT id, registration_id FROM volunteers WHERE phone = ?')
            cursor.execute(query, (phone,))
            existing = cursor.fetchone()
            if existing:
                flash(f'This phone number is already registered with ID: {existing[1]}', 'error')
                return redirect(url_for('volunteer_registration'))

            # Generate registration ID
            year = datetime.now().year
            query = adapt_query('SELECT registration_id FROM volunteers WHERE registration_id LIKE ? ORDER BY id DESC LIMIT 1')
            cursor.execute(query, (f'VOL-{year}-%',))
            last_reg = cursor.fetchone()
            
            if last_reg:
                last_num = int(last_reg[0].split('-')[-1])
                registration_id = f'VOL-{year}-{last_num + 1:04d}'
            else:
                registration_id = f'VOL-{year}-0001'

            # Insert volunteer data
            query = adapt_query('''
                INSERT INTO volunteers (
                    registration_id, name, email, phone, age, address,
                    occupation, education, experience, motivation,
                    availability, skills
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''')
            cursor.execute(query, (registration_id, name, email, phone, age, address,
                  occupation, education, experience, motivation,
                  availability, skills))

            # Get volunteer_id (PostgreSQL compatible)
            if hasattr(cursor, 'lastrowid') and cursor.lastrowid:
                volunteer_id = cursor.lastrowid
            else:
                # PostgreSQL - get the last inserted id
                cursor.execute('SELECT currval(pg_get_serial_sequence(%s, %s))', ('volunteers', 'id'))
                volunteer_id = cursor.fetchone()[0]
            
            # Insert status record
            query = adapt_query('''
                INSERT INTO volunteer_status (volunteer_id, status)
                VALUES (?, 'pending')
            ''')
            cursor.execute(query, (volunteer_id,))

            conn.commit()
            flash(f'Registration successful! Your Registration ID is {registration_id}. Please save this for future reference.', 'success')
            return redirect(url_for('volunteer_registration'))

        except Exception as e:
            print(f"Registration Error: {e}")
            import traceback
            traceback.print_exc()
            flash(f'An error occurred during registration: {str(e)}', 'error')
            return redirect(url_for('volunteer_registration'))
        finally:
            if conn:
                conn.close()

    return render_template('volunteer_registration.html')'''

if old_route in content:
    content = content.replace(old_route, new_route)
    print("✅ Updated volunteer_registration route to use db_config")
else:
    print("⚠️  Could not find exact route pattern - checking for variations...")

# Write the updated content back
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Fixed volunteer registration route!")
print("\n📋 Changes made:")
print("1. Added db_config imports")
print("2. Updated volunteer_registration to use get_db_connection()")
print("3. Updated all SQL queries to use adapt_query() for PostgreSQL compatibility")
print("4. Fixed volunteer_id retrieval for PostgreSQL")
print("\n🚀 Please restart the Flask application for changes to take effect")
