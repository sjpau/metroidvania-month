import os

def collect_image_paths(directory_path):
    image_paths = []
    for _, _, files in os.walk(directory_path):
        for filename in files:
            image_paths.append(os.path.join(directory_path, filename))

    return image_paths

sp = 'data/png/parallax/'
sprites_background_layers = sorted(collect_image_paths(sp))
sp = 'data/sprites/env/clouds/'
sprites_clouds = sorted(collect_image_paths(sp))

sp = 'data/sprites/player/idle/'
sp_r = 'data/sprites/player/run/'
sp_d = 'data/sprites/player/dash/'
sp_up = 'data/sprites/player/up/'
sp_down = 'data/sprites/player/down/'
sp_ah = 'data/sprites/player/attack_hor/'
sprites_player = {
    'idle': sorted(collect_image_paths(sp)),
    'run': sorted(collect_image_paths(sp_r)), # TODO better var naming
    'dash': sorted(collect_image_paths(sp_d)),
    'up': sorted(collect_image_paths(sp_up)),
    'down': sorted(collect_image_paths(sp_down)),
    'attack_hor': sorted(collect_image_paths(sp_ah)),
}
sp = 'data/sprites/player/slash/'
sp_v = 'data/sprites/player/slash_ver/'
sprites_player_slash = {
    'slash': sorted(collect_image_paths(sp)),
    'slash_ver': sorted(collect_image_paths(sp_v)),
}

sp = 'data/sprites/enemy/melee/bandit/idle/'
sprites_enemy_melee_bandit = {
    'idle': sorted(collect_image_paths(sp)),
}

sp = 'data/sprites/env/dust/'
sprites_env_dust = {
    'dust': sorted(collect_image_paths(sp)),
}
