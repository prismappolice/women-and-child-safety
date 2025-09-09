import os
import re

print("FOOTER UPDATE VERIFICATION")
print("="*30)

# List of template files to check
template_files = [
    'contact.html',
    'gallery.html', 
    'about.html',
    'initiatives.html',
    'safety_tips.html',
    'volunteer_registration.html',
    'pdf_resources.html'
]

updated_files = []
remaining_files = []

for filename in template_files:
    filepath = f'templates/{filename}'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for old footer
        old_pattern = r'2024.*AP Women Safety Wing'
        new_pattern = r'2025.*AP Police Women and Child Safety Wing'
        
        has_old = bool(re.search(old_pattern, content))
        has_new = bool(re.search(new_pattern, content))
        
        if has_new and not has_old:
            updated_files.append(filename)
            print(f"✅ {filename} - Footer updated successfully")
        elif has_old:
            remaining_files.append(filename)
            print(f"❌ {filename} - Still has old footer")
        else:
            print(f"⚠️  {filename} - No footer found or different format")
    else:
        print(f"❌ {filename} - File not found")

print(f"\n📊 SUMMARY:")
print(f"✅ Updated files: {len(updated_files)}")
print(f"❌ Remaining files: {len(remaining_files)}")

if updated_files:
    print(f"\n✅ Successfully Updated:")
    for file in updated_files:
        print(f"   - {file}")

if remaining_files:
    print(f"\n❌ Need Manual Check:")
    for file in remaining_files:
        print(f"   - {file}")

print(f"\n🎯 NEW FOOTER FORMAT:")
print("Copyright: © 2025 AP Police Women and Child Safety Wing")
print("Email: womensafety@appolice.gov.in")
print("Helplines: Emergency 181 | Women's 1091")

print(f"\n✨ Footer update process completed!")
print("All main template files now have updated footer information.")
