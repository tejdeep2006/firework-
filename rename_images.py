import os
import re
import shutil

def sanitize_filename(filename):
    # Convert to lowercase
    filename = filename.lower()
    # Replace spaces and special characters with hyphens
    filename = re.sub(r'[^a-z0-9.]+', '-', filename)
    # Remove multiple hyphens
    filename = re.sub(r'-+', '-', filename).strip('-')
    return filename

def rename_images():
    image_dir = os.path.join('static', 'images')
    
    # Create a list of files to rename
    files_to_rename = []
    for filename in os.listdir(image_dir):
        if filename != sanitize_filename(filename):
            files_to_rename.append(filename)
    
    if not files_to_rename:
        print("All filenames are already in the correct format!")
        return
    
    print("The following files will be renamed:")
    for old_name in files_to_rename:
        new_name = sanitize_filename(old_name)
        print(f"- {old_name} -> {new_name}")
    
    print("\nStarting renaming process...")
    
    # Rename files
    for old_name in files_to_rename:
        old_path = os.path.join(image_dir, old_name)
        new_name = sanitize_filename(old_name)
        new_path = os.path.join(image_dir, new_name)
        
        # Handle case where new filename already exists
        counter = 1
        while os.path.exists(new_path) and new_path != old_path:
            name, ext = os.path.splitext(new_name)
            new_name = f"{name}-{counter}{ext}"
            new_path = os.path.join(image_dir, new_name)
            counter += 1
        
        if old_path != new_path:
            shutil.move(old_path, new_path)
            print(f"Renamed: {old_name} -> {new_name}")
    
    print("\nAll files have been renamed successfully!")
    print("Don't forget to update your HTML templates with the new filenames.")

if __name__ == "__main__":
    rename_images()
