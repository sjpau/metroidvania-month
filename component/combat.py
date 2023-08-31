import pygame
from defs.finals import tile_size

class Combat:
    def __init__(self, hit_box_group=None, melee_hitbox=pygame.Surface((tile_size, tile_size)), projectile_hitbox=None):
        self.attack_direction = {
            "left": False,
            "right": False,
            "up": False,
            "down": False,
        }
        self.melee_hitbox = melee_hitbox
    
    def set_attack_direction(self, a_dir):
        for d in self.attack_direction:
            if a_dir == d:
                self.attack_direction[a_dir] = True
            else:
                self.attack_direction[d] = False