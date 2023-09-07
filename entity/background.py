import pygame

from component.parallax import Parallax
from entity.entity import Entity

class BackgroundLayer(
    pygame.sprite.Sprite,
    Entity,
    Parallax,
):
    def __init__(self, image, position, group, target, factor, ceil, floor=None):
        super().__init__(group)
        self.position = position
        self.image = image
        Entity.__init__(self, image, self.position)
        Parallax.__init__(self, factor, ceil, floor=floor)
        self.target = target

    def update(self, dt):
        self.attach_parallax(self.target)