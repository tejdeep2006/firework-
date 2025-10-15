import os

def clean_paths(file_path):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix double quotes in image paths
    content = content.replace('""/static/', '"/static/')
    
    # Write the cleaned content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print("Paths cleaned successfully!")

if __name__ == "__main__":
    file_path = os.path.join('templates', 'index.html')
    clean_paths(file_path)
