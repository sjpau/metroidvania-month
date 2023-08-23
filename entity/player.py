import pygame
from component.graphics import Graphics2D
from component.physics import Physics2D
from entity.entity import Entity
from render.animation import Animation
import loader.assets as assets
import loader.loader as loader

class Player(
    pygame.sprite.Sprite,
    Entity,
    Graphics2D,
    Physics2D,
    ):
    def __init__(self, position, group, size, image):
        super(Player, self).__init__(group)
        animations = {
            'idle': Animation(loader.load_sprites(assets.sprites_player['idle']), 300)
        }
        self.on_ground = False
        Entity.__init__(self, image, position)
        Graphics2D.__init__(self, image, animations=animations)
        Physics2D.__init__(self, size)
        self.group = group

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_l]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_h]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            self.jump()

    def update(self, dt):
        self.get_input()
        #self.set_animation('idle')
        self.graphics_update_animation(dt)
