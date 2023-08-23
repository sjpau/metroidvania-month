from typing import Final
import pygame

tile_size: Final = 16

NEIGHBOUR_OFFSETS = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (0,0), (-1,1), (0,1), (1,1)]

display_resolution: Final = {
    '64x64': (64, 64),
    '320x320': (320, 320),
    '640x640': (640, 640),
    '1280x1280': (1280, 1280),
    '320x180': (320, 180),
    '640x360': (640, 360),
    '1280x720': (1280, 720),
    '1920x1080': (1920, 1080),
}

CANVAS_WIDTH: Final = 320
CANVAS_HEIGHT: Final = 180

CAPTION: Final = "Metroidvania month"

COLOR_BLACK: Final = pygame.Color((16, 13, 19))
COLOR_RED: Final = pygame.Color((170, 0, 0))
COLOR_GREEN_SUBTLE: Final = pygame.Color((132, 197, 166))
