import pygame
from entity.entity import Entity
from component.graphics import Graphics2D

class ShadowSprite(
    pygame.sprite.Sprite,
    Entity,
    Graphics2D,
):
    def __init__(self, target, group, color, alpha_dec=15):
        super().__init__(group)
        self.position = pygame.math.Vector2(target.rect.topleft)
        self.mask = pygame.mask.from_surface(target.image)
        self.image = self.mask.to_surface()
        self.image.set_colorkey((0,0,0))
        w, h = self.image.get_size()
        self.color = color
        for x in range(w):
            for y in range(h):
                if self.image.get_at((x,y))[0] != 0:
                    self.image.set_at((x,y), self.color)
        Entity.__init__(self, self.image, self.position)
        Graphics2D.__init__(self, self.image)
        self.alpha = 255
        self.alpha_dec = alpha_dec
        self.kill = False
    
    def update(self, dt):
        self.alpha -= self.alpha_dec
        self.image.set_alpha(self.alpha)
        if self.alpha == 0:
            self.kill = True
