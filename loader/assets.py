import os

def collect_image_paths(directory_path):
    image_paths = []

    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_paths.append(os.path.join(directory_path, filename))

    return image_paths

sprite_path = 'asset/sprites/player/idle/'
sprites_player = {
    'idle': collect_image_paths(sprite_path),
}
