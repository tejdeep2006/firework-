import os

def update_image_paths(file_path):
    # Mapping of old paths to new paths
    path_mapping = {
        'Seematapakayalu (100 Pieces).jpg': 'seema-tapakai.jpg',
        'Bhuchakaram big.jpg': 'bhoo-chakram.jpg',
        'Shower ( 1 piece).jpg': 'shower.jpg',
        'Flower Outs(5 Pieces).jpg': 'flower-pots.jpg',
        'Lakshmi Small (5 Pieces).jpg': 'laxmi-bombs.jpg',
        'Pamubillalu small (10 Pieces).jpg': 'pamu-bilalu.jpg',
        'Pencils (10 Pieces).jpg': 'pencil.jpg',
        'Rockets (10 Pieces).jpg': 'rockets.jpg',
        'Threads Big(1 piece).jpg': 'thadulu-big.jpg',
        'Threads Small(1 Piece).jpg': 'thadulu-small.jpg',
        'Vankaya Ultra Deluxe (10 pieces ).jpg': 'vinkaya-big.jpg',
        '100 Wala (1 packet).jpg': '100-wala.jpg',
        '1000 Wala (1 Packet).jpg': '1000-wala.jpg',
        '2000 Wala (1 Packet).jpg': '2000-wala.jpg',
        '12 Shots.jpg': '12-shots.jpg',
        '1 Shot.jpg': '1shot.jpg',
        '7 Shots (5 pieces).jpg': '7shots.jpg',
        'Chitapatalu (10 Pieces).jpg': 'Chitapatalu (10 Pieces).jpg',
        'VennaMuddalu (10 Pieces).jpg': 'VennaMuddalu (10 Pieces).jpg',
        '28 Wala (1 Packet).jpg': '28 Wala (1 Packet).jpg',
        'Kakarapulu 15cm Colour GreenRed (10 pieces).jpg': 'Kakarapulu 15cm Colour GreenRed (10 pieces).jpg',
        'Kakarapulu 30cm colour (5 pieces).jpg': 'Kakarapulu 30cm colour (5 pieces).jpg',
        'Kakarapulu 7cm(10 pieces).jpg': 'Kakarapulu 7cm(10 pieces).jpg',
        'Kunda Bombulu (1 Pieces).jpg': 'kunda-bombulu.jpg',
        'Laxmi Big (5 Pieces).jpg': 'Laxmi Big (5 Pieces).jpg',
        'Laxmi Medium (5 Pieces).jpg': 'Laxmi Medium (5 Pieces).jpg',
        'Pamubillalu Big(10 Pieces).jpg': 'pamubillalu Big(10 Pieces).jpg',
        'Vankaya Medium (10 Pieces).jpg': 'Vankaya Medium (10 Pieces).jpg'
    }

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace each path
    for old_name, new_name in path_mapping.items():
        old_path = f'src="/static/images/{old_name}"'
        new_path = f'src="/static/images/{new_name}"'
        content = content.replace(old_path, new_path)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print("Image paths updated successfully!")

if __name__ == "__main__":
    file_path = os.path.join('templates', 'index.html')
    update_image_paths(file_path)
