"""
Quick PostgreSQL Setup and Migration Script
Run this after installing PostgreSQL
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a system command and display result"""
    print(f"\n{'='*60}")
    print(f"📌 {description}")
    print(f"{'='*60}")
    print(f"Command: {command}\n")
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ Success!")
        if result.stdout:
            print(result.stdout)
        return True
    else:
        print(f"❌ Error!")
        if result.stderr:
            print(result.stderr)
        return False

def check_postgresql():
    """Check if PostgreSQL is installed"""
    print("\n" + "="*60)
    print("Checking PostgreSQL Installation...")
    print("="*60)
    
    result = subprocess.run("psql --version", shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ PostgreSQL is installed: {result.stdout.strip()}")
        return True
    else:
        print("❌ PostgreSQL is not installed!")
        print("\nPlease install PostgreSQL from:")
        print("https://www.postgresql.org/download/windows/")
        return False

def check_python_packages():
    """Check if required Python packages are installed"""
    print("\n" + "="*60)
    print("Checking Python Packages...")
    print("="*60)
    
    required = ['psycopg2', 'flask']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is NOT installed")
            missing.append(package)
    
    return len(missing) == 0, missing

def install_packages():
    """Install required Python packages"""
    print("\n" + "="*60)
    print("Installing Python Packages...")
    print("="*60)
    
    return run_command("pip install psycopg2-binary", "Installing psycopg2-binary")

def create_databases():
    """Create PostgreSQL databases"""
    print("\n" + "="*60)
    print("Creating PostgreSQL Databases")
    print("="*60)
    print("\nYou will need to enter your PostgreSQL password")
    
    commands = [
        'CREATE DATABASE women_safety;',
        'CREATE DATABASE admin_db;'
    ]
    
    for cmd in commands:
        print(f"\nExecuting: {cmd}")
        result = subprocess.run(
            f'psql -U postgres -c "{cmd}"',
            shell=True,
            capture_output=True,
            text=True
        )
        
        if "already exists" in result.stderr:
            print(f"⚠️  Database already exists, skipping...")
        elif result.returncode == 0:
            print(f"✅ Database created successfully")
        else:
            print(f"❌ Error: {result.stderr}")
            return False
    
    return True

def run_schema_scripts():
    """Run schema creation scripts"""
    print("\n" + "="*60)
    print("Creating Database Schemas")
    print("="*60)
    
    # Main database schema
    if run_command(
        'psql -U postgres -d women_safety -f postgresql_schema.sql',
        "Creating main database schema"
    ):
        print("✅ Main schema created")
    else:
        print("❌ Failed to create main schema")
        return False
    
    # Admin database schema
    if run_command(
        'psql -U postgres -d admin_db -f postgresql_admin_schema.sql',
        "Creating admin database schema"
    ):
        print("✅ Admin schema created")
    else:
        print("❌ Failed to create admin schema")
        return False
    
    return True

def update_config():
    """Update database configuration"""
    print("\n" + "="*60)
    print("Configuration Update Required")
    print("="*60)
    print("\n⚠️  IMPORTANT: You need to update PostgreSQL password in these files:")
    print("\n1. migrate_to_postgresql.py")
    print("   - Lines 14-25: Update PG_CONFIG and PG_ADMIN_CONFIG")
    print("\n2. db_config.py")
    print("   - Lines 24-34: Update POSTGRESQL_CONFIG")
    print("\nReplace 'your_password_here' with your actual PostgreSQL password")
    print("\nPress Enter after updating the configuration files...")
    input()

def run_migration():
    """Run data migration script"""
    print("\n" + "="*60)
    print("Running Data Migration")
    print("="*60)
    print("\nThis will migrate all data from SQLite to PostgreSQL")
    print("Press Enter to continue or Ctrl+C to cancel...")
    input()
    
    return run_command("python migrate_to_postgresql.py", "Migrating data")

def main():
    """Main setup process"""
    print("\n" + "="*70)
    print(" "*15 + "PostgreSQL Setup & Migration")
    print(" "*10 + "Women and Child Safety Wing Project")
    print("="*70)
    
    # Step 1: Check PostgreSQL
    if not check_postgresql():
        print("\n❌ Setup aborted: PostgreSQL not found")
        return False
    
    # Step 2: Check/Install Python packages
    packages_ok, missing = check_python_packages()
    if not packages_ok:
        print(f"\n⚠️  Missing packages: {', '.join(missing)}")
        if input("\nInstall missing packages? (y/n): ").lower() == 'y':
            if not install_packages():
                print("\n❌ Failed to install packages")
                return False
        else:
            print("\n❌ Setup aborted: Required packages not installed")
            return False
    
    # Step 3: Create databases
    print("\n" + "="*60)
    print("Step 1: Create PostgreSQL Databases")
    print("="*60)
    if input("\nCreate databases? (y/n): ").lower() == 'y':
        if not create_databases():
            print("\n❌ Failed to create databases")
            return False
    
    # Step 4: Run schema scripts
    print("\n" + "="*60)
    print("Step 2: Create Database Schemas")
    print("="*60)
    if input("\nRun schema scripts? (y/n): ").lower() == 'y':
        if not run_schema_scripts():
            print("\n❌ Failed to create schemas")
            return False
    
    # Step 5: Update configuration
    print("\n" + "="*60)
    print("Step 3: Update Configuration")
    print("="*60)
    update_config()
    
    # Step 6: Run migration
    print("\n" + "="*60)
    print("Step 4: Migrate Data")
    print("="*60)
    if input("\nRun data migration? (y/n): ").lower() == 'y':
        if not run_migration():
            print("\n❌ Migration failed")
            return False
    
    # Success!
    print("\n" + "="*70)
    print(" "*20 + "✅ SETUP COMPLETED!")
    print("="*70)
    print("\n📋 Next Steps:")
    print("1. Review migration log file")
    print("2. Test application: python app.py")
    print("3. Verify all features are working")
    print("4. Keep SQLite backups for rollback if needed")
    print("\n📖 For detailed information, see: POSTGRESQL_MIGRATION_GUIDE.md")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if success:
            sys.exit(0)
        else:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
