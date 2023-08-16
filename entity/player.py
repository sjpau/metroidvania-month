import pygame
from component.graphics import Graphics2D
from component.physics import Physics2D
from render.animation import Animation
import loader.assets as assets
import loader.loader as loader

class Player(
    pygame.sprite.Sprite,
    Graphics2D,
    Physics2D,
    ):
    def __init__(self, position, group, size, *args, **kwargs):
        super(Player, self).__init__(group)
        animations = {
            'idle': Animation(loader.load_sprites(assets.sprites_player['idle']), 300)
        }
        Graphics2D.__init__(self, *args, **kwargs, animations=animations)
        Physics2D.__init__(self, position, size)
        self.group = group

    def update(self, dt):
        self.rect.center = self.position
        self.g2d_update(dt)
        self.p2d_update()
        self.set_animation('idle')
