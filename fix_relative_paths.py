import os
import re

def update_to_relative_paths(file_path):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update CSS path
    content = content.replace('href="/static/', 'href="static/')
    
    # Update image paths
    content = content.replace('src="/static/', 'src="static/')
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print("Updated all paths to relative paths!")

if __name__ == "__main__":
    file_path = os.path.join('templates', 'index.html')
    update_to_relative_paths(file_path)
