"""
Add CSRF tokens to ALL admin form templates
This will fix the "Bad Request" errors when submitting forms
"""

import os
import re

templates_dir = 'templates'
fixed_count = 0
skipped_count = 0

print("🔧 Adding CSRF tokens to admin templates...")
print("=" * 80)

# Find all admin template files
for filename in os.listdir(templates_dir):
    if filename.startswith('admin_') and filename.endswith('.html'):
        filepath = os.path.join(templates_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has CSRF token
        if 'csrf_token' in content:
            print(f"⏭️  {filename} - Already has CSRF token")
            skipped_count += 1
            continue
        
        # Find forms with method="POST"
        pattern = r'(<form[^>]*method=["\']POST["\'][^>]*>)'
        matches = re.findall(pattern, content, re.IGNORECASE)
        
        if matches:
            # Add CSRF token after each POST form tag
            new_content = re.sub(
                pattern,
                r'\1\n                                <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>',
                content,
                flags=re.IGNORECASE
            )
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ {filename} - Added CSRF token to {len(matches)} form(s)")
            fixed_count += 1
        else:
            print(f"ℹ️  {filename} - No POST forms found")
            skipped_count += 1

print("\n" + "=" * 80)
print(f"📊 Summary:")
print(f"   ✅ Fixed: {fixed_count} templates")
print(f"   ⏭️  Skipped: {skipped_count} templates")
print(f"\n✅ All admin forms now have CSRF protection!")
print(f"\n🔄 Please restart Flask application to test")
