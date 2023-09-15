import pygame
import pytmx
from entity.tile import Tile
from entity.tmx import Decoration, Spawner, Trigger, Limit, Wall, Spike, Pickup, TextObject
from defs.finals import tile_size
from loader.loader import png
from render.font import Font

def unpack_tmx(tmx_data, lvl_name, tile_layers_to_groups, obj_layers_to_groups):
    tmx_tiles = []
    tmx_decor = []
    tmx_triggers = []
    tmx_spawners = []
    tmx_limits = []
    tmx_walls = []
    tmx_enemy_walls = []
    tmx_spikes = []
    tmx_pickups = []
    tmx_text = []
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
                t_id = obj.id
                t_type = obj.t_type
                action = obj.action
                if t_type == "sender":
                    desired_receiver_id = obj.desired_receiver_id
                else:
                    desired_receiver_id = ""
                t = Trigger(pos, surf, obj_layers_to_groups[obj_layer_name], t_type=t_type, t_id=t_id, desired_receiver_id=desired_receiver_id, action=action)
                tmx_triggers.append(t)
            if obj.type == 'Transitioner':
                pos = pygame.math.Vector2(obj.x, obj.y)
                surf = pygame.Surface((int(obj.width), int(obj.height)))
                surf.set_alpha(0)
                t_id = obj.id
                t_type = obj.t_type
                if t_type == "sender":
                    desired_receiver_id = obj.desired_receiver_id
                else:
                    desired_receiver_id = ""
                action = obj.action
                transition_to = obj.transition_to_class
                t = Trigger(pos, surf, obj_layers_to_groups[obj_layer_name], t_type=t_type, t_id=t_id, desired_receiver_id=desired_receiver_id, action=action, action_receiver=transition_to)
            if obj.type == 'Spawner':
                pos = pygame.math.Vector2(obj.x, obj.y)
                surf = pygame.Surface((int(obj.width), int(obj.height)))
                surf.set_alpha(0)
                entity_spawn = obj.entity
                active = obj.active
                t_id = obj.id
                s = Spawner(pos, surf, obj_layers_to_groups[obj_layer_name], entity_spawn=entity_spawn, active=active, t_id=t_id)
                tmx_spawners.append(s)
            if obj.type == 'Limit':
                pos = pygame.math.Vector2(obj.x, obj.y)
                surf = pygame.Surface((int(obj.width), int(obj.height)))
                surf.set_alpha(0)
                l = Limit(pos, surf, obj_layers_to_groups[obj_layer_name], obj.limit_on)
                tmx_limits.append(l)
            if obj.type == 'Wall':
                pos = pygame.math.Vector2(obj.x, obj.y)
                surf = pygame.Surface((int(obj.width), int(obj.height)))
                surf.set_alpha(0)
                w = Wall(pos, surf, obj_layers_to_groups[obj_layer_name])
                tmx_walls.append(w)
            if obj.type == 'WallForEnemy':
                pos = pygame.math.Vector2(obj.x, obj.y)
                surf = pygame.Surface((int(obj.width), int(obj.height)))
                surf.set_alpha(0)
                w = Wall(pos, surf, obj_layers_to_groups[obj_layer_name])
                tmx_enemy_walls.append(w)
            if obj.type == 'Spike':
                pos = pygame.math.Vector2(obj.x, obj.y)
                surf = pygame.Surface((int(obj.width), int(obj.height)))
                surf.set_alpha(0)
                s = Spike(pos, surf, obj_layers_to_groups[obj_layer_name])
                tmx_spikes.append(s)
            if obj.type == 'Pickup':
                pos = pygame.math.Vector2(obj.x, obj.y)
                surf = png('data/png/misc/not_found.png')
                p = Pickup(pos, surf, obj_layers_to_groups[obj_layer_name], active=obj.active, ability=obj.ability)
                tmx_pickups.append(p)
            if obj.type == 'TextObject':
                pos = pygame.math.Vector2(obj.x, obj.y)
                surf = pygame.Surface((obj.width, obj.height))
                surf.set_colorkey((0,0,0))
                t = TextObject(pos, surf, obj_layers_to_groups[obj_layer_name], obj.text, Font('data/png/font/small_font.png'))

    return tmx_tiles, tmx_decor, tmx_triggers, tmx_spawners, tmx_limits, tmx_walls, tmx_enemy_walls, tmx_spikes, tmx_pickups, tmx_text