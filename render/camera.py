import pygame
from defs.finals import CANVAS_HEIGHT, CANVAS_WIDTH

class Camera(pygame.sprite.Group): 
    def __init__(self, canvas):
        super().__init__()
        self.half_width = canvas.get_width() / 2
        self.half_height = canvas.get_height() / 2
        self.offset = pygame.math.Vector2(self.half_width, self.half_height)
        self.render_rect = pygame.FRect(canvas.get_rect())

        self.min_x = None
        self.min_y = None
        self.max_x = None
        self.max_y = None
    
    def set_level_borders(self, min_x, min_y, max_x, max_y):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        
    def attach_to(self, target):
        x = target.rect.centerx
        y = target.rect.centery
        
        unstrict_x = self.offset.x + (x - self.half_width - self.offset.x) / 15
        unstrict_y = self.offset.y + (y - self.half_height - self.offset.y) / 15
        
        self.offset.x = max(self.min_x, min(unstrict_x, self.max_x - self.half_width * 2))
        self.offset.y = max(self.min_y, min(unstrict_y, self.max_y - self.half_height * 2))
        self.render_rect.topleft = self.offset
    
    def render_all(self, surface, special_flags=0):
        for sprite in self.sprites():
            if self.render_rect.colliderect(sprite.rect):
                offset_pos = sprite.rect.topleft - self.offset
                surface.blit(sprite.image, offset_pos, special_flags=special_flags)
    
    def render_all_parallax(self, surface, special_flags=0):
        for sprite in self.sprites():
            offset_pos = pygame.math.Vector2()
            offset_pos.x = sprite.rect.x - self.offset.x * sprite.depth
            offset_pos.y = sprite.rect.y - self.offset.y * sprite.depth
            offset_pos.x = offset_pos.x % (CANVAS_WIDTH + sprite.rect.width) - sprite.rect.width
            offset_pos.y = offset_pos.y % (CANVAS_HEIGHT + sprite.rect.height) - sprite.rect.height
            surface.blit(sprite.image, offset_pos, special_flags=special_flags)