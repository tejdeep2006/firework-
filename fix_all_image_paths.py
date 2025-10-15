import os
import re

def fix_image_paths(file_path):
    # Mapping of displayed names to actual filenames
    image_mapping = {
        'Seematapakayalu (100 Pieces).jpg': 'seema-tapakai.jpg',
        'Chitapatalu (10 Pieces).jpg': 'Chitapatalu (10 Pieces).jpg',  # This one seems correct
        'VennaMuddalu (10 Pieces).jpg': 'VennaMuddalu (10 Pieces).jpg',  # This one seems correct
        '28 Wala (1 Packet).jpg': '28 Wala (1 Packet).jpg',  # This one seems correct
        'Bhuchakaram big.jpg': 'bhoo-chakram.jpg',
        'Shower ( 1 piece).jpg': 'shower.jpg',  # Note: I don't see this exact file, you might need to add it
        'Flower Outs(5 Pieces).jpg': 'flower-pots.jpg',
        'Kakarapulu 15cm Colour GreenRed (10 pieces).jpg': 'kakarapulu-15cm.jpg',  # Adjust if needed
        'Kakarapulu 30cm colour (5 pieces).jpg': 'kakarapulu-30cm.jpg',  # Adjust if needed
        'Kakarapulu 7cm(10 pieces).jpg': 'kakarapulu-7cm.jpg',  # Adjust if needed
        'Lakshmi Small (5 Pieces).jpg': 'laxmi-bombs.jpg',
        'Laxmi Big (5 Pieces).jpg': 'laxmi-big.jpg',  # Adjust if needed
        'Laxmi Medium (5 Pieces).jpg': 'laxmi-mid.jpg',  # Adjust if needed
        'Pamubillalu small (10 Pieces).jpg': 'pamu-bilalu.jpg',
        'Pencils (10 Pieces).jpg': 'pencil.jpg',
        'Rockets (10 Pieces).jpg': 'rockets.jpg',
        'Threads Big(1 piece).jpg': 'thadulu-big.jpg',
        'Threads Small(1 Piece).jpg': 'thadulu-small.jpg',
        'Vankaya Medium (10 Pieces).jpg': 'vinkaya-mid.jpg',  # Adjust if needed
        'Vankaya Ultra Deluxe (10 pieces ).jpg': 'vinkaya-big.jpg',
        'Bullet Bombs (10 Pieces).jpg': 'bullet-bombs.jpg',  # Adjust if needed
        '100 Wala (1 packet).jpg': '100-wala.jpg',
        '1000 Wala (1 Packet).jpg': '1000-wala.jpg',
        '2000 Wala (1 Packet).jpg': '2000-wala.jpg',
        '12 Shots.jpg': '12-shots.jpg',
        '15 shots.jpg': '15-shots.jpg',  # Adjust if needed
        '1 Shot.jpg': '1shot.jpg',
        '7 Shots (5 pieces).jpg': '7shots.jpg',
        '2 Sound (5 Pieces).jpg': '2-sound.jpg',  # Adjust if needed
        '30 Shots.jpg': '30-shots.jpg',  # Adjust if needed
    }

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace each image path
    for old_name, new_name in image_mapping.items():
        old_path = f'src="/static/images/{old_name}"'
        new_path = f'src="/static/images/{new_name}"'
        content = content.replace(old_path, new_path)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print("Image paths updated successfully!")

if __name__ == "__main__":
    file_path = os.path.join('templates', 'index.html')
    fix_image_paths(file_path)
