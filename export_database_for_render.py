"""
Database Backup Script for Render Deployment
Export complete PostgreSQL database with all data
"""

import subprocess
import os
from datetime import datetime

def export_database():
    """Export PostgreSQL database for Render deployment"""
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f'render_backup_{timestamp}.sql'
    
    # Database configuration (your local database)
    db_config = {
        'host': 'localhost',
        'database': 'women_safety_db',
        'user': 'postgres',
        'password': 'postgres123',
        'port': '5432'
    }
    
    print("=" * 60)
    print("🔄 Database Export for Render Deployment")
    print("=" * 60)
    print(f"📋 Database: {db_config['database']}")
    print(f"📋 Host: {db_config['host']}")
    print(f"📋 Output File: {backup_file}")
    print("=" * 60)
    
    # Set password environment variable
    os.environ['PGPASSWORD'] = db_config['password']
    
    # Export command with all necessary flags
    cmd = [
        'pg_dump',
        '-h', db_config['host'],
        '-p', db_config['port'],
        '-U', db_config['user'],
        '-d', db_config['database'],
        '--clean',              # Add DROP statements
        '--if-exists',          # Use IF EXISTS for DROP
        '--inserts',            # Use INSERT statements (more compatible)
        '--column-inserts',     # Include column names in INSERT
        '-f', backup_file
    ]
    
    try:
        print("\n⏳ Exporting database...")
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        # Get file size
        file_size = os.path.getsize(backup_file)
        file_size_kb = file_size / 1024
        file_size_mb = file_size_kb / 1024
        
        print(f"\n✅ Database exported successfully!")
        print(f"📦 File: {backup_file}")
        if file_size_mb > 1:
            print(f"📦 Size: {file_size_mb:.2f} MB")
        else:
            print(f"📦 Size: {file_size_kb:.2f} KB")
        
        print("\n" + "=" * 60)
        print("📋 Next Steps:")
        print("=" * 60)
        print("1. Create PostgreSQL database on Render")
        print("2. Get connection details from Render")
        print("3. Restore using this command:")
        print(f"\n   psql -h <render-host> -U <render-user> -d <render-db> -f {backup_file}\n")
        print("4. Enter password when prompted")
        print("=" * 60)
        
        return backup_file
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Export failed!")
        print(f"Error: {e.stderr if hasattr(e, 'stderr') else str(e)}")
        print("\n💡 Troubleshooting:")
        print("   - Check if PostgreSQL is running")
        print("   - Verify database credentials")
        print("   - Ensure pg_dump is in PATH")
        return None
        
    except FileNotFoundError:
        print("\n❌ pg_dump command not found!")
        print("\n💡 Please install PostgreSQL or add it to PATH:")
        print("   - Windows: C:\\Program Files\\PostgreSQL\\<version>\\bin")
        print("   - Add to System Environment Variables")
        return None
        
    finally:
        # Clear password from environment
        if 'PGPASSWORD' in os.environ:
            del os.environ['PGPASSWORD']


def check_database_stats():
    """Check database size and table counts"""
    try:
        import psycopg2
        
        conn = psycopg2.connect(
            host='localhost',
            database='women_safety_db',
            user='postgres',
            password='postgres123',
            port='5432'
        )
        cur = conn.cursor()
        
        print("\n" + "=" * 60)
        print("📊 Database Statistics")
        print("=" * 60)
        
        # Get database size
        cur.execute("SELECT pg_size_pretty(pg_database_size('women_safety_db'))")
        db_size = cur.fetchone()[0]
        print(f"💾 Total Database Size: {db_size}")
        
        # Get table counts
        cur.execute("""
            SELECT 
                schemaname,
                tablename,
                pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
            FROM pg_tables
            WHERE schemaname = 'public'
            ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC
            LIMIT 10
        """)
        
        print("\n📋 Top 10 Tables by Size:")
        print("-" * 60)
        for schema, table, size in cur.fetchall():
            print(f"   {table:<30} {size:>15}")
        
        # Get row counts for main tables
        tables = ['volunteers', 'gallery_items', 'districts', 'shakthi_teams', 
                  'admin_credentials', 'email_otp']
        
        print("\n📊 Row Counts:")
        print("-" * 60)
        for table in tables:
            try:
                cur.execute(f"SELECT COUNT(*) FROM {table}")
                count = cur.fetchone()[0]
                print(f"   {table:<30} {count:>10} rows")
            except:
                pass
        
        cur.close()
        conn.close()
        print("=" * 60)
        
    except Exception as e:
        print(f"\n⚠️ Could not fetch database stats: {e}")


if __name__ == '__main__':
    print("\n🚀 Starting Database Backup Process...\n")
    
    # Check database statistics first
    check_database_stats()
    
    # Export database
    backup_file = export_database()
    
    if backup_file:
        print("\n✅ Backup process completed successfully!")
        print(f"\n📁 Your backup file is ready: {backup_file}")
        print("\n🎯 You can now proceed with Render deployment!")
    else:
        print("\n❌ Backup process failed. Please check errors above.")
