"""Update admin email for OTP testing"""
from db_config import get_db_connection

def update_admin_email():
    email = input("Enter admin email address: ").strip()
    
    if not email or '@' not in email:
        print("❌ Invalid email address")
        return
    
    try:
        conn = get_db_connection('admin')
        cursor = conn.cursor()
        
        cursor.execute('UPDATE admin_credentials SET email = %s WHERE username = %s', 
                      (email, 'admin'))
        conn.commit()
        
        # Verify update
        cursor.execute('SELECT username, email FROM admin_credentials WHERE username = %s', ('admin',))
        admin = cursor.fetchone()
        conn.close()
        
        if admin:
            print(f"\n✅ Admin email updated successfully!")
            print(f"   Username: {admin[0]}")
            print(f"   Email: {admin[1]}")
        else:
            print("❌ Admin user not found")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    print("🔧 Update Admin Email for OTP Testing")
    print("=" * 50)
    update_admin_email()
