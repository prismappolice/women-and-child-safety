import sqlite3
import os

def migrate_database():
    """Migrate database to handle column name differences"""
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    print("Starting database migration...")
    
    try:
        # Check current volunteers table structure
        cursor.execute("PRAGMA table_info(volunteers)")
        columns = cursor.fetchall()
        
        existing_columns = [col[1] for col in columns]
        print(f"Existing columns: {existing_columns}")
        
        # Check if we have old structure with full_name instead of name
        if 'full_name' in existing_columns and 'name' not in existing_columns:
            print("Found old structure with 'full_name', migrating to 'name'...")
            
            # Create backup
            cursor.execute("CREATE TABLE volunteers_backup AS SELECT * FROM volunteers")
            print("Created backup table...")
            
            # Drop old table
            cursor.execute("DROP TABLE volunteers")
            print("Dropped old volunteers table...")
            
            # Create new table with correct structure
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
            print("Created new volunteers table...")
            
            # Migrate data from backup
            cursor.execute('''
                INSERT INTO volunteers (name, email, phone, age, address, occupation, education, experience, motivation, availability, skills)
                SELECT 
                    COALESCE(full_name, '') as name,
                    COALESCE(email, '') as email,
                    COALESCE(phone, '') as phone,  
                    COALESCE(district, '') as age,
                    COALESCE(district, '') as address,
                    COALESCE(occupation, '') as occupation,
                    COALESCE(education, '') as education,
                    '' as experience,
                    '' as motivation,
                    '' as availability,
                    COALESCE(interests, '') as skills
                FROM volunteers_backup
            ''')
            print("Migrated data from backup...")
            
        elif 'name' not in existing_columns:
            print("Creating new volunteers table...")
            
            # Create new table if it doesn't have the right structure
            cursor.execute("DROP TABLE IF EXISTS volunteers")
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
            print("Created new volunteers table...")
        else:
            print("Volunteers table already has correct structure")
        
        # Ensure email tables exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS email_notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                volunteer_id INTEGER,
                email_type TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT NOT NULL,
                sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'sent',
                FOREIGN KEY (volunteer_id) REFERENCES volunteers (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS volunteer_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                volunteer_id INTEGER UNIQUE,
                age_score INTEGER DEFAULT 0,
                education_score INTEGER DEFAULT 0,
                motivation_score INTEGER DEFAULT 0,
                skills_score INTEGER DEFAULT 0,
                total_score INTEGER DEFAULT 0,
                status TEXT DEFAULT 'pending',
                admin_notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (volunteer_id) REFERENCES volunteers (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS admin_settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                setting_name TEXT UNIQUE NOT NULL,
                setting_value TEXT,
                description TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        print("✅ Database migration completed successfully!")
        
        # Show final structure
        cursor.execute("PRAGMA table_info(volunteers)")
        columns = cursor.fetchall()
        print("\nFinal volunteers table structure:")
        for col in columns:
            print(f"- {col[1]} ({col[2]})")
            
    except Exception as e:
        print(f"❌ Migration failed: {str(e)}")
        conn.rollback()
    
    finally:
        conn.close()

if __name__ == "__main__":
    migrate_database()
