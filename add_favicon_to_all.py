"""
Add favicon link to all HTML template files that don't have it
"""
import os
import re

# Path to templates directory
TEMPLATES_DIR = 'templates'

# Favicon link to add
FAVICON_LINK = '    <link rel="icon" type="image/png" href="{{ url_for(\'static\', filename=\'favicon.png\') }}">\n'

def add_favicon_to_file(filepath):
    """Add favicon link to an HTML file if it doesn't have one"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if favicon already exists
    if 'favicon' in content.lower():
        print(f"✓ {os.path.basename(filepath)} - Already has favicon")
        return False
    
    # Check if file has a <head> section
    if '<head>' not in content:
        print(f"✗ {os.path.basename(filepath)} - No <head> tag found")
        return False
    
    # Find the <title> tag and add favicon after it
    title_pattern = r'(<title>.*?</title>)'
    match = re.search(title_pattern, content, re.DOTALL)
    
    if match:
        # Insert favicon after title tag
        title_end = match.end()
        new_content = content[:title_end] + '\n' + FAVICON_LINK + content[title_end:]
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ {os.path.basename(filepath)} - Favicon added")
        return True
    else:
        print(f"✗ {os.path.basename(filepath)} - No <title> tag found")
        return False

def main():
    """Process all HTML files in templates directory"""
    if not os.path.exists(TEMPLATES_DIR):
        print(f"Error: {TEMPLATES_DIR} directory not found!")
        return
    
    print("Adding favicon to all HTML template files...\n")
    
    files_processed = 0
    files_updated = 0
    
    # Process all HTML files
    for filename in os.listdir(TEMPLATES_DIR):
        if filename.endswith('.html'):
            filepath = os.path.join(TEMPLATES_DIR, filename)
            files_processed += 1
            
            if add_favicon_to_file(filepath):
                files_updated += 1
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Total files processed: {files_processed}")
    print(f"  Files updated: {files_updated}")
    print(f"  Files skipped (already had favicon): {files_processed - files_updated}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
