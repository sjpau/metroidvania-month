import pygame

class Camera(pygame.sprite.Group):
    def __init__(self, canvas, scale_factor):
        super().__init__()
        self.canvas = canvas
        self.scale_factor = scale_factor
        self.half_width = self.canvas.get_width() // 2
        self.half_height = self.canvas.get_height() // 2
        self.offset = pygame.math.Vector2(self.half_width, self.half_height)

    def attach_to(self, target):
        x = target.rect.center[0]
        y = target.rect.center[1]
        self.offset.x = x - self.half_width
        self.offset.y = y - self.half_height

    def render_all(self, surface):
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            surface.blit(sprite.image, offset_pos)
