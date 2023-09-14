import pygame

class ButtonDefault:
    def __init__(self, position, text, char_width, char_height, fixed_width=0, padding=10, color=pygame.Color((0, 0, 0)), outline=1, outline_color=pygame.Color((255,255,255))):
        self.text = text
        self.color = color
        self.outline_color = outline_color
        self.outline = outline
        self.position = position
        render_rect_width = 0
        render_rect_height = char_height
        if not fixed_width:
            for _ in self.text:
                render_rect_width += char_width
        else:
            render_rect_width = fixed_width
        self.render_rect = pygame.FRect((self.position), (render_rect_width, render_rect_height))
        self.padding_rect = pygame.FRect((self.position), (render_rect_width+padding, render_rect_height+padding))
        self.padding_rect.center = self.render_rect.center
        self.surf = pygame.Surface((render_rect_width, render_rect_height))
        self.surf.fill(self.color)
        self.active = False
    
    def draw(self, surface):
        if self.active:
            pygame.draw.rect(surface, self.outline_color, self.padding_rect, self.outline, 2)
        surface.blit(self.surf, self.render_rect.topleft)
        
        