import pygame    
    
def circle_surface(radius, color):
    if radius > 0:
        surf = pygame.Surface((radius * 2, radius * 2))
        pygame.draw.circle(surf, color, (radius, radius), radius, pygame.SRCALPHA)
        surf.set_colorkey((0, 0, 0))
        surf.set_alpha(100)
        return surf
    else:
        return None
