import pygame
import defs.finals as finals


class State(object):
    def __init__(self, font_small=None, font_large=None, desired_next_state="", name=""):
        self.done = False
        self.quit = False
        self.font_small = font_small
        self.font_large = font_large
        self.next_state = None
        self.name = name
        self.theme = ""
        self.start_playing_music = True
        self.desired_next_state = desired_next_state
        self.state_arg = 0
        self.persist = {}
        self.font = pygame.font.Font(None, 50)
        self.canvas = pygame.Surface((finals.CANVAS_WIDTH, finals.CANVAS_HEIGHT))
        self.surface = pygame.display.get_surface()
        self.ratio_x = (self.surface.get_width() / self.canvas.get_width())
        self.ratio_y = (self.surface.get_height() / self.canvas.get_height())
        self.s_width = self.surface.get_width()
        self.s_height = self.surface.get_height()
        self.canvas_rect = self.canvas.get_rect(center = (self.s_width//2, self.s_height//2))
        self.handle = {
            'player input': True,
            'level update': True,
            'level draw': True,
        }
        self.ready = False
        self.fullscreen = False

    def on_videoresize(self):
        self.surface = pygame.display.get_surface()
        self.s_width = self.surface.get_width()
        self.s_height = self.surface.get_height()
        self.ratio_x = (self.surface.get_width() / self.canvas.get_width())
        self.ratio_y = (self.surface.get_height() / self.canvas.get_height())

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

    def on_exit(self):
        pass

    def preload(self):
        pass

    def update(self, dt):
        pass

    def draw(self):
        pass
