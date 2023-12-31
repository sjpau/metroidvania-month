import pygame 
from entity.entity import Entity
from component.graphics import Graphics2D
from utils.utils import bool_dict_set_true

class Melee(
    pygame.sprite.Sprite,
    Entity,
    Graphics2D,
):
    def __init__(self, parent, image, group, animations={}, cooldown=10):
        super().__init__(group)
        self.parent = parent
        self.position = pygame.math.Vector2(parent.rect.topleft)
        Entity.__init__(self, image, self.position)
        Graphics2D.__init__(self, image, animations=animations)
        self.animations = animations
        self.attack = False
        self.want_be_flipped_ver = True
        self.count_cooldown = False
        self.cd_counter = 0
        self.cooldown = cooldown
        self.rect.x = -1000
        self.rect.y = -1000

    def set_attack_hitbox_to_direction(self, attack_direction):
        if attack_direction['left']:
            self.rect.topright = self.parent.rect.topright
            bool_dict_set_true(self.direction, 'left')
        elif attack_direction['right']:
            self.rect.topleft = self.parent.rect.topleft # This sort of requires parent width to be same as attack box on for other directions respectively
            bool_dict_set_true(self.direction, 'right')
        if attack_direction['up']:
            self.rect.bottomleft = self.parent.rect.topleft
            bool_dict_set_true(self.direction, 'up')
        if attack_direction['down']:
            self.rect.bottomleft = self.parent.rect.bottomleft 
            bool_dict_set_true(self.direction, 'down')

    def hit(self, sg_colliders):
        hits = pygame.sprite.spritecollide(self, sg_colliders, False)
        sprites_hit = []
        for h in hits:
            if pygame.sprite.collide_mask(self, h):
                sprites_hit.append(h)
        return sprites_hit

    def update(self, dt):
        if self.count_cooldown:
            self.cd_counter += 1
            if self.cd_counter >= self.cooldown:
                self.cd_counter = 0
                self.count_cooldown = False
        if self.current_animation is not None:
            if self.current_animation.done:
                self.attack = False
                self.current_animation = None
                self.image.set_alpha(0)
        if self.attack:
            self.count_cooldown = True
            self.set_animation('slash')
            self.image.set_alpha(255)
            self.current_animation.done = False

        
        self.graphics_update_animation(dt)