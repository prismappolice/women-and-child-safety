# 🚀 Complete Render Deployment Guide
## AP Police Women and Child Safety Wing - PostgreSQL Database

---

## 📋 PRE-DEPLOYMENT CHECKLIST

### ✅ Step 1: Verify Requirements.txt
- [x] psycopg2-binary==2.9.9 (Added for PostgreSQL)
- [x] python-dotenv==1.0.0 (Added for environment variables)
- [x] gunicorn==23.0.0 (Already present)
- [x] Flask==3.1.2 (Already present)
- [x] Flask-Mail==0.10.0 (Already present)

### ✅ Step 2: Create Database Backup

```powershell
# Run the export script
python export_database_for_render.py
```

This will create: `render_backup_YYYYMMDD_HHMMSS.sql`

**What gets exported:**
- ✅ All tables with structure
- ✅ All data (volunteers, gallery, districts, etc.)
- ✅ Foreign keys and constraints
- ✅ Sequences (auto-increment values)
- ✅ Indexes

---

## 🎯 RENDER DEPLOYMENT STEPS

### Step 1: Create GitHub Repository (if not done)

```powershell
# Initialize git (if needed)
git init
git add .
git commit -m "Initial commit - Ready for Render deployment"

# Push to GitHub
git remote add origin https://github.com/bujji584/women-and-child-safety-wing.git
git branch -M main
git push -u origin main
```

---

### Step 2: Create PostgreSQL Database on Render

1. **Go to Render Dashboard:** https://dashboard.render.com/
2. **Click "New +"** → Select **"PostgreSQL"**
3. **Fill Details:**
   - Name: `women-safety-db`
   - Database: `women_safety_db` (auto-generated)
   - User: `women_safety_db_user` (auto-generated)
   - Region: Singapore (closest to India)
   - PostgreSQL Version: 16 (latest)
   - Plan: Free (or paid based on your needs)

4. **Click "Create Database"**

5. **Note Down Connection Details:**
   ```
   Internal Database URL: postgres://user:pass@internal-host/db
   External Database URL: postgres://user:pass@external-host/db
   PSQL Command: psql -h host -U user db
   ```

**⏳ Wait for database to be ready (Status: Available)**

---

### Step 3: Restore Database to Render

#### Option A: Using PSQL Command (Recommended)

```powershell
# From Render dashboard, copy the PSQL command
psql -h <render-hostname> -U <render-user> -d <render-database> -f render_backup_YYYYMMDD_HHMMSS.sql

# Example:
psql -h dpg-xxxxx.singapore-postgres.render.com -U women_safety_db_user -d women_safety_db -f render_backup_20251119_120000.sql

# Enter password when prompted (copy from Render dashboard)
```

#### Option B: Using Render Shell (Alternative)

1. Go to Render Dashboard → Your Database → **"Shell"** tab
2. Click **"Launch Shell"**
3. Upload your `.sql` file:
   ```bash
   # In shell, create file and paste content
   nano restore.sql
   # Paste content, Ctrl+X, Y, Enter
   
   # Run restore
   psql $DATABASE_URL -f restore.sql
   ```

#### Verify Restoration:

```sql
-- Connect to database
psql -h <render-hostname> -U <render-user> -d <render-database>

-- Check tables
\dt

-- Check row counts
SELECT COUNT(*) FROM volunteers;
SELECT COUNT(*) FROM gallery_items;
SELECT COUNT(*) FROM districts;
SELECT COUNT(*) FROM admin_credentials;

-- Exit
\q
```

---

### Step 4: Create Web Service on Render

1. **Go to Render Dashboard** → Click **"New +"** → Select **"Web Service"**

2. **Connect GitHub Repository:**
   - Select: `bujji584/women-and-child-safety-wing`
   - Branch: `main`

3. **Configure Service:**
   ```
   Name: women-safety-app
   Region: Singapore
   Branch: main
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   Instance Type: Free (or paid)
   ```

4. **Add Environment Variables:**

   Click **"Advanced"** → **"Add Environment Variable"**

   ```env
   # Database Configuration
   DB_MODE=postgresql
   PG_HOST=<internal-render-host>
   PG_DATABASE=women_safety_db
   PG_USER=women_safety_db_user
   PG_PASSWORD=<render-db-password>
   PG_PORT=5432

   # Admin Database (same as main)
   PG_ADMIN_HOST=<internal-render-host>
   PG_ADMIN_DATABASE=women_safety_db
   PG_ADMIN_USER=women_safety_db_user
   PG_ADMIN_PASSWORD=<render-db-password>
   PG_ADMIN_PORT=5432

   # Email Configuration
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USERNAME=meta1.aihackathon@gmail.com
   MAIL_PASSWORD=hgsqrgfhuvqczvaa

   # Flask Configuration
   FLASK_ENV=production
   SECRET_KEY=<generate-random-32-char-string>

   # Python Configuration
   PYTHON_VERSION=3.11.0
   ```

   **To generate SECRET_KEY:**
   ```python
   import secrets
   print(secrets.token_hex(32))
   ```

