import pygame

def load_sprites(sprite_list):
    sprites = []
    for path in sprite_list:
        image = pygame.image.load(path).convert_alpha()
        sprites.append(image)
    return sprites

def png(path):
    return pygame.image.load(path).convert_alpha()