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
    
    def set_direction(self, new):
        for key in self.direction:
            if new == key:
                self.direction[new] = True
            else:
                self.direction[key] = False