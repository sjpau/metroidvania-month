import os

def collect_image_paths(directory_path):
    image_paths = []

    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_paths.append(os.path.join(directory_path, filename))

    return image_paths

sprite_path = 'data/sprites/player/idle/'
sprites_player = {
    'idle': sorted(collect_image_paths(sprite_path)),
}
sprite_path = 'data/sprites/env/dust/'
sprites_env_dust = {
    'dust': sorted(collect_image_paths(sprite_path)),
}
