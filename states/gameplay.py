import pygame
from .state import State
import defs.finals as finals
from entity.player import Player
from render.camera import Camera

class Gameplay(State):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.sg_camera = Camera(self.canvas, self.scale_factor)
        self.player = Player([0,0], self.sg_camera, (32, 32),
                            pygame.surface.Surface((finals.tile_size, finals.tile_size)))

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.VIDEORESIZE:
            self.on_videoresize()

    def update(self, dt):
        self.sg_camera.update(dt)
        self.sg_camera.attach_to(self.player)

    def draw(self):
        self.surface.blit(pygame.transform.scale(self.canvas, (self.surface.get_size())), (0,0))
        self.canvas.fill(finals.COLOR_GREEN_SUBTLE)
        self.sg_camera.render_all(self.canvas)
