import pygame
from states.state import State
from ui.buttons import ButtonDefault

class MainMenu(State):
    def __init__(self, save_data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = [ # TODO add settings
            'Play',
            'Credits',
            'Exit',
        ]
        self.choice_current = 0
        self.anchors = {
            'topleft':  (20, 20),
            'center':   (self.canvas.get_width()/2, self.canvas.get_height()/2),
        }
        self.player_persistent_data = save_data
        self.buttons = []
        x = self.anchors['topleft'][0]
        y = self.anchors['topleft'][1]
        self.font_small.change_color('white')
        for choice in self.choices:
            self.buttons.append(ButtonDefault((x, y), choice, self.font_small.char_width, self.font_small.char_height, fixed_width=50))
            y += self.font_small.char_height + 13

    def check_choices(self):
        for butt in self.buttons:
            if butt.active:
                if butt.text == self.choices[0]:
                    self.done = True
                if butt.text == self.choices[1]:
                    pass
                if butt.text == self.choices[2]:
                    self.quit = True

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.VIDEORESIZE:
            self.on_videoresize()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.check_choices()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                self.desired_next_state = self.player_persistent_data.current_area
                self.check_choices()
    
    def update(self, dt):
        pos = list(pygame.mouse.get_pos())
     # take the mouse position and scale it, too
        scaled_pos = (pos[0] / self.ratio_x, pos[1] / self.ratio_y)
        for button in self.buttons:
            self.font_small.render(button.surf, button.text, (0,0))
            if button.padding_rect.collidepoint(scaled_pos):
                button.active = True
            else:
                button.active = False


    def draw(self):
        self.canvas.fill((0, 0, 0))
        for button in self.buttons:
            button.draw(self.canvas)
        try: # NOTE ???
            self.surface.blit(pygame.transform.scale(self.canvas, (self.surface.get_size())), (0,0))
        except Exception as e:
            print(e, self.surface.get_size()) 
            print('Ooops... Something went terribly wrong! Trying to get screen size again.')
            self.surface = pygame.display.get_surface()


