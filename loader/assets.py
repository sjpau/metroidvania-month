import os

def collect_image_paths(directory_path):
    image_paths = []
    for _, _, files in os.walk(directory_path):
        for filename in files:
            image_paths.append(os.path.join(directory_path, filename))

    return image_paths

sp = 'data/sprites/player/idle/'
sp_ = 'data/sprites/player/run/'
sprites_player = {
    'idle': sorted(collect_image_paths(sp)),
    'run': sorted(collect_image_paths(sp_)), # TODO better var naming
}

sp = 'data/sprites/env/dust/'
sprites_env_dust = {
    'dust': sorted(collect_image_paths(sp)),
}
