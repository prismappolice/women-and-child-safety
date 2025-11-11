"""
PostgreSQL Migration Script
Migrates data from SQLite to PostgreSQL
Preserves all data, structure, and relationships
"""

import sqlite3
import psycopg2
from psycopg2 import sql
import sys
from datetime import datetime

# PostgreSQL connection parameters
# CHANGE THESE ACCORDING TO YOUR POSTGRESQL SETUP
PG_CONFIG = {
    'host': 'localhost',
    'database': 'women_safety_db',
    'user': 'postgres',
    'password': 'postgres123',
    'port': 5432
}

PG_ADMIN_CONFIG = {
    'host': 'localhost',
    'database': 'women_safety_db',
    'user': 'postgres',
    'password': 'postgres123',
    'port': 5432
}

# SQLite database files
SQLITE_MAIN_DB = 'women_safety.db'
SQLITE_ADMIN_DB = 'database.db'
SQLITE_VOLUNTEER_DB = 'volunteer_system.db'

class DatabaseMigration:
    def __init__(self):
        self.sqlite_conn = None
        self.pg_conn = None
        self.migration_log = []
        
    def log(self, message):
        """Log migration progress"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        self.migration_log.append(log_message)
        
    def connect_postgresql(self, config):
        """Connect to PostgreSQL database"""
        try:
            conn = psycopg2.connect(**config)
            conn.autocommit = False
            self.log(f"✅ Connected to PostgreSQL: {config['database']}")
            return conn
        except Exception as e:
            self.log(f"❌ Error connecting to PostgreSQL: {e}")
            sys.exit(1)
            
    def connect_sqlite(self, db_file):
        """Connect to SQLite database"""
        try:
            conn = sqlite3.connect(db_file)
            self.log(f"✅ Connected to SQLite: {db_file}")
            return conn
        except Exception as e:
            self.log(f"❌ Error connecting to SQLite: {e}")
            sys.exit(1)
            
    def get_table_columns(self, sqlite_cursor, table_name):
        """Get column names from SQLite table"""
        sqlite_cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [row[1] for row in sqlite_cursor.fetchall()]
        return columns
        
    def migrate_table(self, sqlite_conn, pg_conn, table_name, exclude_id=False):
        """Migrate a single table from SQLite to PostgreSQL"""
        try:
            sqlite_cursor = sqlite_conn.cursor()
            pg_cursor = pg_conn.cursor()
            
            # Get columns
            columns = self.get_table_columns(sqlite_cursor, table_name)
            
            # Get data from SQLite
            sqlite_cursor.execute(f"SELECT * FROM {table_name}")
            rows = sqlite_cursor.fetchall()
            
            if not rows:
                self.log(f"⚠️  Table '{table_name}' is empty, skipping data migration")
                return 0
                
            # Prepare columns for INSERT (excluding id if needed)
            if exclude_id and 'id' in columns:
                insert_columns = [col for col in columns if col != 'id']
            else:
                insert_columns = columns
                
            # Create INSERT query
            placeholders = ', '.join(['%s'] * len(insert_columns))
            insert_query = f"INSERT INTO {table_name} ({', '.join(insert_columns)}) VALUES ({placeholders})"
            
            # Insert data
            inserted_count = 0
            for row in rows:
                try:
                    if exclude_id and 'id' in columns:
                        # Skip the id column (first column)
                        row_data = row[1:]
                    else:
                        row_data = row
                        
                    pg_cursor.execute(insert_query, row_data)
                    inserted_count += 1
                except Exception as e:
                    self.log(f"⚠️  Error inserting row in {table_name}: {e}")
                    continue
                    
            pg_conn.commit()
            self.log(f"✅ Migrated {inserted_count} rows to '{table_name}'")
            return inserted_count
            
        except Exception as e:
            self.log(f"❌ Error migrating table '{table_name}': {e}")
            pg_conn.rollback()
            return 0
            
    def reset_sequence(self, pg_conn, table_name):
        """Reset PostgreSQL sequence for auto-increment columns"""
        try:
            pg_cursor = pg_conn.cursor()
            pg_cursor.execute(f"""
                SELECT setval(pg_get_serial_sequence('{table_name}', 'id'), 
                    COALESCE((SELECT MAX(id) FROM {table_name}), 1), 
                    true);
            """)
            pg_conn.commit()
            self.log(f"✅ Reset sequence for '{table_name}'")
        except Exception as e:
            self.log(f"⚠️  Could not reset sequence for '{table_name}': {e}")
            
    def migrate_main_database(self):
        """Migrate women_safety.db to PostgreSQL"""
        self.log("\n" + "="*60)
        self.log("MIGRATING MAIN DATABASE: women_safety.db")
        self.log("="*60)
        
        sqlite_conn = self.connect_sqlite(SQLITE_MAIN_DB)
        pg_conn = self.connect_postgresql(PG_CONFIG)
        
        # Tables in order (respecting foreign key dependencies)
        tables_order = [
            'content',
            'media_gallery',
            'officers',
            'success_stories',
            'site_settings',
            'district_info',
            'safety_tips',
            'initiatives',
            'pdf_resources',
            'events',
            'page_content',
            'emergency_numbers',
            'about_content',
            'home_content',
            'gallery_items',
            'navigation_menu',
            'contact_info',
            'districts',  # Master table first
            'district_sps',
            'shakthi_teams',
            'women_police_stations',
            'one_stop_centers',
            'volunteers',  # Volunteer master table
            'volunteer_status',
            'volunteer_scores',
            'email_notifications',
            'admin_settings'
        ]
        
        total_rows = 0
        for table in tables_order:
            count = self.migrate_table(sqlite_conn, pg_conn, table, exclude_id=True)
            total_rows += count
            if count > 0:
                self.reset_sequence(pg_conn, table)
                
        sqlite_conn.close()
        pg_conn.close()
        
        self.log(f"\n✅ Main database migration completed: {total_rows} total rows migrated")
        return total_rows
        
    def migrate_admin_database(self):
        """Migrate database.db (admin) to PostgreSQL"""
        self.log("\n" + "="*60)
        self.log("MIGRATING ADMIN DATABASE: database.db")
        self.log("="*60)
        
        sqlite_conn = self.connect_sqlite(SQLITE_ADMIN_DB)
        pg_conn = self.connect_postgresql(PG_ADMIN_CONFIG)
        
        # Admin tables in order
        tables_order = [
            'admin_credentials',
            'admin_security_questions',
            'admin_security'
        ]
        
        total_rows = 0
        for table in tables_order:
            try:
                count = self.migrate_table(sqlite_conn, pg_conn, table, exclude_id=True)
                total_rows += count
                if count > 0:
                    self.reset_sequence(pg_conn, table)
            except Exception as e:
                self.log(f"⚠️  Table '{table}' might not exist: {e}")
                continue
                
        sqlite_conn.close()
        pg_conn.close()
        
        self.log(f"\n✅ Admin database migration completed: {total_rows} total rows migrated")
        return total_rows
        
    def verify_migration(self):
        """Verify that data was migrated correctly"""
        self.log("\n" + "="*60)
        self.log("VERIFYING MIGRATION")
        self.log("="*60)
        
        # Verify main database
        sqlite_conn = self.connect_sqlite(SQLITE_MAIN_DB)
        pg_conn = self.connect_postgresql(PG_CONFIG)
        
        sqlite_cursor = sqlite_conn.cursor()
        pg_cursor = pg_conn.cursor()
        
        verification_tables = ['volunteers', 'gallery_items', 'officers', 'districts']
        
        all_verified = True
        for table in verification_tables:
            try:
                # Count in SQLite
                sqlite_cursor.execute(f"SELECT COUNT(*) FROM {table}")
                sqlite_count = sqlite_cursor.fetchone()[0]
                
                # Count in PostgreSQL
                pg_cursor.execute(f"SELECT COUNT(*) FROM {table}")
                pg_count = pg_cursor.fetchone()[0]
                
                if sqlite_count == pg_count:
                    self.log(f"✅ {table}: {pg_count} rows (matched)")
                else:
                    self.log(f"⚠️  {table}: SQLite={sqlite_count}, PostgreSQL={pg_count} (mismatch)")
                    all_verified = False
            except Exception as e:
                self.log(f"⚠️  Could not verify {table}: {e}")
                
        sqlite_conn.close()
        pg_conn.close()
        
        return all_verified
        
    def save_log(self):
        """Save migration log to file"""
        log_filename = f"migration_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(log_filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.migration_log))
        self.log(f"\n✅ Migration log saved to: {log_filename}")
        
    def run_migration(self):
        """Run complete migration process"""
        self.log("="*60)
        self.log("POSTGRESQL MIGRATION STARTED")
        self.log("="*60)
        self.log(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.log(f"SQLite Databases: {SQLITE_MAIN_DB}, {SQLITE_ADMIN_DB}")
        self.log(f"PostgreSQL: {PG_CONFIG['host']}:{PG_CONFIG['port']}")
        
        try:
            # Migrate main database
            main_rows = self.migrate_main_database()
            
            # Migrate admin database
            admin_rows = self.migrate_admin_database()
            
            # Verify migration
            verified = self.verify_migration()
            
            # Summary
            self.log("\n" + "="*60)
            self.log("MIGRATION SUMMARY")
            self.log("="*60)
            self.log(f"Total rows migrated: {main_rows + admin_rows}")
            self.log(f"Verification: {'✅ PASSED' if verified else '⚠️  CHECK LOG'}")
            self.log("="*60)
            
            # Save log
            self.save_log()
            
            if verified:
                self.log("\n🎉 MIGRATION COMPLETED SUCCESSFULLY!")
                self.log("\nNext steps:")
                self.log("1. Update app.py to use PostgreSQL")
                self.log("2. Update admin_security.py for PostgreSQL")
                self.log("3. Test all functionalities")
                self.log("4. Keep SQLite backups for rollback if needed")
            else:
                self.log("\n⚠️  Migration completed with warnings. Please check the log.")
                
        except Exception as e:
            self.log(f"\n❌ MIGRATION FAILED: {e}")
            import traceback
            self.log(traceback.format_exc())
            self.save_log()
            sys.exit(1)

if __name__ == "__main__":
    print("\n" + "="*60)
    print("PostgreSQL Migration Tool")
    print("Women and Child Safety Wing Project")
    print("="*60)
    print("\n⚠️  IMPORTANT: Before running this script:")
    print("1. Install PostgreSQL and create databases: women_safety, admin_db")
    print("2. Run postgresql_schema.sql in 'women_safety' database")
    print("3. Run postgresql_admin_schema.sql in 'admin_db' database")
    print("4. Update PG_CONFIG with your PostgreSQL credentials in this file")
    print("5. Ensure SQLite databases exist and are backed up")
    print("\nPress Enter to continue or Ctrl+C to cancel...")
    input()
    
    migrator = DatabaseMigration()
    migrator.run_migration()
