import os

def fix_quotes(file_path):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix double quotes in image paths
    content = content.replace('.jpg""', '.jpg"')
    content = content.replace('.png""', '.png"')
    content = content.replace('.jpeg""', '.jpeg"')
    
    # Write the cleaned content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print("Quotes fixed successfully!")

if __name__ == "__main__":
    file_path = os.path.join('templates', 'index.html')
    fix_quotes(file_path)
