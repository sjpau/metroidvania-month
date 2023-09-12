import pygame

class Parallax:
    def __init__(self, factor, ceil, floor=None):
        self.factor = factor
        self.ceil = ceil
        self.floor = floor
        self.offset = 0.0

    def attach_parallax(self, target):
        self.offset = (self.rect.y + target.rect.y) * self.factor
        self.offset = min(self.offset, self.floor)
        self.offset = max(self.offset, self.ceil)
        self.rect.y = self.offset