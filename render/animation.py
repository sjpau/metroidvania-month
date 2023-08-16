import pygame

class Animation():
    def __init__(self, sprites, speed):
        self.sprites = sprites
        self.speed = speed
        self.current_sprite = 0
        self.frame_timer = 0.0
    
    def get_current_sprite(self):
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        return self.sprites[int(self.current_sprite)]
    
    def get_sprite(self, i):
        return self.sprites[i]

    def play(self, dt):
        self.frame_timer += dt
        if self.frame_timer >= self.speed:
            self.frame_timer = 0.0
            self.current_sprite += 1
