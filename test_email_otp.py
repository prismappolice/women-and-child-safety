"""Quick test for email OTP functionality"""
import sys

print("=" * 60)
print("🧪 EMAIL OTP CONFIGURATION TEST")
print("=" * 60)

# Test 1: Check if Flask-Mail is installed
print("\n1️⃣ Checking Flask-Mail installation...")
try:
    from flask_mail import Mail, Message
    print("   ✅ Flask-Mail installed")
except ImportError:
    print("   ❌ Flask-Mail not installed")
    print("   💡 Run: pip install Flask-Mail")
    sys.exit(1)

# Test 2: Check database connection
print("\n2️⃣ Checking database connection...")
try:
    from db_config import get_db_connection
    conn = get_db_connection('admin')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM admin_credentials')
    count = cursor.fetchone()[0]
    conn.close()
    print(f"   ✅ Database connected ({count} admin(s) found)")
except Exception as e:
    print(f"   ❌ Database error: {e}")
    sys.exit(1)

# Test 3: Check if email_otp table exists
print("\n3️⃣ Checking email_otp table...")
try:
    conn = get_db_connection('admin')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'email_otp'")
    exists = cursor.fetchone()[0] > 0
    conn.close()
    if exists:
        print("   ✅ email_otp table exists")
    else:
        print("   ⚠️ email_otp table not found")
        print("   💡 Run: python app.py (it will create the table)")
except Exception as e:
    print(f"   ⚠️ Could not verify: {e}")

# Test 4: Check admin email configuration
print("\n4️⃣ Checking admin email configuration...")
try:
    conn = get_db_connection('admin')
    cursor = conn.cursor()
    cursor.execute('SELECT username, email FROM admin_credentials WHERE username = %s', ('admin',))
    admin = cursor.fetchone()
    conn.close()
    
    if admin:
        username, email = admin
        if email and '@' in email and email != 'your.email@gmail.com':
            print(f"   ✅ Admin email configured: {email}")
        else:
            print(f"   ⚠️ Admin email not configured properly")
            print(f"   💡 Current: {email}")
            print(f"   💡 Run: python update_admin_email.py")
    else:
        print("   ❌ Admin user not found")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 5: Check email config in app.py
print("\n5️⃣ Checking app.py email configuration...")
try:
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "MAIL_USERNAME = 'your.email@gmail.com'" in content:
        print("   ⚠️ Email config not updated in app.py")
        print("   💡 Update lines around 590:")
        print("      MAIL_USERNAME = 'youremail@gmail.com'")
        print("      MAIL_PASSWORD = 'your-app-password'")
    else:
        print("   ✅ Email config appears to be updated")
        print("   💡 Make sure you used your actual Gmail credentials")
except Exception as e:
    print(f"   ⚠️ Could not check: {e}")

# Summary
print("\n" + "=" * 60)
print("📋 SUMMARY")
print("=" * 60)
print("\n✅ Setup steps to complete:")
print("   1. Get Gmail App Password from Google Account")
print("   2. Update app.py (lines 590-594) with your email/password")
print("   3. Run: python update_admin_email.py")
print("   4. Restart Flask app: python app.py")
print("   5. Test at: http://127.0.0.1:5000/admin-login")
print("\n📖 Full guide: EMAIL_OTP_SETUP.txt")
print("=" * 60)
