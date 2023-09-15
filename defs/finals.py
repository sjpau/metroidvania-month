from typing import Final
import pygame

tile_size: Final = 16

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

PATH_BACKGROUND: Final = "data/png/background.png"

COLOR_BLACK: Final = pygame.Color((16, 13, 19))
COLOR_WHITE: Final = pygame.Color((255, 255, 255))
COLOR_BEIGE: Final = pygame.Color((242, 229, 177))
COLOR_HERO_GREEN: Final = pygame.Color((40, 195, 151))
COLOR_HERO_BLUE: Final = pygame.Color((153, 230, 230))
COLOR_HERO_GRAY: Final = pygame.Color((53, 48, 31))
COLOR_HERO_GREEN_SUBTLE: Final = pygame.Color((22, 110, 85))
