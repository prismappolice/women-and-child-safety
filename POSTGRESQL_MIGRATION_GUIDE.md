# PostgreSQL Migration Guide
## Women and Child Safety Wing Project

**Date**: November 11, 2025  
**Migration Type**: SQLite → PostgreSQL  
**Status**: Ready for Execution

---

## 📋 PRE-MIGRATION CHECKLIST

### ✅ Completed Steps:
1. ✅ **Database Backups Created**
   - `women_safety_backup_YYYYMMDD_HHMMSS.db`
   - `database_backup_YYYYMMDD_HHMMSS.db`
   - `volunteer_system_backup_YYYYMMDD_HHMMSS.db`

2. ✅ **Migration Scripts Created**
   - `postgresql_schema.sql` - Main database schema
   - `postgresql_admin_schema.sql` - Admin database schema
   - `migrate_to_postgresql.py` - Data migration script
   - `db_config.py` - Database abstraction layer

3. ✅ **Requirements Updated**
   - Added `psycopg2-binary==2.9.9` to requirements.txt

---

## 🚀 MIGRATION STEPS

### Step 1: Install PostgreSQL

**Windows:**
1. Download from: https://www.postgresql.org/download/windows/
2. Run installer (PostgreSQL 15 or 16)
3. Set password for `postgres` user (remember this!)
4. Default port: 5432

**Verify Installation:**
```powershell
psql --version
```

### Step 2: Create PostgreSQL Databases

Open PowerShell as Administrator and run:

```powershell
# Connect to PostgreSQL
psql -U postgres

# In psql prompt:
CREATE DATABASE women_safety;
CREATE DATABASE admin_db;

# Verify databases
\l

# Exit
\q
```

### Step 3: Create Database Schemas

```powershell
cd "e:\final ap women safety"

# Create main database schema
psql -U postgres -d women_safety -f postgresql_schema.sql

# Create admin database schema
psql -U postgres -d admin_db -f postgresql_admin_schema.sql
```

**Expected Output:**
- CREATE TABLE messages for all 28+ tables
- CREATE INDEX messages
- No error messages

### Step 4: Install Python Dependencies

```powershell
cd "e:\final ap women safety"
pip install psycopg2-binary
```

### Step 5: Update Migration Script Configuration

Edit `migrate_to_postgresql.py` (lines 14-25):

```python
PG_CONFIG = {
    'host': 'localhost',
    'database': 'women_safety',
    'user': 'postgres',
    'password': 'YOUR_ACTUAL_PASSWORD',  # ← Change this!
    'port': 5432
}

PG_ADMIN_CONFIG = {
    'host': 'localhost',
    'database': 'admin_db',
    'user': 'postgres',
    'password': 'YOUR_ACTUAL_PASSWORD',  # ← Change this!
    'port': 5432
}
```

### Step 6: Run Data Migration

```powershell
cd "e:\final ap women safety"
python migrate_to_postgresql.py
```

**Expected Output:**
```
==============================================================
PostgreSQL Migration Tool
Women and Child Safety Wing Project
==============================================================

⚠️  IMPORTANT: Before running this script:
...

Press Enter to continue or Ctrl+C to cancel...

[YYYY-MM-DD HH:MM:SS] POSTGRESQL MIGRATION STARTED
[YYYY-MM-DD HH:MM:SS] ✅ Connected to PostgreSQL: women_safety
[YYYY-MM-DD HH:MM:SS] ✅ Connected to SQLite: women_safety.db
[YYYY-MM-DD HH:MM:SS] ✅ Migrated 77 rows to 'gallery_items'
[YYYY-MM-DD HH:MM:SS] ✅ Migrated 3 rows to 'volunteers'
...
[YYYY-MM-DD HH:MM:SS] 🎉 MIGRATION COMPLETED SUCCESSFULLY!
```

**Migration Log**: A detailed log file will be created: `migration_log_YYYYMMDD_HHMMSS.txt`

### Step 7: Update db_config.py

Edit `db_config.py` (lines 24-34) with your PostgreSQL password:

```python
POSTGRESQL_CONFIG = {
    'main_db': {
        'host': 'localhost',
        'database': 'women_safety',
        'user': 'postgres',
        'password': 'YOUR_ACTUAL_PASSWORD',  # ← Change this!
        'port': 5432
    },
    'admin_db': {
        'host': 'localhost',
        'database': 'admin_db',
        'user': 'postgres',
        'password': 'YOUR_ACTUAL_PASSWORD',  # ← Change this!
        'port': 5432
    }
}
```

