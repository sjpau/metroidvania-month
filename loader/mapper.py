import pygame
import pytmx
from entity.tile import Tile
from entity.decoration import Decoration
from defs.finals import tile_size

def unpack_tmx(tmx_data, lvl_name, tile_layers_to_groups, obj_layers_to_groups):
    tmx_tiles = []
    tmx_decor = []
    tmx_triggers = []
    # Tiles
    for layer in tmx_data[lvl_name].visible_layers:
        if hasattr(layer, 'data'):
            for x, y, surf in layer.tiles():
                grid_pos = (x,y)
                pos = pygame.math.Vector2(x * tile_size, y * tile_size)
                t = Tile(pos, grid_pos, surf, tile_layers_to_groups[layer.name])
                tmx_tiles.append(t)
    # Objects
    for obj_layer_name in obj_layers_to_groups.keys():
        layer = tmx_data[lvl_name].get_layer_by_name(obj_layer_name)
        for obj in layer:
            if obj.type == 'Static':
                pos = pygame.math.Vector2(obj.x, obj.y)
                d = Decoration(pos, obj.image, obj_layers_to_groups[obj_layer_name])
                tmx_decor.append(d)
            if obj.type == 'Trigger':
                pos = pygame.math.Vector2(obj.x, obj.y)
                surf = pygame.Surface((int(obj.width), int(obj.height)))
                surf.set_alpha(0)
                d = Decoration(pos, surf, obj_layers_to_groups[obj_layer_name])
                tmx_triggers.append(d)

    return tmx_tiles, tmx_decor, tmx_triggers
