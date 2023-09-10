import pygame
from math import sin, cos, pi
from entity.entity import Entity
from component.graphics import Graphics2D
from component.physics import Physics2D
from loader.assets import sprites_env_dust
from loader.loader import load_sprites
from render.animation import Animation
from utils.utils import circle_surface

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

class ParticleBlob:
    def __init__(self, position, color, radius, glow_color, velocity=pygame.math.Vector2(0,0)):
        self.position = position
        self.color = color
        self.radius = radius
        self.glow_color = glow_color
        self.velocity = velocity
        self.glow_radius = self.radius*2
        self.kill = False
    
    def update(self, dt):
        self.position += self.velocity
        self.radius -= 0.1
        self.glow_radius = self.radius * 2
        if self.radius <= 0:
            self.kill = True
    
    def draw(self, screen, camera):
        offset_pos = self.position - camera.offset
        pygame.draw.circle(screen, self.color, (int(offset_pos.x), int(offset_pos.y)), int(self.radius))
        circ_surf = circle_surface(self.glow_radius, color=self.glow_color)
        if circ_surf is not None:
            screen.blit(circ_surf, (int(offset_pos.x - self.glow_radius), int(offset_pos.y - self.glow_radius)), special_flags=pygame.BLEND_RGB_ADD)

class ParticleSpark:
    def __init__(self, position, color, angle, speed):
        self.position = position
        self.angle = angle
        self.speed = speed
        self.color = color
        self.kill = False

    def update(self, dt):
        self.position.x += cos(self.angle) * self.speed
        self.position.y += sin(self.angle) * self.speed

        self.speed = max(0, self.speed - 0.1)
        if not self.speed:
            self.kill = True
    
    def draw(self, screen, camera):
        render_points = [
            (self.position.x + cos(self.angle) * self.speed * 3 - camera.offset.x,
            self.position.y + sin(self.angle) * self.speed * 3 - camera.offset.y),

            (self.position.x + cos(self.angle + pi * 0.5) * self.speed * 0.5 - camera.offset.x,
            self.position.y + sin(self.angle + pi * 0.5) * self.speed * 0.5 - camera.offset.y),

            (self.position.x + cos(self.angle + pi) * self.speed * 3 - camera.offset.x,
            self.position.y + sin(self.angle + pi) * self.speed * 3 - camera.offset.y),

            (self.position.x + cos(self.angle - pi * 0.5) * self.speed * 0.5 - camera.offset.x,
            self.position.y + sin(self.angle - pi * 0.5) * self.speed * 0.5 - camera.offset.y),
        ]

        pygame.draw.polygon(screen, self.color, render_points )