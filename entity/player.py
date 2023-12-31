import pygame
from component.graphics import Graphics2D
from component.physics import Physics2D
from component.combat import Combat
from entity.entity import Entity
from entity.melee import Melee
from render.animation import Animation
import loader.assets as assets
import loader.loader as loader
from utils.utils import bool_dict_set_true

class Player(
    pygame.sprite.Sprite,
    Entity,
    Graphics2D,
    Physics2D,
    Combat,
    ):
    def __init__(self, position, group, size, image, attack_group=None):
        super(Player, self).__init__(group)
        animations = {
            'idle': Animation(loader.load_sprites(assets.sprites_player['idle']), 300),
            'run': Animation(loader.load_sprites(assets.sprites_player['run']), 70),
            'dash': Animation(loader.load_sprites(assets.sprites_player['dash']), 40),
            'up': Animation(loader.load_sprites(assets.sprites_player['up']), 100),
            'down': Animation(loader.load_sprites(assets.sprites_player['down']), 100),
            'attack_hor': Animation(loader.load_sprites(assets.sprites_player['attack_hor']), 100),
        }
        Entity.__init__(self, image, position)
        Graphics2D.__init__(self, image, animations=animations)
        Physics2D.__init__(self, size)
        Combat.__init__(self, size)
        self.group = group
        self.want_move = {
            'right': False,
            'left': False,
        }
        self.keys_right = {pygame.K_RIGHT, pygame.K_l, pygame.K_d}
        self.keys_left = {pygame.K_LEFT, pygame.K_h, pygame.K_a}
        self.keys_up = {pygame.K_UP, pygame.K_k, pygame.K_w}
        self.keys_down = {pygame.K_DOWN, pygame.K_j, pygame.K_s}
        self.keys_jump = {pygame.K_SPACE}
        self.keys_attack = {pygame.K_q}
        self.keys_dash = {pygame.K_LSHIFT}

        mas = pygame.Surface((self.image.get_width()*2, self.image.get_height()))
        mas.set_colorkey((0,0,0))
        attack_anims = {
            'slash': Animation(loader.load_sprites(assets.sprites_player_slash['slash']), 50, play_once=True),
            'slash_ver': Animation(loader.load_sprites(assets.sprites_player_slash['slash_ver']), 50, play_once=True),
        }
        self.attack_melee = Melee(self, mas, attack_group, animations=attack_anims)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            k = event.key
            if k in self.keys_right:
                self.want_move['right'] = True
                bool_dict_set_true(self.attack_direction,'right')
            elif k in self.keys_left:
                self.want_move['left'] = True
                bool_dict_set_true(self.attack_direction,'left')
            elif k in self.keys_dash:
                if self.abilities['dash']:
                    self.dash(self.attack_direction)
        if event.type == pygame.KEYUP:
            k = event.key
            if k in self.keys_jump:
                self.jump()
            elif k in self.keys_right:
                self.want_move['right'] = False
            elif k in self.keys_left:
                self.want_move['left'] = False
            elif k in self.keys_attack:
                if not self.attack_melee.cd_counter:
                    self.attack_melee.attack = True


    def update(self, dt):
        if self.invul:
            self.invul -= 1
            #TODO show some invulnerability thingy
        if pygame.mouse.get_pressed()[0] and not self.attack_melee.cd_counter:
            self.attack_melee.attack = True
        if self.want_move['right']:
            self.velocity.x = 1
        if self.want_move['left']:
            self.velocity.x = -1
        if not self.want_move['right'] and not self.want_move['left']:
            self.velocity.x = 0
        self.attack_melee.set_attack_hitbox_to_direction(self.attack_direction)
        self.dash_update()
        if self.velocity.y < 0:
            self.set_animation('up')
        elif self.velocity.y > 0:
            self.set_animation('down')
        if self.velocity.x != 0 and self.velocity.y == 0 and not self.in_dash:
            self.set_animation('run')
        if self.in_dash:
            self.set_animation('dash')
        if self.velocity.x == 0 and self.velocity.y == 0:
            self.set_animation('idle')
        if self.attack_melee.attack:
            self.set_animation('attack_hor')
        self.graphics_update_animation(dt)