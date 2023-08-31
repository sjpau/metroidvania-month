import pygame 
from entity.entity import Entity
from component.graphics import Graphics2D

class Melee(
    pygame.sprite.Sprite,
    Entity,
    Graphics2D,
):
    def __init__(self, parent, image, group, horiznotal=True, animations={}):
        super().__init__(group)
        self.parent = parent
        self.position = pygame.math.Vector2(parent.rect.topleft)
        Entity.__init__(self, image, self.position)
        Graphics2D.__init__(self, image, animations=animations)
        self.animations = animations
        self.attack = False
        self.horizontal = horiznotal # Means left or right attack, False for top-down attacks. 
        self.flipped = False

    def set_attack_hitbox_to_direction(self, attack_direction):
        if self.horizontal:
            if attack_direction['left']:
                self.rect.bottomright = self.parent.rect.bottomright
                if not self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.flipped = True
            elif attack_direction['right']:
                self.rect.topleft = self.parent.rect.topleft # This sort of requires parent width to be same as attack box on for other directions respectively
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.flipped = False
        else:
            if attack_direction['up']:
                self.rect.bottomright = self.parent.rect.bottomright
                if self.flipped:
                    self.image = pygame.transform.flip(self.image, False, True)
                    self.flipped = False
            if attack_direction['down']:
                self.rect.topleft = self.parent.rect.topleft 
                if not self.flipped:
                    self.image = pygame.transform.flip(self.image, False, True)
                    self.flipped = True

    def update(self, dt):
        pass