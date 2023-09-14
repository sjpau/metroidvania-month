import pygame

from entity.entity import Entity
from component.graphics import Graphics2D
from component.combat import Combat
from component.physics import Physics2D
from entity.melee import Melee
import random
from utils.utils import bool_dict_set_true

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
        self.attack_trigger_rect = pygame.FRect(0,0, self.image.get_width() * 6, self.image.get_height() * 6)

class MeleeBandit(Enemy):
    def __init__(self, position, group, size, image, attack_group=None, animations={}, behaviour='stand', melee_anims={}):
        super().__init__(position, group, size, image, attack_group, animations)
        mas = pygame.Surface((self.image.get_width() * 2, self.image.get_height()))
        mas.set_colorkey((0,0,0))
        self.attack_melee = Melee(self, mas, attack_group, animations=melee_anims, cooldown=100)
        self.walking = False
        self.walking_time = 0

        self.attack_melee.set_attack_hitbox_to_direction(self.attack_direction)
        self.action_defend = False
        self.defend_timer = 200
        self.defend_counter = 0

        self.action_prepare = False

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
        if self.invul:
            self.invul -= 1
        self.attack_trigger_rect.center = self.rect.center
        self.behave()
        if self.want_move['right']:
            self.velocity.x = -0.1
        if self.want_move['left']:
            self.velocity.x = 0.1
        if not self.want_move['right'] and not self.want_move['left']:
            self.velocity.x = 0
        if self.velocity.x != 0:
            self.set_animation('walk')
        else:
            self.set_animation('idle')
        if self.action_defend:
            self.defend_counter += 1
            self.velocity.x = 0
            self.walking = False
            self.want_move['right'] = False
            self.want_move['left'] = False
            self.set_animation('defend') 
        if self.action_prepare and not self.action_defend and not self.attack_melee.cd_counter:
            self.velocity.x = 0
            self.walking = False
            self.want_move['right'] = False
            self.want_move['left'] = False
            self.set_animation('prepare')
            dir_key = [key for key, value in self.direction.items() if value]
            bool_dict_set_true(self.attack_direction,dir_key[0])
        if self.current_animation == self.animations['prepare'] and self.current_animation.done:
            self.action_prepare = False
            self.current_animation.done = False
            self.attack_melee.attack = True
        if self.defend_counter >= self.defend_timer:
            self.defend_counter = 0
            self.action_defend = False
        if self.attack_melee.attack:
            self.set_animation('attack')
            self.attack_melee.count_cooldown = True
        self.attack_melee.set_attack_hitbox_to_direction(self.attack_direction)
        self.graphics_update_animation(dt)