import pygame

from entity.entity import Entity
from component.graphics import Graphics2D
from component.combat import Combat
from component.physics import Physics2D
from entity.melee import Melee
import random

class Enemy(
    pygame.sprite.Sprite,
    Entity,
    Graphics2D,
    Combat,
    Physics2D,
):
    def __init__(self, position, group, size, image, attack_group=None, animations={}):
        super().__init__(group)
        Entity.__init__(self, image, position)
        Graphics2D.__init__(self, image, animations=animations)
        Physics2D.__init__(self, size)
        Combat.__init__(self, size)
        self.group = group
        self.want_move = {
            'right': False,
            'left': False,
        }

class MeleeBandit(Enemy):
    def __init__(self, position, group, size, image, attack_group=None, animations={}, behaviour='stand'):
        super().__init__(position, group, size, image, attack_group, animations)
        mas = pygame.Surface((self.image.get_width(), self.image.get_height()))
        mas.set_colorkey((0,0,0))
        self.attack_melee = Melee(self, mas, attack_group)
        self.walking = False
        self.walking_time = 0

    def behave(self):
        if self.walking:
            if self.walking_time > 0:
               self.walking_time -= 1
            else:
                self.walking = False
                self.want_move['right'] = False
                self.want_move['left'] = False
        elif random.random() < 0.01:
            self.walking_time = random.randint(10, 500) 
            self.walking = True
            if random.random() > 0.6:
                self.want_move['right'] = True
                self.want_move['left'] = False
            else:
                self.want_move['right'] = False
                self.want_move['left'] = True


    def update(self, dt):
        self.behave()
        if self.want_move['right']:
            self.velocity.x = -0.1
        if self.want_move['left']:
            self.velocity.x = 0.1
        if not self.want_move['right'] and not self.want_move['left']:
            self.velocity.x = 0
        self.set_animation('idle')
        self.graphics_update_animation(dt)