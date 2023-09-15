import pygame
import debug
from defs.lvl import states


class Game(object):

    def __init__(self, state):
        self.done = False
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.state = state
        self.desired_next_state = self.state.desired_next_state

    def event_loop(self):
        for event in pygame.event.get():
            self.state.get_event(event)

    def flip_state(self, state):
        self.state.on_exit()
        state.preload(player_persistent_data=self.state.player_persistent_data)
        if state.ready:
            self.state.done = False
            persistent = self.state.persist
            self.state = state
            self.state.startup(persistent)
            self.state.on_enter()

    def update(self, dt):
        self.desired_next_state = self.state.desired_next_state
        if self.state.quit:
            self.state.player_persistent_data.save()
            self.done = True
        elif self.state.done:
            self.state.done = False
            self.flip_state(states[self.desired_next_state])
            self.switch_music = True
        if self.state.handle['level update']:
            self.state.update(dt)

    def draw(self):
        if self.state.handle['level draw']:
            self.state.draw()
        if debug.status:
            debug.display(int(self.clock.get_fps()))

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.update()
