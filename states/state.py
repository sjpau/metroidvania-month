import pygame
import defs.finals as finals


class State(object):
    def __init__(self):

        self.done = False
        self.quit = False
        self.next_state = None
        self.theme = ""
        self.start_playing_music = True
        self.desired_next_state = ""
        self.state_arg = 0
        self.persist = {}
        self.font = pygame.font.Font(None, 50)
        self.canvas = pygame.Surface((finals.CANVAS_WIDTH, finals.CANVAS_HEIGHT))

        self.surface = pygame.display.get_surface()
        self.s_width = self.surface.get_width()
        self.s_height = self.surface.get_height()
        self.scale_factor = min(self.s_width//finals.CANVAS_WIDTH, self.s_height//finals.CANVAS_HEIGHT)
        self.canvas = pygame.transform.scale(self.canvas, (finals.CANVAS_WIDTH*self.scale_factor, finals.CANVAS_HEIGHT*self.scale_factor))
        self.canvas_rect = self.canvas.get_rect(center = (self.s_width//2, self.s_height//2))
    
    def on_videoresize(self):
        self.surface = pygame.display.get_surface()
        self.s_width = self.surface.get_width()
        self.s_height = self.surface.get_height()
        self.scale_factor = min(self.s_width//finals.CANVAS_WIDTH, self.s_height//finals.CANVAS_HEIGHT)
        #self.canvas = pygame.transform.scale(self.canvas, (finals.CANVAS_WIDTH*self.scale_factor, finals.CANVAS_HEIGHT*self.scale_factor))
        #self.canvas_rect = self.canvas.get_rect(center = (self.s_width//2, self.s_height//2))

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def manage_music(self):
        if self.start_playing_music and self.theme != "":
#            pygame.mixer.music.load(finals.music_path + self.theme)
#            pygame.mixer.music.play(-1)
#TODO: finish when adding music
            self.start_playing_music = False

    def on_enter(self):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass