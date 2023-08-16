import pygame

class Physics2D:
    def __init__(self, position, size, e_type=0):
        self.position = position
        self.size = size
        self.type = e_type
        self.velocity = [0, 0]
        self.movement = [False, False]

    def p2d_update(self):
        frame_movement = (self.movement[0] + self.velocity[0], self.movement[1] + self.velocity[1])
        self.position[0] += frame_movement[0]
        self.position[1] += frame_movement[1]
