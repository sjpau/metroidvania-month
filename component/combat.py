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
        self.health = 3
        self.invul = 0
        self.alive = True
