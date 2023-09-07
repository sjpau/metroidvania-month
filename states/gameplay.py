import pygame
from .state import State
import defs.finals as finals
import debug 
from entity.player import Player
from entity.enemy import Enemy
from entity.shadow import ShadowSprite
from entity.background import BackgroundLayer
from render.camera import Camera
import loader.mapper as mapper
from loader.loader import png
from entity.particles import ParticleDust
import random

from loader.assets import sprites_background_layers
from loader.assets import sprites_enemy_melee_bandit
from render.animation import Animation
from loader.loader import load_sprites

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
        self.sg_limits = Camera(self.canvas, self.scale_factor)
        self.sg_enemies = Camera(self.canvas, self.scale_factor)
        self.sg_attack_hitboxes = Camera(self.canvas, self.scale_factor)
        self.sg_shadow_sprites = Camera(self.canvas, self.scale_factor)
        self.sg_background_layers = Camera(self.canvas, self.scale_factor)
        self.sg_camera_groups = [self.sg_tiles_colliders, self.sg_tiles_non_colliders,
                                 self.sg_decor_fg, self.sg_decor_bg,
                                 self.sg_camera, self.sg_triggers,
                                 self.sg_dust_fg, self.sg_dust_bg,
                                 self.sg_spawners, self.sg_attack_hitboxes,
                                 self.sg_shadow_sprites, self.sg_limits,
                                 self.sg_enemies, self.sg_background_layers,]
        self.tmx_tile_layers_to_sg = {
            'colliders': self.sg_tiles_colliders,
            'background': self.sg_tiles_non_colliders,
        }
        self.tmx_obj_layers_to_sg = {
            'decor_fg': self.sg_decor_fg,
            'decor_bg': self.sg_decor_bg,
            'triggers': self.sg_triggers,
            'spawners': self.sg_spawners,
            'camera_limits': self.sg_limits,
        }
        _, _, _, _, self.limits = mapper.unpack_tmx(self.tmx_maps, 'example', 
                                    self.tmx_tile_layers_to_sg, 
                                    self.tmx_obj_layers_to_sg)
        self.player = Player(pygame.math.Vector2(0,0), self.sg_camera, (16, 16),
                            pygame.surface.Surface((finals.tile_size, finals.tile_size)), attack_group=self.sg_attack_hitboxes)
        self.player_box = pygame.FRect(self.canvas.get_rect())
        self.particles_dust = []
        for spawner in self.sg_spawners:
            if spawner.entity_spawn == 'player':
                spawner.spawn_entity(self.player)
            if spawner.entity_spawn == 'melee_bandit':
                animations_enemy_melee_bandit = {
                    'idle': Animation(load_sprites(sprites_enemy_melee_bandit['idle']), 300),
                }
                e = Enemy(pygame.math.Vector2(0,0), self.sg_enemies, (16, 16), pygame.Surface((16,16)), animations=animations_enemy_melee_bandit, attack_group=self.sg_attack_hitboxes)
                spawner.spawn_entity(e)

        self.player_shadow_cd = 40
        self.player_shadow_count = 0

        # Calculate level borders
        min_x = None
        max_x = None
        min_y = None
        max_y = None
        for tile in self.limits:
            x, y, width, height = tile.rect
            if min_x is None or x < min_x:
                min_x = x
            if max_x is None or x + width > max_x:
                max_x = x + width
            if min_y is None or y < min_y:
                min_y = y
            if max_y is None or y + height > max_y:
                max_y = y + height
        for camera in self.sg_camera_groups:
            camera.set_level_borders(min_x, min_y, max_x, max_y)

        # Parallax layers
        factor = 0.001
        for path in sprites_background_layers:
            factor += 0.005
            BackgroundLayer(png(path), pygame.math.Vector2(0,0), self.sg_background_layers, self.player, factor, -5, floor=5)
            

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
            if not entity.on_ground and entity.abilities['slide']:
                entity.velocity.y = min(entity.velocity.y, 0.3)
                entity.jumps = 1

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
        self.sg_attack_hitboxes.update(dt)
        self.sg_shadow_sprites.update(dt)
        self.sg_limits.update(dt)
        self.sg_enemies.update(dt)
        self.sg_background_layers.update(dt)

        self.sg_camera.attach_to(self.player)
        self.sg_tiles_colliders.attach_to(self.player)
        self.sg_tiles_non_colliders.attach_to(self.player)
        self.sg_decor_bg.attach_to(self.player)
        self.sg_decor_fg.attach_to(self.player)
        self.sg_triggers.attach_to(self.player)
        self.sg_spawners.attach_to(self.player)
        self.sg_dust_bg.attach_to(self.player)
        self.sg_dust_fg.attach_to(self.player)
        self.sg_attack_hitboxes.attach_to(self.player)
        self.sg_shadow_sprites.attach_to(self.player)
        self.sg_limits.attach_to(self.player)
        self.sg_enemies.attach_to(self.player)

        self.entity_movement_collision_horizontal(self.player)
        self.entity_movement_collision_vertical(self.player)
        self.entity_on_trigger(self.player)

        # Player logic
        if self.player.attack_melee.attack:
            self.player.attack_melee.hit(self.sg_enemies)
            # TODO add "deal damage" logic

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
        
        for s in self.sg_shadow_sprites:
            if s.kill == True:
                self.sg_shadow_sprites.remove(s)
        # Cool dashing animation
        if self.player.in_dash:
            ShadowSprite(self.player, self.sg_shadow_sprites, finals.COLOR_HERO_GREEN)

    def draw(self):
        #self.canvas.blit(pygame.transform.scale(self.background, (self.canvas.get_size())), (0,0))
        self.canvas.blit(self.background, (0,0))
        for sprite in self.sg_background_layers.sprites():
            self.canvas.blit(sprite.image, sprite.rect.topleft)

        self.sg_dust_bg.render_all(self.canvas)
        self.sg_decor_bg.render_all(self.canvas)
        self.sg_tiles_non_colliders.render_all(self.canvas)
        self.sg_tiles_colliders.render_all(self.canvas)
        self.sg_shadow_sprites.render_all(self.canvas)
        self.sg_camera.render_all(self.canvas)
        self.sg_decor_fg.render_all(self.canvas)
        self.sg_dust_fg.render_all(self.canvas)
        self.sg_limits.render_all(self.canvas)
        self.sg_enemies.render_all(self.canvas)
        self.sg_attack_hitboxes.render_all(self.canvas)
        self.surface.blit(pygame.transform.scale(self.canvas, (self.surface.get_size())), (0,0))
