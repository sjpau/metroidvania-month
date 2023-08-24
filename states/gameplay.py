import pygame
from .state import State
import defs.finals as finals
from entity.player import Player
from render.camera import Camera
import loader.mapper as mapper

class Gameplay(State):
    def __init__(self, tmx_maps):
        super(Gameplay, self).__init__()
        self.tmx_maps = tmx_maps
        self.sg_camera = Camera(self.canvas, self.scale_factor)
        self.sg_tiles_colliders = Camera(self.canvas, self.scale_factor)
        self.sg_tiles_non_colliders = Camera(self.canvas, self.scale_factor)
        self.sg_decor_fg = Camera(self.canvas, self.scale_factor)
        self.sg_decor_bg = Camera(self.canvas, self.scale_factor)
        self.sg_triggers = Camera(self.canvas, self.scale_factor)
        self.sg_camera_groups = [self.sg_tiles_colliders, self.sg_tiles_non_colliders,
                                 self.sg_decor_fg, self.sg_decor_bg,
                                 self.sg_camera, self.sg_triggers]
        self.tmx_tile_layers_to_sg = { # TODO: better naming of tmx layers
            'colliders': self.sg_tiles_colliders,
            'background': self.sg_tiles_non_colliders,
        }
        self.tmx_obj_layers_to_sg = {
            'decor_fg': self.sg_decor_fg,
            'decor_bg': self.sg_decor_bg,
            'triggers': self.sg_triggers,
        }
        self.tiles, self.decorations, self.triggers = mapper.unpack_tmx(self.tmx_maps, 'example', 
                                                                        self.tmx_tile_layers_to_sg, 
                                                                        self.tmx_obj_layers_to_sg)
        self.player = Player(pygame.math.Vector2(0,0), self.sg_camera, (16, 16),
                            pygame.surface.Surface((finals.tile_size, finals.tile_size)))

    def entity_movement_collision_horizontal(self, entity):  # TODO: MOVE TO LEVEL class
        entity.movement_horizontal() # Entity must have Physics2D component for collision
        for hit in pygame.sprite.spritecollide(entity, self.sg_tiles_colliders, False):
            if entity.direction.x < 0:
                entity.rect.left = hit.rect.right
            if entity.direction.x > 0:
                entity.rect.right = hit.rect.left

    def entity_movement_collision_vertical(self, entity):
        entity.movement_vertical() # Entity must have Physics2D component for collision
        for hit in pygame.sprite.spritecollide(entity, self.sg_tiles_colliders, False):
            if entity.direction.y > 0:
                entity.rect.bottom = hit.rect.top
                entity.direction.y = 0
            if entity.direction.y < 0:
                entity.rect.top = hit.rect.bottom 
                entity.direction.y = 0

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.VIDEORESIZE:
            self.on_videoresize()

    def update(self, dt):
        self.sg_camera.update(dt)
        self.sg_decor_bg.update(dt)
        self.sg_decor_fg.update(dt)
        self.sg_triggers.update(dt)
        self.sg_tiles_colliders.update(dt)
        self.sg_tiles_non_colliders.update(dt)

        self.sg_camera.attach_to(self.player)
        self.sg_tiles_colliders.attach_to(self.player)
        self.sg_tiles_non_colliders.attach_to(self.player)
        self.sg_decor_bg.attach_to(self.player)
        self.sg_decor_fg.attach_to(self.player)
        self.sg_triggers.attach_to(self.player)

        self.entity_movement_collision_horizontal(self.player)
        self.entity_movement_collision_vertical(self.player)

    def draw(self):
        self.canvas.fill(finals.COLOR_GREEN_SUBTLE)
        # Draw Sprite groups
        self.sg_tiles_non_colliders.render_all(self.canvas)
        self.sg_tiles_colliders.render_all(self.canvas)
        self.sg_decor_bg.render_all(self.canvas)
        self.sg_camera.render_all(self.canvas)
        self.sg_decor_fg.render_all(self.canvas)
        self.sg_triggers.render_all(self.canvas)
        self.surface.blit(pygame.transform.scale(self.canvas, (self.surface.get_size())), (0,0))
