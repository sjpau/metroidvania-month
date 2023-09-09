import pygame
from entity.entity import Entity
import random
from defs.finals import CANVAS_HEIGHT, CANVAS_WIDTH

class Cloud(
    pygame.sprite.Sprite,
    Entity,
):
    def __init__(self, position, image, group, depth, speed=0.5):
        super().__init__(group)
        self.position = position
        self.image = image
        Entity.__init__(self, self.image, self.position)
        self.speed = speed
        self.depth = depth
    
    def update(self, dt):
        self.rect.x += self.speed
    
class CloudHandler:
    def __init__(self, images, group, count=13):
        self.clouds = []
        self.images = images
        self.group = group
        for i in range(count):
            self.clouds.append(Cloud(pygame.math.Vector2(random.random() * 99999, random.random() * 99999), 
                                    random.choice(self.images), self.group, random.random() * 0.5 + 0.02 ,speed=random.random() * 0.05 + 0.01))
        self.clouds.sort(key=lambda x: x.depth)

