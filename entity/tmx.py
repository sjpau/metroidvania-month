import pygame
from entity.entity import Entity
from component.graphics import Graphics2D

class Decoration(
        pygame.sprite.Sprite,
        Entity,
        Graphics2D,
        ):
    def __init__(self, position, image, group):
        super().__init__(group)
        self.position = position
        Entity.__init__(self, image, position)
        Graphics2D.__init__(self, image, s_type='tile')
    
    def update(self, dt):
        self.graphics_update_animation(dt)

class Spawner(
    pygame.sprite.Sprite,
    Entity,
):
    def __init__(self, position, image, group, entity_spawn=None, active=True):
        super().__init__(group)
        self.position = position
        Entity.__init__(self, image, position)
        self.image = image
        self.active = active
        self.entity_spawn = entity_spawn

    def spawn(self, handler_entity_spawn):
        if self.active:
            handler_entity_spawn[self.entity_spawn].rect.x = self.rect.x
            handler_entity_spawn[self.entity_spawn].rect.y = self.rect.y

    def update(self, dt):
        pass

class Trigger(
    pygame.sprite.Sprite,
    Entity,
):
    def __init__(self, position, image, group, t_id=0, t_type="", active=True, desired_receiver_id=0, action=""):
        super().__init__(group)
        self.position = position
        Entity.__init__(self, image, position)
        self.image = image
        self.active = active
        self.action = action
        self.type = t_type
        self.t_id = t_id
        self.desired_receiver_id = desired_receiver_id
        self.collider_entities = {}

    def update(self, dt):
        pass
