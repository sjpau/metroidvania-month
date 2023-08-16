import pygame

class Graphics2D:
    def __init__(self, image, animations={}):
        self.image = image
        self.rect = self.image.get_rect()
        self.animations = animations
        self.current_animation = None
        self.playing_busy = False

    def set_animation(self, name):
        if name in self.animations:
            self.current_animation = self.animations[name]

    def g2d_update(self, dt):
        if self.current_animation is not None:
            if self.playing_busy:
                if self.current_animation.current_sprite >= len(self.current_animation.sprites)-1:
                    self.playing_busy = False
                    self.current_animation.current_sprite = 0
            self.current_animation.play(dt)
            self.image = self.current_animation.get_current_sprite()
