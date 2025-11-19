# 🚀 Render Deployment Checklist
**Date:** November 19, 2025

---

## ✅ PRE-DEPLOYMENT TASKS

### 1. Local Preparation
- [ ] Updated requirements.txt with psycopg2-binary and python-dotenv
- [ ] Created Procfile for Gunicorn
- [ ] Updated app.py with PORT configuration
- [ ] Tested application locally
- [ ] All features working (admin login, OTP, gallery, etc.)

### 2. Database Backup
- [ ] Run: `python export_database_for_render.py`
- [ ] Backup file created: `render_backup_YYYYMMDD_HHMMSS.sql`
- [ ] Verified backup file size (check it's not empty)
- [ ] Noted backup filename for later use

### 3. Code Repository
- [ ] Code pushed to GitHub
- [ ] Repository: `bujji584/women-and-child-safety-wing`
- [ ] Branch: `main`
- [ ] All files committed

---

## 🎯 RENDER SETUP TASKS

### 4. Create PostgreSQL Database
- [ ] Login to Render: https://dashboard.render.com/
- [ ] Click "New +" → PostgreSQL
- [ ] Database name: `women-safety-db`
- [ ] Region: Singapore
- [ ] Plan: Free (or paid)
- [ ] Database status: **Available** ✅
- [ ] Noted connection details:
  ```
  Internal Host: _____________________
  Database: _____________________
  User: _____________________
  Password: _____________________
  ```

### 5. Restore Database
- [ ] Downloaded backup file to local machine
- [ ] Connected using PSQL command from Render
- [ ] Restored backup: `psql -h <host> -U <user> -d <db> -f backup.sql`
- [ ] Verified tables exist: `\dt`
- [ ] Checked row counts:
  - [ ] volunteers: _____ rows
  - [ ] gallery_items: _____ rows
  - [ ] districts: _____ rows
  - [ ] admin_credentials: _____ rows

### 6. Create Web Service
- [ ] Click "New +" → Web Service
- [ ] Connected GitHub repository
- [ ] Selected branch: `main`
- [ ] Configured:
  - [ ] Name: `women-safety-app`
  - [ ] Region: Singapore
  - [ ] Runtime: Python 3
  - [ ] Build Command: `pip install -r requirements.txt`
  - [ ] Start Command: `gunicorn app:app`
  - [ ] Instance Type: Free (or paid)

### 7. Environment Variables
Added all variables from `.env.render.template`:

**Database:**
- [ ] DB_MODE=postgresql
- [ ] PG_HOST (Internal URL)
- [ ] PG_DATABASE
- [ ] PG_USER
- [ ] PG_PASSWORD
- [ ] PG_PORT=5432
- [ ] PG_ADMIN_HOST (same as PG_HOST)
- [ ] PG_ADMIN_DATABASE (same as PG_DATABASE)
- [ ] PG_ADMIN_USER (same as PG_USER)
- [ ] PG_ADMIN_PASSWORD (same as PG_PASSWORD)
- [ ] PG_ADMIN_PORT=5432

**Email:**
- [ ] MAIL_SERVER=smtp.gmail.com
- [ ] MAIL_PORT=587
- [ ] MAIL_USERNAME=meta1.aihackathon@gmail.com
- [ ] MAIL_PASSWORD=hgsqrgfhuvqczvaa

**Flask:**
- [ ] FLASK_ENV=production
- [ ] SECRET_KEY (generated random 64-char hex)
- [ ] PYTHON_VERSION=3.11.0

---

## 🔍 DEPLOYMENT VERIFICATION

### 8. Build Status
- [ ] Build started automatically
- [ ] Build completed successfully (no errors)
- [ ] Service status: **Live** ✅
- [ ] URL generated: `https://________.onrender.com`

### 9. Application Testing
- [ ] Homepage loads: `https://your-app.onrender.com`
- [ ] Admin login page: `/admin-login`
- [ ] Login works with: admin / admin123
- [ ] Dashboard displays
- [ ] Volunteer count shows correct number
- [ ] Gallery images load
- [ ] Districts dropdown populated

### 10. OTP Email Testing
- [ ] Logout from admin
- [ ] Click "Forgot Password?"
- [ ] Enter username: admin
- [ ] OTP sent successfully
- [ ] Received OTP email
- [ ] OTP verification works
- [ ] Password reset successful

### 11. Database Connectivity
- [ ] Admin dashboard shows correct data
- [ ] Gallery items count matches local
- [ ] Volunteer list displays
- [ ] No database errors in logs

### 12. File Uploads
- [ ] Upload new gallery image (test)
- [ ] Image displays correctly
- [ ] Static files loading properly

---

## 📊 POST-DEPLOYMENT

### 13. Monitoring
- [ ] Checked logs for errors
- [ ] No Python exceptions
- [ ] No database connection errors
- [ ] Response times acceptable

### 14. Documentation
- [ ] Noted deployment URL
- [ ] Updated team with new URL
- [ ] Documented any issues found
- [ ] Created incident report (if needed)

### 15. Backup Schedule
- [ ] Set up automated backups on Render
- [ ] Scheduled weekly backups
- [ ] Documented backup restoration process

---

## 🎉 DEPLOYMENT COMPLETE!

**Deployment Date:** _______________  
**Deployed By:** _______________  
**Application URL:** https://________.onrender.com  
**Database:** Render PostgreSQL  
**Status:** ✅ Live

---

## 📞 EMERGENCY CONTACTS

**Render Support:** support@render.com  
**GitHub Issues:** https://github.com/bujji584/women-and-child-safety-wing/issues  

---

## 🔄 ROLLBACK PLAN

If deployment fails:
1. Check logs in Render dashboard
2. Verify environment variables
3. Test database connection
4. Restore previous version from GitHub
5. Contact Render support if needed

---

**Checklist Completed:** [ ] Yes / [ ] No  
**Notes:** _____________________________________
