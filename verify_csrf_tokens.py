"""
Quick verification script to check CSRF tokens in slideshow templates
"""

def check_csrf_tokens():
    print("=" * 60)
    print("🔍 CSRF Token Verification")
    print("=" * 60)
    
    templates = {
        'admin_add_slideshow.html': 'templates/admin_add_slideshow.html',
        'admin_edit_slideshow.html': 'templates/admin_edit_slideshow.html',
        'admin_slideshow.html': 'templates/admin_slideshow.html'
    }
    
    all_good = True
    
    for name, path in templates.items():
        print(f"\n📄 {name}")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Count forms
            form_count = content.count('<form')
            print(f"   Forms found: {form_count}")
            
            # Count CSRF tokens
            csrf_count = content.count('csrf_token')
            print(f"   CSRF tokens found: {csrf_count}")
            
            if form_count == csrf_count and form_count > 0:
                print(f"   ✅ All forms have CSRF protection")
            elif form_count > csrf_count:
                print(f"   ❌ Missing CSRF tokens! {form_count - csrf_count} form(s) without protection")
                all_good = False
            else:
                print(f"   ✅ CSRF tokens present")
                
        except Exception as e:
            print(f"   ❌ Error reading file: {e}")
            all_good = False
    
    print("\n" + "=" * 60)
    if all_good:
        print("✅ ALL SLIDESHOW FORMS HAVE CSRF PROTECTION")
        print("\n🎯 You can now:")
        print("   1. Login at http://127.0.0.1:5000/admin-login")
        print("   2. Click 'Slideshow' button")
        print("   3. Add/Edit/Delete slides without CSRF errors")
    else:
        print("❌ SOME FORMS STILL MISSING CSRF TOKENS")
    print("=" * 60)

if __name__ == "__main__":
    check_csrf_tokens()
