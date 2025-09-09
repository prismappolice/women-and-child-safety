import re

print("UPDATING GALLERY TEMPLATE FOR LOCAL VIDEO SUPPORT")
print("="*50)

# Read the current template
with open('templates/gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original template length: {len(content)} characters")

# Define the new video button pattern
old_pattern = r'{% if item\[4\] %}\s*<a href="{{ item\[4\] }}" target="_blank" class="view-btn">\s*<i class="fas fa-play"></i> Watch Video\s*</a>'
new_pattern = '''{% if item[4] %}
                            {% if item[4].startswith('http') %}
                                <a href="{{ item[4] }}" target="_blank" class="view-btn">
                                    <i class="fas fa-play"></i> Watch Video
                                </a>
                            {% else %}
                                <button onclick="playLocalVideo('{{ item[4] }}', '{{ item[1] }}')" class="view-btn" style="border: none; cursor: pointer;">
                                    <i class="fas fa-play"></i> Play Video
                                </button>
                            {% endif %}'''

# Replace all occurrences
updated_content = re.sub(old_pattern, new_pattern, content, flags=re.MULTILINE | re.DOTALL)

# Count replacements made
original_matches = len(re.findall(old_pattern, content, flags=re.MULTILINE | re.DOTALL))
print(f"Found {original_matches} video button patterns to update")

if original_matches > 0:
    # Write the updated content
    with open('templates/gallery.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"✅ Updated {original_matches} video button instances")
    print(f"New template length: {len(updated_content)} characters")
else:
    print("⚠️  No patterns found to replace - manual update needed")

print("\n🎯 Template update complete!")
print("Local videos will now open in modal player")
print("YouTube videos will still open in new tab")
