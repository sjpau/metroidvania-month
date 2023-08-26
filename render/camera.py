import pygame

class Camera(pygame.sprite.Group): 
    def __init__(self, canvas, scale_factor):
        super().__init__()
        self.scale_factor = scale_factor
        self.half_width = canvas.get_width() / 2
        self.half_height = canvas.get_height() / 2
        self.offset = pygame.math.Vector2(self.half_width, self.half_height)
        self.render_rect = pygame.FRect(canvas.get_rect())
    
    def attach_to(self, target):
        x = target.rect.centerx
        y = target.rect.centery
        self.offset.x += (x - self.half_width - self.offset.x) / 30
        self.offset.y += (y - self.half_height - self.offset.y) / 30
        self.render_rect.topleft = self.offset

    def render_all(self, surface):
        for sprite in self.sprites():
            if self.render_rect.colliderect(sprite.rect):
                offset_pos = sprite.rect.topleft - self.offset
                surface.blit(sprite.image, offset_pos)
        pygame.draw.rect(surface, 'yellow', self.render_rect, 4)