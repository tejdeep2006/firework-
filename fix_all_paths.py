import re
import os

def fix_all_paths(file_path):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix the CSS link
    content = content.replace(
        '<link rel="stylesheet" href="{{ url_for(\'static\', filename=\'css/style.css\') }}">',
        '<link rel="stylesheet" href="/static/css/style.css">'
    )
    
    # Fix the banner image
    content = content.replace(
        '<img src="{{ url_for(\'static\', filename=\'images/banner.jpj.png\') }}"',
        '<img src="/static/images/banner.jpj.png"'
    )
    
    # Fix all other image paths
    pattern = r'\{\{\s*url_for\(\s*[\'\"]static[\'\"]\s*,\s*filename\s*=\s*[\'\"]([^\'\"]+)[\'\"]\s*\)\s*\}\}'
    
    def replace_url_for(match):
        filename = match.group(1)
        return f'"/static/{filename}"'
    
    # Replace all url_for patterns
    content = re.sub(pattern, replace_url_for, content)
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print("All paths updated successfully!")

if __name__ == "__main__":
    file_path = os.path.join('templates', 'index.html')
    fix_all_paths(file_path)