---

## 🔧 CODE UPDATES (Automatic via db_config.py)

The `db_config.py` module provides database abstraction, so minimal code changes are needed.

### Key Functions:
- `get_db_connection('main')` - Get main database connection
- `get_db_connection('admin')` - Get admin database connection
- `adapt_query(query)` - Converts SQLite queries to PostgreSQL
- `execute_query()` - Execute queries with proper parameter binding

### Environment Variable (Optional):
```powershell
# Switch to PostgreSQL mode
$env:DB_MODE = "postgresql"

# Switch back to SQLite (for testing)
$env:DB_MODE = "sqlite"
```

---

## ✅ TESTING CHECKLIST

After migration, test these features:

### 1. Admin Features
- [ ] Login with username/password
- [ ] Change password functionality
- [ ] Security questions setup
- [ ] Forgot password recovery
- [ ] Session timeout (15 minutes)

### 2. Content Management
- [ ] Add/Edit/Delete gallery items
- [ ] Upload images (check file paths)
- [ ] Add/Edit officers
- [ ] Add/Edit success stories
- [ ] Add/Edit initiatives
- [ ] Add/Edit safety tips
- [ ] Upload PDF resources

### 3. Volunteer System
- [ ] Volunteer registration
- [ ] Auto-generate registration ID (VOL-2025-XXXX)
- [ ] Check volunteer status by ID
- [ ] Check volunteer status by phone
- [ ] Admin: Approve/Reject volunteers
- [ ] Admin: Send email notifications

### 4. District Management
- [ ] View all 26 districts
- [ ] Add/Edit district SPs
- [ ] Add/Edit Shakthi teams
- [ ] Add/Edit Women Police Stations
- [ ] Add/Edit One Stop Centers

### 5. Public Pages
- [ ] Home page loads correctly
- [ ] About page displays content
- [ ] Contact page shows district info
- [ ] Gallery displays images/videos
- [ ] Initiatives page
- [ ] Safety tips page
- [ ] PDF resources downloadable

---

## 🔍 VERIFICATION QUERIES

Connect to PostgreSQL and verify data:

```sql
-- Connect to database
psql -U postgres -d women_safety

-- Check row counts
SELECT 'volunteers' as table_name, COUNT(*) FROM volunteers
UNION ALL
SELECT 'gallery_items', COUNT(*) FROM gallery_items
UNION ALL
SELECT 'officers', COUNT(*) FROM officers
UNION ALL
SELECT 'districts', COUNT(*) FROM districts
UNION ALL
SELECT 'success_stories', COUNT(*) FROM success_stories;

-- Check volunteer data
SELECT registration_id, name, phone, email 
FROM volunteers 
LIMIT 5;

-- Check admin data (switch to admin_db)
\c admin_db
SELECT username FROM admin_credentials;

-- Check security questions exist
SELECT COUNT(*) FROM admin_security;
```

**Expected Results:**
- Volunteers: 3 rows
- Gallery items: 77 rows
- Officers: (your count)
- Districts: 26 rows
- Admin credentials: 1 row (admin user)

---

## 🔄 ROLLBACK PLAN

If something goes wrong, you can easily revert to SQLite:

### Option 1: Environment Variable
```powershell
# Switch back to SQLite mode
$env:DB_MODE = "sqlite"

# Restart application
python app.py
```

### Option 2: Restore from Backup
```powershell
cd "e:\final ap women safety"

# Find your backup files
Get-ChildItem *_backup_*.db

# Restore (example)
Copy-Item women_safety_backup_20251111_*.db women_safety.db -Force
Copy-Item database_backup_20251111_*.db database.db -Force
Copy-Item volunteer_system_backup_20251111_*.db volunteer_system.db -Force
```

### Option 3: Modify db_config.py
Edit line 8 in `db_config.py`:
```python
DB_MODE = os.getenv('DB_MODE', 'sqlite')  # Change 'postgresql' to 'sqlite'
```

---

## 📊 PERFORMANCE COMPARISON

### SQLite vs PostgreSQL

