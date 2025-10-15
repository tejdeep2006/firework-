import re
import os

def update_file_paths(file_path):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace url_for patterns with direct paths
    pattern = r'\{\{\s*url_for\(\s*[\'"]([^\'")]+)[\'"]\s*,\s*filename\s*=\s*[\'"]([^\'")]+)[\'"]\s*\)\s*\}\}'
    
    def replace_match(match):
        # Extract the static path and filename
        static_part = match.group(1)
        filename = match.group(2)
        # Create the direct path
        return f'"/static/{filename}"'
    
    # Perform the replacement
    updated_content = re.sub(pattern, replace_match, content)
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

if __name__ == "__main__":
    # Path to your index.html file
    file_path = os.path.join('templates', 'index.html')
    update_file_paths(file_path)
    print("File paths updated successfully!")
