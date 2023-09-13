import pygame
from utils.utils import clip
from math import ceil, sqrt

class Font():
    def __init__(self, path):
        self.spacing = 1
        self.character_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']
        font_img = pygame.image.load(path).convert_alpha()
        font_img.set_colorkey((0, 0, 0))
        current_char_width = 0
        self.characters = {}
        character_count = 0
        for x in range(font_img.get_width()):
            c = font_img.get_at((x, 0))
            if c[0] == 127:
                char_img = clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
                self.characters[self.character_order[character_count]] = char_img.copy()
                character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        self.space_width = self.characters['A'].get_width()
        self.char_width, self.char_height = self.characters['A'].get_size() 

    def calculate_center(self, text, position):
        matrix_size = int(ceil(sqrt(len(text))))
        matrix = [[' ' for _ in range(matrix_size)] for _ in range(matrix_size)]
        for i, char in enumerate(text):
            row = i // matrix_size
            col = i % matrix_size
            matrix[row][col] = char

        matrix_width = sum([self.characters[char].get_width() + self.spacing for char in text if char != ' ']) - self.spacing
        matrix_center_x = position[0] - matrix_width / 2
        matrix_center_y = position[1]    
        return pygame.math.Vector2(matrix_center_x, matrix_center_y)

    def render(self, surf, text, position, center=False):
        x_offset = 0
        if center:
            position = self.calculate_center(text, position)
        x = position[0]
        y = position[1]
        line_height = 0
        for char in text:
            if char != ' ':
                if x + self.char_width > position[0] + surf.get_width():
                    x = position[0]
                    y += line_height
                    line_height = 0
                surf.blit(self.characters[char], (x, y))
                x += self.char_width + self.spacing
                line_height = max(line_height, self.char_height)
            else:
                x += self.space_width + self.spacing