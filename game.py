import pygame
import debug


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
        self.state.done = False
        persistent = self.state.persist
        self.state = state
        self.state.startup(persistent)
        self.state.on_enter()

    def update(self, dt):
        self.desired_next_state = self.state.desired_next_state
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state(self.desired_next_state)
            self.switch_music = True
        self.state.update(dt)

    def draw(self):
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
