import os

def fix_image_paths(file_path):
    # Mapping of old paths to actual filenames
    image_mapping = {
        'seema-tapakai.jpg': 'Seematapakayalu (100 Pieces).jpg',
        'Chitapatalu (10 Pieces).jpg': 'Chitapatalu (10 Pieces).jpg',  # Already correct
        'VennaMuddalu (10 Pieces).jpg': 'VennaMuddalu (10 Pieces).jpg',  # Already correct
        '28 Wala (1 Packet).jpg': '28 Wala (1 Packet).jpg',  # Already correct
        'Bhuchakaram big.jpg': 'bhoo-chakram.jpg',
        'Shower ( 1 piece).jpg': 'Shower ( 1 piece).jpg',  # Already correct
        'Flower Outs(5 Pieces).jpg': 'flower-pots.jpg',
        'Kakarapulu 15cm Colour GreenRed (10 pieces).jpg': 'Kakarapulu 15cm Colour GreenRed (10 pieces).jpg',  # Already correct
        'Kakarapulu 30cm colour (5 pieces).jpg': 'Kakarapulu 30cm colour (5 pieces).jpg',  # Already correct
        'Kakarapulu 7cm(10 pieces).jpg': 'Kakarapulu 7cm(10 pieces).jpg',  # Already correct
        'Kunda Bombulu (1 Pieces).jpg': 'kunda-bombulu.jpg',
        'Lakshmi Small (5 Pieces).jpg': 'laxmi-bombs.jpg',
        'Laxmi Big (5 Pieces).jpg': 'Laxmi Big (5 Pieces).jpg',  # Already correct
        'Laxmi Medium (5 Pieces).jpg': 'Laxmi Medium (5 Pieces).jpg',  # Already correct
        'Pamubillalu small (10 Pieces).jpg': 'Pamubillalu small (10 Pieces).jpg',  # Already correct
        'Pencils (10 Pieces).jpg': 'pencil.jpg',
        'Rockets (10 Pieces).jpg': 'rockets.jpg',
        'Threads Big(1 piece).jpg': 'thadulu-big.jpg',
        'Threads Small(1 Piece).jpg': 'thadulu-small.jpg',
        'Vankaya Medium (10 Pieces).jpg': 'Vankaya Medium (10 Pieces).jpg',  # Already correct
        'Vankaya Ultra Deluxe (10 pieces ).jpg': 'vinkaya-big.jpg',
        '100 Wala (1 packet).jpg': '100-wala.jpg',
        '1000 Wala (1 Packet).jpg': '1000-wala.jpg',
        '2000 Wala (1 Packet).jpg': '2000-wala.jpg',
        '12 Shots.jpg': '12-shots.jpg',
        '1 Shot.jpg': '1shot.jpg',
        '7 Shots (5 pieces).jpg': '7shots.jpg',
        '2 Sound (5 Pieces).jpg': '2 Sound (5 Pieces).jpg',  # Already correct
        '30 Shots.jpg': '30 Shots.jpg',  # Already correct
        'Bullet Bombs (10 Pieces).jpg': 'Bullet Bombs (10 Pieces).jpg',  # Already correct
        'Chichubudlu Small(10 Pieces).jpg': 'Chichubudlu Small(10 Pieces).jpg',  # Already correct
        'Chichubudlu Big (10 Pieces).jpg': 'Chichubudlu Big (10 Pieces).jpg',  # Already correct
        'Pamubillalu Big(10 Pieces).jpg': 'Pamubillalu Big(10 Pieces).jpg'  # Already correct
    }

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace each path
    for old_name, new_name in image_mapping.items():
        old_path = f'src="static/images/{old_name}"'
        new_path = f'src="static/images/{new_name}"'
        content = content.replace(old_path, new_path)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print("Image paths updated successfully!")

if __name__ == "__main__":
    file_path = os.path.join('templates', 'index.html')
    fix_image_paths(file_path)
