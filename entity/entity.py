import pygame

class Entity:
    def __init__(self, surface, position):
        self.surface = surface
        self.rect = pygame.FRect(self.surface.get_rect())
        self.rect.topleft = position
        self.abilities = {
            'hop': True,
            'slide': True,
            'dash': False,
        }
        self.direction = {
            "left": False,
            "right": False,
            "up": False,
            "down": False,
        }
        self.direction_pi = {
            "left": 1,
            "right": 0,
            "up": 1.5,
            "down": 0.5,
        }
        self.ability_remove_on_death = []
        self.want_be_flipped_ver = False

    def entity_movement_collision_horizontal(self, collide_groups):
        self.movement_horizontal() # Entity must have Physics2D component for collision
        for group in collide_groups:
            for hit in pygame.sprite.spritecollide(self, group, False):
                if self.velocity.x < 0:
                    self.rect.left = hit.rect.right
                if self.velocity.x > 0:
                    self.rect.right = hit.rect.left
                if not self.on_ground and self.abilities['slide'] and hit.climable:
                    self.velocity.y = min(self.velocity.y, 0.3)
                    self.jumps = 1

    def entity_movement_collision_vertical(self, collide_groups):
        self.movement_vertical() # Entity must have Physics2D component for collision
        for group in collide_groups:
            for hit in pygame.sprite.spritecollide(self, group, False):
                if self.velocity.y > 0:
                    self.rect.bottom = hit.rect.top
                    self.velocity.y = 0
                    if self.abilities['hop']:
                        self.jumps = 2
                    else:
                        self.jumps = 1
                if self.velocity.y < 0:
                    self.rect.top = hit.rect.bottom 
                    self.velocity.y = 0