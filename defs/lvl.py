import pygame
from pytmx.util_pygame import load_pygame
from states.lvls.desert import DesertLevel
from render.font import Font

tmx_maps = {
    'desert_one': load_pygame('data/tmx/desert_1.tmx'),
    'desert_two': load_pygame('data/tmx/desert_2.tmx'),
}

desert_areas = {
    'desert_one': DesertLevel(tmx_maps, 'desert_one', font_small=Font('data/png/font/small_font.png'), font_large=Font('data/png/font/large_font.png')),
    'desert_two': DesertLevel(tmx_maps, 'desert_two', font_small=Font('data/png/font/small_font.png'), font_large=Font('data/png/font/large_font.png')),
}
