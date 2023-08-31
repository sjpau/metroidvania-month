import pygame
from component.graphics import Graphics2D
from component.physics import Physics2D
from component.combat import Combat
from entity.entity import Entity
from entity.melee import Melee
from render.animation import Animation
import loader.assets as assets
import loader.loader as loader

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
        }
        self.on_ground = False
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
        self.keys_attack = {pygame.K_n}

        mas_h = pygame.Surface((self.image.get_width() * 2, self.image.get_height()))
      #  mas_h.set_colorkey((0,0,0))
        mas_v = pygame.Surface((self.image.get_width(), self.image.get_height() * 2))
      #  mas_v.set_colorkey((0,0,0))
        self.attack_melee_horizontal = Melee(self, mas_h, attack_group, horiznotal=True)
        self.attack_melee_vertical = Melee(self, mas_v, attack_group, horiznotal=False)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            k = event.key
            if k in self.keys_right:
                self.want_move['right'] = True
                self.set_attack_direction('right')
            elif k in self.keys_left:
                self.want_move['left'] = True
                self.set_attack_direction('left')
            elif k in self.keys_down:
                self.set_attack_direction('down')
            elif k in self.keys_up:
                self.set_attack_direction('up')
        if event.type == pygame.KEYUP:
            k = event.key
            if k in self.keys_jump:
                self.jump()
            elif k in self.keys_right:
                self.want_move['right'] = False
            elif k in self.keys_left:
                self.want_move['left'] = False
            elif k in self.keys_attack:
                pass
                #self.attack()


    def update(self, dt):
        if self.want_move['right']:
            self.velocity.x = 1
        if self.want_move['left']:
            self.velocity.x = -1
        if not self.want_move['right'] and not self.want_move['left']:
            self.velocity.x = 0
        print(self.attack_melee_horizontal.image)
        self.attack_melee_horizontal.set_attack_hitbox_to_direction(self.attack_direction)
        self.attack_melee_vertical.set_attack_hitbox_to_direction(self.attack_direction)

        if self.velocity.x != 0 and self.velocity.y == 0:
            self.set_animation('run')
        else:
            self.set_animation('idle')
        self.graphics_update_animation(dt)
