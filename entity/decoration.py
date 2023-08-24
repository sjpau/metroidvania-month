import pygame
from entity.entity import Entity
from component.graphics import Graphics2D

class Decoration(
        pygame.sprite.Sprite,
        Entity,
        Graphics2D,
        ):
    def __init__(self, position, image, group):
        super().__init__(group)
        self.position = position
        Entity.__init__(self, image, position)
        Graphics2D.__init__(self, image, s_type='tile')
    
    def update(self, dt):
        self.graphics_update_animation(dt)