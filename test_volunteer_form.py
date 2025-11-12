"""
Test Volunteer Registration - Check fixes
"""

import requests
from bs4 import BeautifulSoup

print("🧪 Testing Volunteer Registration Form...")
print("=" * 60)

# Test 1: Check if form loads and CSRF token is present
print("\n1️⃣ Testing form load and CSRF token...")
try:
    response = requests.get('http://127.0.0.1:5000/volunteer-registration')
    if response.status_code == 200:
        print("✅ Form page loads successfully")
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check for CSRF token
        csrf_input = soup.find('input', {'name': 'csrf_token'})
        if csrf_input:
            csrf_token = csrf_input.get('value')
            print(f"✅ CSRF token found: {csrf_token[:20]}...")
        else:
            print("❌ CSRF token NOT found in form!")
    else:
        print(f"❌ Form page returned status code: {response.status_code}")
except Exception as e:
    print(f"❌ Error loading form: {e}")

# Test 2: Test form submission with CSRF token
print("\n2️⃣ Testing form submission...")
try:
    # Get a fresh session and CSRF token
    session = requests.Session()
    response = session.get('http://127.0.0.1:5000/volunteer-registration')
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
    
    # Submit test data
    test_data = {
        'csrf_token': csrf_token,
        'name': 'Test Volunteer',
        'email': 'test@example.com',
        'phone': '9876543210',
        'age': '25',
        'address': 'Test Address, Visakhapatnam',
        'occupation': 'Student',
        'education': 'Bachelor\'s Degree',
        'experience': 'First time volunteer',
        'motivation': 'Want to help make communities safer',
        'availability': 'Weekends',
        'skills': 'Communication, First Aid'
    }
    
    response = session.post(
        'http://127.0.0.1:5000/volunteer-registration',
        data=test_data,
        allow_redirects=False
    )
    
    if response.status_code in [200, 302]:
        if response.status_code == 302:
            print("✅ Form submitted successfully (redirected)")
        else:
            print("✅ Form processed (status 200)")
            
        # Check for error messages
        if 'csrf' in response.text.lower() or 'token' in response.text.lower():
            print("⚠️  Response contains CSRF/token references - check for errors")
        else:
            print("✅ No CSRF errors detected")
    else:
        print(f"❌ Form submission failed with status: {response.status_code}")
        
except Exception as e:
    print(f"❌ Error during form submission: {e}")

print("\n" + "=" * 60)
print("📋 Test Summary:")
print("- Form should load without CSRF errors")
print("- CSRF token should be present in form")
print("- Form submission should work with valid CSRF token")
print("\n💡 If you still see CSRF errors:")
print("1. Clear browser cookies/cache")
print("2. Try in incognito/private mode")
print("3. Restart Flask application")
print("4. Check browser console for errors")
