import pygame
import pytmx
from entity.tile import Tile
from defs.finals import tile_size

def unpack_tmx(tmx_data, lvl_name, layers_to_groups):
    tiles = []
    for layer in tmx_data[lvl_name].visible_layers:
        if hasattr(layer, 'data'):
            for x, y, surf in layer.tiles():
                grid_pos = (x,y)
                pos = pygame.math.Vector2(x * tile_size, y * tile_size)
                t = Tile(pos, grid_pos, surf, layers_to_groups[layer.name])
                tiles.append(t)
    return tiles
