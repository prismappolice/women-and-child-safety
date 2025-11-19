import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def test_gmail_smtp():
    """Test Gmail SMTP connection and email sending"""
    
    # Email configuration from app.py
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'meta1.aihackathon@gmail.com'
    MAIL_PASSWORD = 'hgsqrgfhuvqczvaa'  # Your App Password (no spaces)
    
    print("🔧 Testing Gmail SMTP Configuration")
    print("=" * 50)
    print(f"SMTP Server: {MAIL_SERVER}")
    print(f"SMTP Port: {MAIL_PORT}")
    print(f"Username: {MAIL_USERNAME}")
    print(f"Password: {'*' * len(MAIL_PASSWORD)}")
    print("=" * 50)
    
    try:
        print("\n1️⃣ Connecting to Gmail SMTP server...")
        server = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
        server.set_debuglevel(1)  # Show detailed debug output
        
        print("\n2️⃣ Starting TLS encryption...")
        server.starttls()
        
        print("\n3️⃣ Logging in...")
        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        
        print("\n4️⃣ Preparing test email...")
        msg = MIMEMultipart()
        msg['From'] = MAIL_USERNAME
        msg['To'] = MAIL_USERNAME
        msg['Subject'] = 'Test Email - SHAKTHI Admin OTP System'
        
        body = """
        <html>
        <body>
            <h2>Test Email Successful!</h2>
            <p>Your Gmail SMTP configuration is working correctly.</p>
            <p><strong>OTP System Ready!</strong></p>
        </body>
        </html>
        """
        msg.attach(MIMEText(body, 'html'))
        
        print("\n5️⃣ Sending email...")
        server.send_message(msg)
        
        print("\n6️⃣ Closing connection...")
        server.quit()
        
        print("\n✅ SUCCESS! Email sent successfully!")
        print(f"📧 Check inbox: {MAIL_USERNAME}")
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"\n❌ Authentication Error: {e}")
        print("\n🔧 Possible fixes:")
        print("   1. Check if App Password is correct")
        print("   2. Make sure 2-Step Verification is enabled")
        print("   3. Generate a new App Password")
        
    except smtplib.SMTPException as e:
        print(f"\n❌ SMTP Error: {e}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print(f"Error Type: {type(e).__name__}")

if __name__ == "__main__":
    test_gmail_smtp()
