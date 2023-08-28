import pygame

class Physics2D:
    def __init__(self, size, e_type=0, speed=1):
        self.size = size
        self.type = e_type
        self.speed = speed
        self.velocity = pygame.math.Vector2(0,0)
        self.gravity = 0.1
        self.jump_speed = -2.5
        self.jumps = 1

    def apply_gravity(self):
        self.velocity.y += self.gravity
        self.rect.y +=  self.velocity.y

    def jump(self):
        if self.jumps > 0:
            self.velocity.y = self.jump_speed
            self.jumps -= 1

    def movement_horizontal(self):
        self.rect.x += self.velocity.x * self.speed
    
    def movement_vertical(self):
        self.apply_gravity()
