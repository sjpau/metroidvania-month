import pygame
from component.graphics import Graphics2D
from entity.entity import Entity

class Tile(
        pygame.sprite.Sprite, 
        Entity, 
        Graphics2D
        ):
    def __init__(self, position, grid_position, image, group, climable=True):
        super().__init__(group)
        self.position = position
        self.grid_position = grid_position
        self.climable = climable # TODO make such component
        Entity.__init__(self, image, position)
        Graphics2D.__init__(self, image, s_type='tile')

    def update(self, dt):
        self.graphics_update_animation(dt)
