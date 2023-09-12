import pygame
from pytmx.util_pygame import load_pygame
from states.lvls.desert import DesertLevel

tmx_maps = {
    'desert_one': load_pygame('data/tmx/desert_1.tmx'),
    'desert_two': load_pygame('data/tmx/desert_2.tmx'),
}

desert_areas = {
    'desert_one': DesertLevel(tmx_maps, 'desert_one'),
    'desert_two': DesertLevel(tmx_maps, 'desert_two'),
}
