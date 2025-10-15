import os
import re
from shutil import copy2

def clean_filename(filename):
    # Remove special characters and replace spaces with hyphens
    clean = re.sub(r'[^\w\s.-]', '', filename)
    clean = re.sub(r'\s+', '-', clean).lower()
    return clean

def update_image_references():
    # Path to your static/images directory
    image_dir = os.path.join('static', 'images')
    
    # Path to your index.html
    index_path = os.path.join('templates', 'index.html')
    
    # Read the HTML content
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Track renamed files
    renamed = {}
    
    # First, handle files that already have clean names but different cases
    for filename in os.listdir(image_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            clean_name = clean_filename(filename)
            if clean_name != filename:
                # If a file with the clean name already exists, keep the one with better quality
                if os.path.exists(os.path.join(image_dir, clean_name)):
                    # Keep the larger file (assuming better quality)
                    if os.path.getsize(os.path.join(image_dir, filename)) > os.path.getsize(os.path.join(image_dir, clean_name)):
                        os.replace(os.path.join(image_dir, filename), os.path.join(image_dir, clean_name + '.tmp'))
                        os.replace(os.path.join(image_dir, clean_name + '.tmp'), os.path.join(image_dir, clean_name))
                        print(f'Replaced: {clean_name} with higher quality version')
                    else:
                        print(f'Skipped: {filename} - better version exists')
                        os.remove(os.path.join(image_dir, filename))
                else:
                    # Rename to clean name
                    os.rename(os.path.join(image_dir, filename), os.path.join(image_dir, clean_name))
                    renamed[filename] = clean_name
    
    # Update HTML with new filenames
    for old_name, new_name in renamed.items():
        old_path = f'static/images/{old_name}'
        new_path = f'static/images/{new_name}'
        content = content.replace(old_path, new_path)
        print(f'Updated reference: {old_name} -> {new_name}')
    
    # Save the updated HTML
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\nImage standardization complete!")

if __name__ == "__main__":
    update_image_references()
