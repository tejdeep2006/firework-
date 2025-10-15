import re
import os

def fix_file_paths(file_path):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix the CSS link
    content = content.replace(
        '<link rel="stylesheet" href="""/static/css/style.css""">',
        '<link rel="stylesheet" href="/static/css/style.css">'
    )
    
    # Fix the banner image
    content = content.replace(
        '<img src="""/static/images/banner.jpj.png"""',
        '<img src="/static/images/banner.jpj.png"'
    )
    
    # Fix other image paths
    pattern = r'\{\{\s*url_for\([^)]*\)\s*\}\}'
    
    def replace_url_for(match):
        # Extract the filename from the url_for call
        url_match = re.search(r"filename\s*=\s*['\"]([^'\"]+)['\"]", match.group(0))
        if url_match:
            filename = url_match.group(1)
            return f'"/static/{filename}"'
        return match.group(0)
    
    # Replace all url_for patterns
    content = re.sub(pattern, replace_url_for, content)
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print("File paths fixed successfully!")

if __name__ == "__main__":
    file_path = os.path.join('templates', 'index.html')
    fix_file_paths(file_path)
