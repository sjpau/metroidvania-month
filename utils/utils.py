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

def bool_dict_set_true(dic, key_to_true):
        for key in dic:
            if key_to_true == key:
                dic[key_to_true] = True
            else:
                dic[key] = False