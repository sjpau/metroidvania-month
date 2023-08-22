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
        self.sg_fg_decors = Camera(self.canvas, self.scale_factor)
        self.sg_bg_decors = Camera(self.canvas, self.scale_factor)
        self.sg_camera_groups = [self.sg_tiles_colliders, self.sg_tiles_non_colliders,
                                 self.sg_fg_decors, self.sg_bg_decors,
                                 self.sg_camera]
        self.tmx_layers_to_sg = { # TODO: better naming of tmx layers
            'colliders_1': self.sg_tiles_colliders,
            'background_1': self.sg_tiles_non_colliders,
        }
        self.tiles = mapper.unpack_tmx(self.tmx_maps, 'example', self.tmx_layers_to_sg)
        self.player = Player(pygame.math.Vector2(0,0), self.sg_camera, (16, 16),
                            pygame.surface.Surface((finals.tile_size, finals.tile_size)))

    def horizontal_tile_collision(self):  # TODO: MOVE TO LEVEL class
        self.player.rect.x += self.player.direction.x * self.player.speed
        for hit in pygame.sprite.spritecollide(self.player, self.sg_tiles_colliders, False):
            if self.player.direction.x < 0:
                self.player.rect.left = hit.rect.right
            elif self.player.direction.x > 0:
                self.player.rect.right = hit.rect.left
            self.player.position = pygame.math.Vector2(self.player.rect.topleft)

    def vertical_tile_collision(self):
        for hit in pygame.sprite.spritecollide(self.player, self.sg_tiles_colliders, False):
            if self.player.direction.y > 0:
                self.player.rect.bottom = hit.rect.top
                self.player.direction.y = 0
            elif self.player.direction.y < 0:
                self.player.rect.top = hit.rect.bottom
            self.player.position = pygame.math.Vector2(self.player.rect.topleft)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.VIDEORESIZE:
            self.on_videoresize()

    def update(self, dt):
        # Update Sprite groups
        self.sg_camera.update(dt)
        self.sg_tiles_colliders.update(dt)
        self.sg_tiles_non_colliders.update(dt)
        self.sg_camera.attach_to(self.player)
        self.sg_tiles_colliders.attach_to(self.player)
        self.sg_tiles_non_colliders.attach_to(self.player)
        self.horizontal_tile_collision()
        self.vertical_tile_collision()

    def draw(self):
        self.canvas.fill(finals.COLOR_GREEN_SUBTLE)
        # Draw Sprite groups
        self.sg_tiles_non_colliders.render_all(self.canvas)
        self.sg_tiles_colliders.render_all(self.canvas)
        self.sg_camera.render_all(self.canvas)
        self.surface.blit(pygame.transform.scale(self.canvas, (self.surface.get_size())), (0,0))
