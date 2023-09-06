import pygame

class Animation():
    def __init__(self, sprites, speed, play_once=False):
        self.sprites = sprites
        self.masks = []
        for sp in self.sprites:
            self.masks.append(pygame.mask.from_surface(sp))
        self.speed = speed
        self.current_sprite = 0
        self.frame_timer = 0.0
        self.play_once = play_once
        self.done = False

    def get_current_sprite_and_mask(self):
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            if self.play_once:
                self.done = True
        return self.sprites[int(self.current_sprite)], self.masks[int(self.current_sprite)]

    def get_sprite(self, i):
        return self.sprites[i]

    def play(self, dt):
        self.frame_timer += dt
        if self.frame_timer >= self.speed:
            self.frame_timer = 0.0
            self.current_sprite += 1