| Feature | SQLite | PostgreSQL |
|---------|--------|------------|
| Concurrent Users | 1-10 | 100+ |
| Database Size | < 1 GB | Unlimited |
| Backup/Restore | File copy | pg_dump/pg_restore |
| Production Ready | Small sites | Enterprise |
| Horizontal Scaling | ❌ | ✅ |
| ACID Compliance | ✅ | ✅ |
| Full-text Search | Limited | Advanced |
| JSON Support | Basic | Native |

---

## 🎯 POST-MIGRATION OPTIMIZATIONS

### 1. Create Additional Indexes (Optional)
```sql
-- For better search performance
CREATE INDEX idx_volunteers_email ON volunteers(email);
CREATE INDEX idx_success_stories_date ON success_stories(date_occurred);
CREATE INDEX idx_gallery_date ON gallery_items(event_date);
```

### 2. Setup Regular Backups
```powershell
# Create backup script: backup_pg.ps1
pg_dump -U postgres -d women_safety -F c -f "backups/women_safety_$(Get-Date -Format 'yyyyMMdd').backup"
pg_dump -U postgres -d admin_db -F c -f "backups/admin_db_$(Get-Date -Format 'yyyyMMdd').backup"
```

### 3. Connection Pooling (For Production)
Add to `db_config.py`:
```python
from psycopg2 import pool

# Connection pool
pg_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=20,
    **POSTGRESQL_CONFIG['main_db']
)
```

---

## 🚨 TROUBLESHOOTING

### Issue 1: "psycopg2 module not found"
**Solution:**
```powershell
pip install psycopg2-binary
```

### Issue 2: "Connection refused" 
**Solution:**
- Check PostgreSQL service is running
- Verify port 5432 is not blocked
- Check pg_hba.conf for access permissions

```powershell
# Check PostgreSQL status (Windows)
Get-Service -Name postgresql*

# Start if stopped
Start-Service postgresql-x64-15
```

### Issue 3: "relation does not exist"
**Solution:**
- Re-run schema creation scripts
- Ensure you're connected to correct database

```powershell
psql -U postgres -d women_safety -f postgresql_schema.sql
```

### Issue 4: "password authentication failed"
**Solution:**
- Verify password in db_config.py
- Reset PostgreSQL password if needed:
```sql
ALTER USER postgres PASSWORD 'new_password';
```

### Issue 5: Migration script errors
**Solution:**
- Check SQLite databases exist and are readable
- Verify PostgreSQL databases are empty (no conflicting data)
- Review migration log file for specific errors

---

## 📞 SUPPORT & RESOURCES

### PostgreSQL Documentation
- Official Docs: https://www.postgresql.org/docs/
- pgAdmin (GUI Tool): https://www.pgadmin.org/

### Python psycopg2 Documentation
- Official Docs: https://www.psycopg.org/docs/

### Common Commands
```powershell
# Connect to PostgreSQL
psql -U postgres -d women_safety

# List databases
\l

# List tables
\dt

# Describe table
\d table_name

# Exit
\q
```

---

## ✨ BENEFITS AFTER MIGRATION

1. ✅ **Better Performance** - Handles concurrent users efficiently
2. ✅ **Scalability** - Can grow with your data needs
3. ✅ **Production Ready** - Suitable for government deployment
4. ✅ **Advanced Features** - Full-text search, JSON, etc.
5. ✅ **Better Backup** - Professional backup/restore tools
6. ✅ **Data Integrity** - Robust transaction handling
7. ✅ **Hosting Options** - Deploy on AWS, DigitalOcean, Heroku, etc.

---

## 🎉 SUCCESS CRITERIA

Migration is successful when:
- ✅ All data migrated (verified row counts match)
- ✅ Admin login works
- ✅ Volunteer registration works
- ✅ Gallery uploads work
- ✅ All CRUD operations function
- ✅ No errors in application logs
- ✅ Website loads correctly
- ✅ All features tested and working

---

## 📝 NOTES

- **Data Safety**: All original SQLite databases are backed up
- **Rollback**: Can revert to SQLite anytime using environment variable
- **Zero Downtime**: Design and functionality unchanged
- **File Storage**: Images/PDFs remain in `/static/` folder
- **URLs Preserved**: All image/video URLs in database remain valid

---

**Created by**: GitHub Copilot  
**For**: Women and Child Safety Wing Project  
**Date**: November 11, 2025

---

## READY TO PROCEED? ✅

Follow the steps in order. If you encounter any issues, refer to the Troubleshooting section or check the migration log file for details.

**Good luck with your migration! 🚀**
