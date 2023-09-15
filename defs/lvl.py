import pygame
from pytmx.util_pygame import load_pygame
from states.lvls.desert import DesertLevel
from states.menus import MainMenu
from render.font import Font

tmx_maps = {
    'desert_one': load_pygame('data/tmx/desert_1.tmx'),
    'desert_two': load_pygame('data/tmx/desert_2.tmx'),
    'desert_three': load_pygame('data/tmx/desert_3.tmx'),
    'desert_four': load_pygame('data/tmx/desert_4.tmx'),
}

states = {
    # Desert area
    'desert_one': DesertLevel(tmx_maps, 'desert_one', font_small=Font('data/png/font/small_font.png'), font_large=Font('data/png/font/large_font.png'), name='desert_one'),
    'desert_two': DesertLevel(tmx_maps, 'desert_two', font_small=Font('data/png/font/small_font.png'), font_large=Font('data/png/font/large_font.png'), name='desert_two'),
    'desert_three': DesertLevel(tmx_maps, 'desert_three', font_small=Font('data/png/font/small_font.png'), font_large=Font('data/png/font/large_font.png'), name='desert_three'),
    'desert_four': DesertLevel(tmx_maps, 'desert_four', font_small=Font('data/png/font/small_font.png'), font_large=Font('data/png/font/large_font.png'), name='desert_four'),
    # Non gameplay
    'main_menu': MainMenu(None, font_small=Font('data/png/font/small_font.png'), font_large=Font('data/png/font/large_font.png'), name='main_menu'),
}

