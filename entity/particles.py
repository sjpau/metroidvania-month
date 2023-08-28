import pygame
from math import sin, cos
from entity.entity import Entity
from component.graphics import Graphics2D
from component.physics import Physics2D
from loader.assets import sprites_env_dust
from loader.loader import load_sprites
from render.animation import Animation

import random

class ParticleDust(
    pygame.sprite.Sprite,
    Entity,
    Graphics2D,
    Physics2D,
):
    def __init__(self, position, image, group, size=1):
        super().__init__(group)
        self.position = position
        self.kill = False
        self.group = group
        self.sin_counter = -100
        animations = {
            'dust': Animation(load_sprites(sprites_env_dust['dust']), 500)
        }
        Entity.__init__(self, image, position)
        Graphics2D.__init__(self, image, s_type='particle_dust', animations=animations)
        Physics2D.__init__(self, size)
        self.playing_busy = True
        self.ttl = 500
        self.ttl_counter = 0
        self.sign_x = 1 if random.random() < 0.5 else -1
        self.sign_y = 1 if random.random() < 0.5 else -1
    
    def update(self, dt):
        self.set_animation('dust')
        self.graphics_update_animation(dt)
        self.sin_counter += 1
        self.ttl_counter += 1
        if self.sin_counter == 100:
            self.sin_counter = -100
        self.velocity.x = self.sign_x * sin(self.sin_counter * 0.035) * 0.3
        self.velocity.y = self.sign_y * 0.3
        self.movement_horizontal()
        self.movement_vertical()
        if not self.playing_busy and self.ttl_counter > self.ttl:
            self.kill = True