5. **Click "Create Web Service"**

---

### Step 5: Monitor Deployment

1. **Watch Build Logs:**
   - Render will show live deployment logs
   - Check for any errors

2. **Common Issues & Fixes:**

   **Issue: Module not found**
   ```
   Fix: Check requirements.txt has all dependencies
   ```

   **Issue: Database connection failed**
   ```
   Fix: Verify environment variables (use Internal Database URL)
   ```

   **Issue: Port binding error**
   ```
   Fix: Ensure app.py uses: app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
   ```

3. **Check Application Status:**
   - Status should show: **"Live"** (green)
   - URL: `https://women-safety-app.onrender.com`

---

### Step 6: Test Deployment

1. **Open Application:**
   ```
   https://your-app-name.onrender.com
   ```

2. **Test Key Features:**
   - ✅ Homepage loads
   - ✅ Admin login: `/admin-login`
   - ✅ Gallery images display
   - ✅ Volunteer registration
   - ✅ Districts dropdown
   - ✅ Forgot password (OTP email)

3. **Test Database:**
   ```
   Login → Admin Dashboard
   Check: Volunteer count, Gallery items, etc.
   All data should match local database
   ```

---

## 🔧 POST-DEPLOYMENT CONFIGURATION

### Update db_config.py (Automatic)

Render will use environment variables automatically. Your `db_config.py` already supports this:

```python
# Reads from environment variables
PG_HOST = os.getenv('PG_HOST', 'localhost')
PG_DATABASE = os.getenv('PG_DATABASE', 'women_safety_db')
PG_USER = os.getenv('PG_USER', 'postgres')
PG_PASSWORD = os.getenv('PG_PASSWORD', 'postgres123')
```

### Update app.py (if needed)

Ensure this line exists:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

---

## 📊 DEPLOYMENT VERIFICATION CHECKLIST

- [ ] Database backup created successfully
- [ ] PostgreSQL database created on Render
- [ ] Database restored with all data
- [ ] Web service deployed successfully
- [ ] Environment variables configured
- [ ] Application shows "Live" status
- [ ] Homepage accessible via URL
- [ ] Admin login working
- [ ] Email OTP sending works
- [ ] All data visible (volunteers, gallery, etc.)
- [ ] File uploads working (test gallery upload)

---

## 🚨 TROUBLESHOOTING

### Issue: Database Connection Error

**Check:**
```python
# In Render shell or logs
echo $PG_HOST
echo $PG_DATABASE
```

**Fix:** Use Internal Database URL, not External

### Issue: Email Not Sending

**Check:**
```env
MAIL_USERNAME=meta1.aihackathon@gmail.com
MAIL_PASSWORD=hgsqrgfhuvqczvaa (no spaces!)
```

### Issue: Static Files Not Loading

**Check app.py:**
```python
app.static_folder = 'static'
app.static_url_path = '/static'
```

### Issue: Build Failed

**Check:**
- requirements.txt has all dependencies
- Python version compatible (3.9+)
- No syntax errors in code

### View Logs:
```
Render Dashboard → Your Service → Logs tab
```

---

## 📞 SUPPORT

**Render Documentation:** https://render.com/docs  
**PostgreSQL Docs:** https://www.postgresql.org/docs/

**Common Commands:**

```powershell
# Check database size
psql -h <host> -U <user> -d <db> -c "SELECT pg_size_pretty(pg_database_size('women_safety_db'));"

# List all tables
psql -h <host> -U <user> -d <db> -c "\dt"

# Backup from Render (download)
pg_dump -h <render-host> -U <user> -d <db> -f backup_from_render.sql
```

---

## ✅ SUCCESS INDICATORS

1. ✅ Render shows: **"Live"** status (green)
2. ✅ URL accessible: `https://your-app.onrender.com`
3. ✅ Admin login works
4. ✅ Database queries return data
5. ✅ No errors in logs
6. ✅ Email OTP sends successfully
7. ✅ File uploads work

---

## 🎉 DEPLOYMENT COMPLETE!

Your application is now live at: `https://your-app-name.onrender.com`

**Next Steps:**
1. Share URL with users
2. Monitor logs for errors
3. Set up custom domain (optional)
4. Configure SSL certificate (automatic on Render)
5. Set up database backups schedule

---

**Deployed By:** GitHub Copilot Assistant  
**Date:** November 19, 2025  
**Version:** PostgreSQL + Email OTP System
