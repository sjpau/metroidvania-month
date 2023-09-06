import pygame

class Graphics2D:
    def __init__(self, image, animations={}, s_type='default'):
        self.image = image
        self.mask = pygame.mask.from_surface(image)
        self.type = s_type
        self.animations = animations
        self.current_animation = None

    def set_animation(self, name):
        if name in self.animations:
            self.current_animation = self.animations[name]

    def graphics_update_animation(self, dt):
        if self.current_animation is not None:
            self.current_animation.play(dt)
            if self.direction['left']: 
                self.image, _ = self.current_animation.get_current_sprite_and_mask()
                self.image = pygame.transform.flip(self.image, True, False)
                self.mask = pygame.mask.from_surface(self.image)
            else:
                self.image, self.mask = self.current_animation.get_current_sprite_and_mask()