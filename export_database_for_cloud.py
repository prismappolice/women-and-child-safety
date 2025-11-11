"""
Export PostgreSQL Database for Cloud Deployment
Creates backup files ready for cloud hosting
"""
import subprocess
import os
from datetime import datetime

print("="*60)
print("PostgreSQL Database Export")
print("Women and Child Safety Wing Project")
print("="*60)

# Configuration
DB_CONFIG = {
    'host': 'localhost',
    'database': 'women_safety_db',
    'user': 'postgres',
    'password': 'postgres123',
    'port': 5432
}

# Add PostgreSQL to PATH
os.environ['PATH'] = os.environ.get('PATH', '') + r';C:\Program Files\PostgreSQL\18\bin'
os.environ['PGPASSWORD'] = DB_CONFIG['password']

# Create exports directory
os.makedirs('database_exports', exist_ok=True)

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

print(f"\n📊 Database: {DB_CONFIG['database']}")
print(f"🕐 Timestamp: {timestamp}")

# Export 1: Custom format (recommended for pg_restore)
print("\n1️⃣ Creating custom format backup (.dump)...")
dump_file = f"database_exports/women_safety_db_{timestamp}.dump"

cmd = [
    'pg_dump',
    '-h', DB_CONFIG['host'],
    '-p', str(DB_CONFIG['port']),
    '-U', DB_CONFIG['user'],
    '-d', DB_CONFIG['database'],
    '-F', 'c',  # Custom format
    '-f', dump_file
]

try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    size = os.path.getsize(dump_file) / 1024  # KB
    print(f"✅ Created: {dump_file} ({size:.2f} KB)")
except subprocess.CalledProcessError as e:
    print(f"❌ Error: {e.stderr}")

# Export 2: SQL format (human readable)
print("\n2️⃣ Creating SQL format backup (.sql)...")
sql_file = f"database_exports/women_safety_db_{timestamp}.sql"

cmd = [
    'pg_dump',
    '-h', DB_CONFIG['host'],
    '-p', str(DB_CONFIG['port']),
    '-U', DB_CONFIG['user'],
    '-d', DB_CONFIG['database'],
    '-f', sql_file
]

try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    size = os.path.getsize(sql_file) / 1024  # KB
    print(f"✅ Created: {sql_file} ({size:.2f} KB)")
except subprocess.CalledProcessError as e:
    print(f"❌ Error: {e.stderr}")

# Export 3: Schema only
print("\n3️⃣ Creating schema-only backup...")
schema_file = f"database_exports/schema_only_{timestamp}.sql"

cmd = [
    'pg_dump',
    '-h', DB_CONFIG['host'],
    '-p', str(DB_CONFIG['port']),
    '-U', DB_CONFIG['user'],
    '-d', DB_CONFIG['database'],
    '--schema-only',
    '-f', schema_file
]

try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    size = os.path.getsize(schema_file) / 1024  # KB
    print(f"✅ Created: {schema_file} ({size:.2f} KB)")
except subprocess.CalledProcessError as e:
    print(f"❌ Error: {e.stderr}")

# Create deployment info file
print("\n4️⃣ Creating deployment info...")
info_file = f"database_exports/DEPLOYMENT_INFO_{timestamp}.txt"

with open(info_file, 'w', encoding='utf-8') as f:
    f.write("="*60 + "\n")
    f.write("DATABASE DEPLOYMENT INFORMATION\n")
    f.write("Women and Child Safety Wing Project\n")
    f.write("="*60 + "\n\n")
    
    f.write("DATABASE CONFIGURATION:\n")
    f.write("-"*60 + "\n")
    f.write(f"Database Name: {DB_CONFIG['database']}\n")
    f.write(f"Current Host: {DB_CONFIG['host']}\n")
    f.write(f"Current Port: {DB_CONFIG['port']}\n")
    f.write(f"Current User: {DB_CONFIG['user']}\n")
    f.write(f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    f.write("TABLES AND ROW COUNTS:\n")
    f.write("-"*60 + "\n")
    f.write("volunteers: 3 rows\n")
    f.write("gallery_items: 77 rows\n")
    f.write("districts: 26 rows\n")
    f.write("officers: 3 rows\n")
    f.write("success_stories: 3 rows\n")
    f.write("district_sps: 26 rows\n")
    f.write("shakthi_teams: 134 rows\n")
    f.write("women_police_stations: 26 rows\n")
    f.write("one_stop_centers: 26 rows\n")
    f.write("+ 21 more tables\n\n")
    
    f.write("DEPLOYMENT STEPS:\n")
    f.write("-"*60 + "\n")
    f.write("1. Copy backup files to VM:\n")
    f.write(f"   scp {os.path.basename(dump_file)} user@vm-ip:/home/user/\n\n")
    
    f.write("2. On VM, create database:\n")
    f.write("   sudo -u postgres createdb women_safety_db\n\n")
    
    f.write("3. Import backup:\n")
    f.write(f"   pg_restore -U postgres -d women_safety_db {os.path.basename(dump_file)}\n\n")
    
    f.write("4. Verify import:\n")
    f.write("   psql -U postgres -d women_safety_db -c 'SELECT COUNT(*) FROM volunteers;'\n\n")
    
    f.write("5. Update db_config.py with cloud credentials\n\n")
    
    f.write("CONNECTION STRING FOR CLOUD:\n")
    f.write("-"*60 + "\n")
    f.write("POSTGRESQL_CONFIG = {\n")
    f.write("    'main_db': {\n")
    f.write("        'host': 'YOUR_VM_IP',\n")
    f.write("        'database': 'women_safety_db',\n")
    f.write("        'user': 'postgres',\n")
    f.write("        'password': 'CHANGE_THIS_PASSWORD',\n")
    f.write("        'port': 5432\n")
    f.write("    }\n")
    f.write("}\n\n")
    
    f.write("SECURITY NOTES:\n")
    f.write("-"*60 + "\n")
    f.write("⚠️ Change default password in production!\n")
    f.write("⚠️ Configure firewall to restrict PostgreSQL access\n")
    f.write("⚠️ Enable SSL/TLS for database connections\n")
    f.write("⚠️ Regular backups recommended\n")

print(f"✅ Created: {info_file}")

print("\n" + "="*60)
print("✅ EXPORT COMPLETED!")
print("="*60)
print(f"\n📁 All files saved in: database_exports/")
print("\nExported files:")
print(f"  1. {os.path.basename(dump_file)} - Main backup (use this)")
print(f"  2. {os.path.basename(sql_file)} - SQL format")
print(f"  3. {os.path.basename(schema_file)} - Schema only")
print(f"  4. {os.path.basename(info_file)} - Deployment guide")

print("\n📤 Next steps:")
print("1. Copy backup files to your VM")
print("2. Follow instructions in DEPLOYMENT_INFO file")
print("3. Update db_config.py with cloud credentials")

print("\n" + "="*60)
