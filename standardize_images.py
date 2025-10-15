import os
import re

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
    
    # Find all image references in the HTML
    img_pattern = r'src=["\'](static/images/[^"\']+)["\']'
    
    # Track renamed files
    renamed = {}
    
    # Process each image file
    for filename in os.listdir(image_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Clean the filename
            new_name = clean_filename(filename)
            
            # Skip if no change needed
            if new_name == filename:
                continue
                
            # Rename the file
            old_path = os.path.join(image_dir, filename)
            new_path = os.path.join(image_dir, new_name)
            os.rename(old_path, new_path)
            
            # Store the mapping
            renamed[filename] = new_name
    
    # Update HTML with new filenames
    for old_name, new_name in renamed.items():
        old_path = f'static/images/{old_name}'
        new_path = f'static/images/{new_name}'
        content = content.replace(old_path, new_path)
        print(f'Updated: {old_name} -> {new_name}')
    
    # Save the updated HTML
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\nAll image files have been standardized and references updated.")

if __name__ == "__main__":
    update_image_references()
