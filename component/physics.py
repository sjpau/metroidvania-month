import pygame

class Physics2D:
    def __init__(self, size, e_type=0, speed=1.5):
        self.size = size
        self.type = e_type
        self.speed = speed
        self.direction = pygame.math.Vector2(0,0)
        self.gravity = 0.1
        self.jump_speed = -1.5

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y +=  self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def movement_horizontal(self):
        self.rect.x += self.direction.x * self.speed
    
    def movement_vertical(self):
        self.apply_gravity()
