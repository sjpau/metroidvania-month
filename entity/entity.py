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
        }