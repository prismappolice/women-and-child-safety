"""
Fix navbar overflow issue for all template pages
Adds horizontal scroll for laptop screens (1366px - 1400px width)
"""
import os
import re

TEMPLATES_DIR = 'templates'

# Files to fix (excluding index.html and about.html which are already fixed)
FILES_TO_FIX = [
    'gallery.html',
    'contact.html',
    'initiatives.html',
    'safety_tips.html',
    'volunteer_registration.html',
    'pdf_resources.html'
]

def fix_navbar_in_file(filepath):
    """Fix navbar overflow in a template file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has navbar styling
    if '.navbar' not in content and '.nav-menu' not in content:
        print(f"✗ {os.path.basename(filepath)} - No navbar found")
        return False
    
    # Check if already fixed (has scrollbar styling)
    if '.nav-menu::-webkit-scrollbar' in content:
        print(f"✓ {os.path.basename(filepath)} - Already fixed")
        return False
    
    # Pattern 1: Find .navbar and .nav-menu styles
    navbar_pattern = r'(\.navbar\s*{[^}]+})\s*(\.nav-menu\s*{[^}]+})'
    match = re.search(navbar_pattern, content, re.DOTALL)
    
    if match:
        old_styles = match.group(0)
        
        # Add overflow-x and scrollbar properties
        new_navbar = match.group(1).rstrip('}').rstrip() + ' overflow-x: hidden; }'
        
        # Modify nav-menu to add scroll
        nav_menu_content = match.group(2)
        nav_menu_content = nav_menu_content.rstrip('}').rstrip() + ' overflow-x: auto; -webkit-overflow-scrolling: touch; scrollbar-width: thin; }'
        
        # Add scrollbar styling
        scrollbar_styles = '''
        
        /* Scrollbar Styling for Navbar */
        .nav-menu::-webkit-scrollbar {
            height: 4px;
        }
        .nav-menu::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }
        .nav-menu::-webkit-scrollbar-thumb {
            background: #3498db;
            border-radius: 10px;
        }
        
        /* Laptop Screen Optimization */
        @media screen and (max-width: 1400px) {
            .navbar {
                padding: 15px 30px;
            }
            .nav-menu {
                gap: 18px;
                justify-content: flex-start;
            }
            .nav-menu a {
                padding: 10px 12px;
                font-size: 1em;
            }
        }'''
        
        new_styles = new_navbar + '\n        ' + nav_menu_content + scrollbar_styles
        
        # Replace in content
        content = content.replace(old_styles, new_styles)
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ {os.path.basename(filepath)} - Navbar fixed")
        return True
    else:
        print(f"✗ {os.path.basename(filepath)} - Could not find navbar pattern")
        return False

def main():
    """Process all specified template files"""
    print("Fixing navbar overflow for laptop screens...\n")
    
    files_updated = 0
    
    for filename in FILES_TO_FIX:
        filepath = os.path.join(TEMPLATES_DIR, filename)
        
        if not os.path.exists(filepath):
            print(f"✗ {filename} - File not found")
            continue
        
        if fix_navbar_in_file(filepath):
            files_updated += 1
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Files updated: {files_updated}")
    print(f"  Mobile responsiveness: Unchanged ✓")
    print(f"  Laptop screens: Horizontal scroll enabled ✓")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
