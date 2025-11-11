"""
Rollback Script - Switch back to SQLite
Use this if you need to revert to SQLite databases
"""

import os
import shutil
from datetime import datetime

def list_backups():
    """List available SQLite backup files"""
    print("\n" + "="*60)
    print("Available SQLite Backups")
    print("="*60)
    
    backups = {
        'main': [],
        'admin': [],
        'volunteer': []
    }
    
    for file in os.listdir('.'):
        if 'women_safety_backup_' in file and file.endswith('.db'):
            backups['main'].append(file)
        elif 'database_backup_' in file and file.endswith('.db'):
            backups['admin'].append(file)
        elif 'volunteer_system_backup_' in file and file.endswith('.db'):
            backups['volunteer'].append(file)
    
    if not any(backups.values()):
        print("⚠️  No backup files found!")
        return None
    
    print("\n📁 Main Database Backups:")
    for i, f in enumerate(sorted(backups['main'], reverse=True), 1):
        size = os.path.getsize(f) / 1024  # KB
        print(f"  {i}. {f} ({size:.2f} KB)")
    
    print("\n📁 Admin Database Backups:")
    for i, f in enumerate(sorted(backups['admin'], reverse=True), 1):
        size = os.path.getsize(f) / 1024  # KB
        print(f"  {i}. {f} ({size:.2f} KB)")
    
    print("\n📁 Volunteer Database Backups:")
    for i, f in enumerate(sorted(backups['volunteer'], reverse=True), 1):
        size = os.path.getsize(f) / 1024  # KB
        print(f"  {i}. {f} ({size:.2f} KB)")
    
    return backups

def restore_from_backup(backups):
    """Restore databases from backup"""
    print("\n" + "="*60)
    print("Restore from Backup")
    print("="*60)
    
    # Get most recent backups
    main_backup = sorted(backups['main'], reverse=True)[0] if backups['main'] else None
    admin_backup = sorted(backups['admin'], reverse=True)[0] if backups['admin'] else None
    volunteer_backup = sorted(backups['volunteer'], reverse=True)[0] if backups['volunteer'] else None
    
    if not all([main_backup, admin_backup, volunteer_backup]):
        print("❌ Missing backup files. Cannot restore.")
        return False
    
    print(f"\n📋 Will restore from:")
    print(f"  Main: {main_backup}")
    print(f"  Admin: {admin_backup}")
    print(f"  Volunteer: {volunteer_backup}")
    
    if input("\nProceed with restore? (yes/no): ").lower() != 'yes':
        print("Restore cancelled")
        return False
    
    try:
        # Backup current databases before restoring
        if os.path.exists('women_safety.db'):
            backup_name = f"women_safety_pre_rollback_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
            shutil.copy2('women_safety.db', backup_name)
            print(f"✅ Current women_safety.db backed up as {backup_name}")
        
        # Restore main database
        shutil.copy2(main_backup, 'women_safety.db')
        print(f"✅ Restored {main_backup} → women_safety.db")
        
        # Restore admin database
        shutil.copy2(admin_backup, 'database.db')
        print(f"✅ Restored {admin_backup} → database.db")
        
        # Restore volunteer database
        shutil.copy2(volunteer_backup, 'volunteer_system.db')
        print(f"✅ Restored {volunteer_backup} → volunteer_system.db")
        
        return True
    
    except Exception as e:
        print(f"❌ Error during restore: {e}")
        return False

def update_db_config():
    """Update db_config.py to use SQLite"""
    print("\n" + "="*60)
    print("Updating Database Configuration")
    print("="*60)
    
    config_file = 'db_config.py'
    
    if not os.path.exists(config_file):
        print(f"⚠️  {config_file} not found. Manual update required.")
        return False
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update DB_MODE to sqlite
        updated = content.replace(
            "DB_MODE = os.getenv('DB_MODE', 'postgresql')",
            "DB_MODE = os.getenv('DB_MODE', 'sqlite')"
        )
        
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(updated)
        
        print(f"✅ Updated {config_file} to use SQLite")
        return True
    
    except Exception as e:
        print(f"❌ Error updating config: {e}")
        return False

def set_environment_variable():
    """Set environment variable to use SQLite"""
    print("\n" + "="*60)
    print("Setting Environment Variable")
    print("="*60)
    
    os.environ['DB_MODE'] = 'sqlite'
    print("✅ Set DB_MODE=sqlite")
    
    print("\n📋 To make this permanent, run in PowerShell:")
    print('   $env:DB_MODE = "sqlite"')
    print("\nOr add to your system environment variables")

def verify_sqlite():
    """Verify SQLite databases exist and are accessible"""
    print("\n" + "="*60)
    print("Verifying SQLite Databases")
    print("="*60)
    
    databases = [
        'women_safety.db',
        'database.db',
        'volunteer_system.db'
    ]
    
    all_ok = True
    for db in databases:
        if os.path.exists(db):
            size = os.path.getsize(db) / 1024  # KB
            print(f"✅ {db} ({size:.2f} KB)")
        else:
            print(f"❌ {db} NOT FOUND")
            all_ok = False
    
    return all_ok

def main():
    """Main rollback process"""
    print("\n" + "="*70)
    print(" "*20 + "PostgreSQL → SQLite Rollback")
    print(" "*15 + "Women and Child Safety Wing Project")
    print("="*70)
    
    print("\n⚠️  WARNING: This will switch your application back to SQLite")
    print("PostgreSQL data will not be affected (remains in PostgreSQL)")
    print("Only the application configuration will be changed")
    
    if input("\nContinue with rollback? (yes/no): ").lower() != 'yes':
        print("\nRollback cancelled")
        return
    
    # Option 1: Check if SQLite databases exist
    print("\n" + "="*60)
    print("Option 1: Use Current SQLite Databases")
    print("="*60)
    
    if verify_sqlite():
        if input("\nUse current SQLite databases? (y/n): ").lower() == 'y':
            update_db_config()
            set_environment_variable()
            print("\n" + "="*70)
            print(" "*25 + "✅ ROLLBACK COMPLETED!")
            print("="*70)
            print("\nYour application is now using SQLite databases")
            print("You can start the application: python app.py")
            return
    
    # Option 2: Restore from backup
    print("\n" + "="*60)
    print("Option 2: Restore from Backup")
    print("="*60)
    
    backups = list_backups()
    if backups:
        if restore_from_backup(backups):
            update_db_config()
            set_environment_variable()
            print("\n" + "="*70)
            print(" "*25 + "✅ ROLLBACK COMPLETED!")
            print("="*70)
            print("\nDatabases restored from backup")
            print("Your application is now using SQLite databases")
            print("You can start the application: python app.py")
            return
    
    print("\n❌ Rollback failed. Please check the errors above.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Rollback cancelled by user")
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
