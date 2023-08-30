import pygame
from .state import State
import defs.finals as finals
from entity.player import Player
from render.camera import Camera
import loader.mapper as mapper
from loader.loader import png
from entity.particles import ParticleDust
import random

class Gameplay(State):
    def __init__(self, tmx_maps):
        super(Gameplay, self).__init__()
        self.handle = {
            'player input': True,
        }
        self.tmx_maps = tmx_maps
        self.background = png(finals.PATH_BACKGROUND)
        self.sg_camera = Camera(self.canvas, self.scale_factor)
        self.sg_tiles_colliders = Camera(self.canvas, self.scale_factor)
        self.sg_tiles_non_colliders = Camera(self.canvas, self.scale_factor)
        self.sg_decor_fg = Camera(self.canvas, self.scale_factor)
        self.sg_decor_bg = Camera(self.canvas, self.scale_factor)
        self.sg_dust_fg = Camera(self.canvas, self.scale_factor)
        self.sg_dust_bg = Camera(self.canvas, self.scale_factor)
        self.sg_triggers = Camera(self.canvas, self.scale_factor)
        self.sg_spawners = Camera(self.canvas, self.scale_factor)
        self.sg_camera_groups = [self.sg_tiles_colliders, self.sg_tiles_non_colliders,
                                 self.sg_decor_fg, self.sg_decor_bg,
                                 self.sg_camera, self.sg_triggers,
                                 self.sg_dust_fg, self.sg_dust_bg,
                                 self.sg_spawners,]
        self.tmx_tile_layers_to_sg = {
            'colliders': self.sg_tiles_colliders,
            'background': self.sg_tiles_non_colliders,
        }
        self.tmx_obj_layers_to_sg = {
            'decor_fg': self.sg_decor_fg,
            'decor_bg': self.sg_decor_bg,
            'triggers': self.sg_triggers,
            'spawners': self.sg_spawners,
        }
        self.tiles, self.decorations, self.triggers, self.spawners = mapper.unpack_tmx(self.tmx_maps, 'example', 
                                                                        self.tmx_tile_layers_to_sg, 
                                                                        self.tmx_obj_layers_to_sg)
        self.player = Player(pygame.math.Vector2(0,0), self.sg_camera, (16, 16),
                            pygame.surface.Surface((finals.tile_size, finals.tile_size)))
        self.player_box = pygame.FRect(self.canvas.get_rect())
        self.particles_dust = []
        self.handler_entity_spawn = { # TODO how to spawn enemies?
            "player": self.player,
        }
        for spawner in self.spawners:
            spawner.spawn(self.handler_entity_spawn)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.VIDEORESIZE:
            self.on_videoresize()
        if self.handle['player input']:
            self.player.handle_input(event)

    def entity_movement_collision_horizontal(self, entity): # Unfortunately has to be here 'cuz of sgs
        entity.movement_horizontal() # Entity must have Physics2D component for collision
        for hit in pygame.sprite.spritecollide(entity, self.sg_tiles_colliders, False):
            if entity.velocity.x < 0:
                entity.rect.left = hit.rect.right
            if entity.velocity.x > 0:
                entity.rect.right = hit.rect.left

    def entity_movement_collision_vertical(self, entity):
        entity.movement_vertical() # Entity must have Physics2D component for collision
        for hit in pygame.sprite.spritecollide(entity, self.sg_tiles_colliders, False):
            if entity.velocity.y > 0:
                entity.rect.bottom = hit.rect.top
                entity.velocity.y = 0
                if entity.abilities['hop']:
                    entity.jumps = 2
                else:
                    entity.jumps = 1
            if entity.velocity.y < 0:
                entity.rect.top = hit.rect.bottom 
                entity.velocity.y = 0

    def entity_on_trigger(self, entity):
        for hit in pygame.sprite.spritecollide(entity, self.sg_triggers, False):
            if hit.action == "teleport" and hit.type == "sender":
                find_id = hit.desired_receiver_id
                for trigger in self.sg_triggers:
                    if int(find_id) == int(trigger.t_id):
                        entity.rect.topleft = trigger.rect.topleft
                        break


    def update(self, dt):
        self.sg_camera.update(dt)
        self.sg_decor_bg.update(dt)
        self.sg_decor_fg.update(dt)
        self.sg_triggers.update(dt)
        self.sg_spawners.update(dt)
        self.sg_tiles_colliders.update(dt)
        self.sg_tiles_non_colliders.update(dt)
        self.sg_dust_bg.update(dt)
        self.sg_dust_fg.update(dt)

        self.sg_camera.attach_to(self.player)
        self.sg_tiles_colliders.attach_to(self.player)
        self.sg_tiles_non_colliders.attach_to(self.player)
        self.sg_decor_bg.attach_to(self.player)
        self.sg_decor_fg.attach_to(self.player)
        self.sg_triggers.attach_to(self.player)
        self.sg_spawners.attach_to(self.player)
        self.sg_dust_bg.attach_to(self.player)
        self.sg_dust_fg.attach_to(self.player)

        self.entity_movement_collision_horizontal(self.player)
        self.entity_movement_collision_vertical(self.player)
        self.entity_on_trigger(self.player)

        self.player_box.center = self.player.rect.center
        # Dust particle generation
        dust_pos = pygame.math.Vector2(random.randint(int(self.player_box.x), int(self.player_box.x + self.player_box.width)),  
                                        random.randint(int(self.player_box.y), int(self.player_box.y + self.player_box.height)))
        if random.random() < 0.01:
            surf =  pygame.Surface((4,4))
            surf.set_colorkey((0,0,0))
            self.particles_dust.append(ParticleDust(dust_pos, surf, self.sg_dust_bg)) if random.random() < 0.5 else self.particles_dust.append(ParticleDust(dust_pos, surf, self.sg_dust_fg))
        for p in self.particles_dust:
            if p.kill:
                self.particles_dust.remove(p)
                p.group.remove(p)

    def draw(self):
        self.canvas.blit(pygame.transform.scale(self.background, (self.canvas.get_size())), (0,0))

        self.sg_dust_bg.render_all(self.canvas)
        self.sg_decor_bg.render_all(self.canvas)
        self.sg_tiles_non_colliders.render_all(self.canvas)
        self.sg_tiles_colliders.render_all(self.canvas)
        self.sg_camera.render_all(self.canvas)
        self.sg_decor_fg.render_all(self.canvas)
        self.sg_dust_fg.render_all(self.canvas)
        self.surface.blit(pygame.transform.scale(self.canvas, (self.surface.get_size())), (0,0))
