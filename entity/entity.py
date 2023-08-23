import pygame

class Entity:
    def __init__(self, surface, position):
        self.surface = surface
        self.rect = pygame.FRect(self.surface.get_rect())
        #self.rect = self.surface.get_rect()
        self.rect.topleft = position