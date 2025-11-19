"""
Email service with multiple providers (Gmail SMTP and SendGrid)
Automatically falls back to SendGrid if Gmail fails on Render
"""
import os
from flask_mail import Message
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_with_fallback(mail, subject, recipient, body_html):
    """
    Try sending email with Flask-Mail (Gmail SMTP) first
    If it fails (timeout on Render), fall back to SendGrid API
    
    Args:
        mail: Flask-Mail instance
        subject: Email subject
        recipient: Recipient email address
        body_html: HTML body content
        
    Returns:
        tuple: (success: bool, error_message: str or None)
    """
    
    # Try Flask-Mail (Gmail SMTP) first
    try:
        msg = Message(subject, recipients=[recipient])
        msg.html = body_html
        
        # Set timeout to fail fast (5 seconds)
        mail.connect(timeout=5)
        mail.send(msg)
        return (True, None)
    except Exception as smtp_error:
        print(f"⚠️ Gmail SMTP failed: {smtp_error}")
        print("🔄 Falling back to SendGrid...")
        
        # Fall back to SendGrid
        try:
            from sendgrid import SendGridAPIClient
            from sendgrid.helpers.mail import Mail as SendGridMail
            
            # Get SendGrid API key from environment
            sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
            
            if not sendgrid_api_key:
                return (False, "SendGrid API key not configured. Please set SENDGRID_API_KEY environment variable.")
            
            # Create SendGrid message
            sendgrid_msg = SendGridMail(
                from_email=os.environ.get('MAIL_USERNAME', 'meta1.aihackathon@gmail.com'),
                to_emails=recipient,
                subject=subject,
                html_content=body_html
            )
            
            # Send via SendGrid API
            sg = SendGridAPIClient(sendgrid_api_key)
            response = sg.send(sendgrid_msg)
            
            print(f"✅ SendGrid email sent! Status: {response.status_code}")
            return (True, None)
            
        except Exception as sendgrid_error:
            error_msg = f"Both Gmail and SendGrid failed. Gmail: {smtp_error}, SendGrid: {sendgrid_error}"
            print(f"❌ {error_msg}")
            return (False, error_msg)


def send_otp_email_safe(mail, recipient_email, otp_code):
    """
    Send OTP email with automatic fallback
    
    Args:
        mail: Flask-Mail instance
        recipient_email: Recipient email
        otp_code: 6-digit OTP code
        
    Returns:
        tuple: (success: bool, error_message: str or None)
    """
    
    subject = "Password Reset OTP - AP Women Safety"
    
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                       color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
            .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }}
            .otp-box {{ background: white; border: 2px dashed #667eea; padding: 20px; 
                        text-align: center; font-size: 32px; font-weight: bold; 
                        letter-spacing: 5px; margin: 20px 0; border-radius: 5px; color: #667eea; }}
            .footer {{ text-align: center; margin-top: 20px; color: #666; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🔐 Password Reset Request</h1>
            </div>
            <div class="content">
                <p>Hello Admin,</p>
                <p>You have requested to reset your password for the <strong>AP Women & Child Safety Admin Panel</strong>.</p>
                <p>Your One-Time Password (OTP) is:</p>
                <div class="otp-box">{otp_code}</div>
                <p><strong>⏰ This OTP is valid for 10 minutes only.</strong></p>
                <p>If you did not request this password reset, please ignore this email or contact support immediately.</p>
                <p>For security reasons, never share this OTP with anyone.</p>
            </div>
            <div class="footer">
                <p>© 2025 Andhra Pradesh Women & Child Safety Department</p>
                <p>This is an automated email. Please do not reply.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return send_email_with_fallback(mail, subject, recipient_email, html_body)
