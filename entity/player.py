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
        self.want_move = {
            'right': False,
            'left': False,
        }
       

    def handle_input(self, event):
        keys_right = [pygame.K_RIGHT, pygame.K_l, pygame.K_d]
        keys_left = [pygame.K_LEFT, pygame.K_h, pygame.K_a]
        keys_jump = [pygame.K_SPACE]
        if event.type == pygame.KEYDOWN:
            k = event.key
            if k in keys_right:
                self.want_move['right'] = True
            elif k in keys_left:
                self.want_move['left'] = True
        if event.type == pygame.KEYUP:
            k = event.key
            if k in keys_jump:
                self.jump()
            if k in keys_right:
                self.want_move['right'] = False
            elif k in keys_left:
                self.want_move['left'] = False


    def update(self, dt):
        if self.want_move['right']:
            self.velocity.x = 1
        if self.want_move['left']:
            self.velocity.x = -1
        if not self.want_move['right'] and not self.want_move['left']:
            self.velocity.x = 0

        self.set_animation('idle')
        self.graphics_update_animation(dt)
