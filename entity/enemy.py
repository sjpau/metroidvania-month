import pygame

from entity.entity import Entity
from component.graphics import Graphics2D
from component.combat import Combat
from component.physics import Physics2D
from entity.melee import Melee

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
        mas_h = pygame.Surface((self.image.get_width() * 2, self.image.get_height()))
        mas_h.set_colorkey((0,0,0))
        self.attack_melee_horizontal = Melee(self, mas_h, attack_group, horiznotal=True)

    def update(self, dt):
        if self.want_move['right']:
            self.velocity.x = 1
        if self.want_move['left']:
            self.velocity.x = -1
        if not self.want_move['right'] and not self.want_move['left']:
            self.velocity.x = 0
        self.set_animation('idle')
        self.graphics_update_animation(dt)