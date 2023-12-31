import pygame
from entity.entity import Entity
from component.graphics import Graphics2D
from defs.finals import COLOR_BEIGE

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
    def __init__(self, position, image, group, t_id=0, entity_spawn=None, active=True):
        super().__init__(group)
        self.position = position
        Entity.__init__(self, image, position)
        self.image = image
        self.active = active
        self.entity_spawn = entity_spawn
        self.t_id = t_id

    def spawn_entity(self, entity):
        if self.active:
            entity.rect.x = self.rect.x
            entity.rect.y = self.rect.y

    def update(self, dt):
        pass

class Trigger(
    pygame.sprite.Sprite,
    Entity,
):
    def __init__(self, position, image, group, t_id=0, t_type="", active=True, desired_receiver_id=0, action="", action_receiver=""):
        super().__init__(group)
        self.position = position
        Entity.__init__(self, image, position)
        self.image = image
        self.active = active
        self.action = action
        self.type = t_type
        self.t_id = t_id
        self.desired_receiver_id = desired_receiver_id
        self.action_receiver = action_receiver

    def update(self, dt):
        pass

class Limit(
    pygame.sprite.Sprite,
    Entity,
):
    def __init__(self, position, image, group, limit_on):
        super().__init__(group)
        self.position = position
        Entity.__init__(self, image, position)
        self.image = image
        self.limit_on = limit_on
    
    def update(self, dt):
        pass

class Wall(
    pygame.sprite.Sprite,
    Entity,
):
    def __init__(self, position, image, group, climable=False):
        super().__init__(group)
        self.position = position
        Entity.__init__(self, image, position)
        self.image = image
        self.climable = climable

    def update(self, dt):
        pass

class Spike(
    pygame.sprite.Sprite,
    Entity,
):
    def __init__(self, position, image, group):
        super().__init__(group)
        self.position = position
        Entity.__init__(self, image, position)
        self.image = image
    
    def update(self, dt):
        pass

class Pickup(
    pygame.sprite.Sprite,
    Entity,
):
    def __init__(self, position, image, group, active=True, ability=""):
        super().__init__(group)
        self.position = position
        Entity.__init__(self, image, position)
        self.image = image
        self.active = active
        self.ability = ability

    def update(self, dt):
        pass

class TextObject(
    pygame.sprite.Sprite,
    Entity,
):
    def __init__(self, position, image, group, text, font, color=COLOR_BEIGE):
        super().__init__(group)
        self.position = position
        Entity.__init__(self, image, position)
        self.image = image
        self.text = text
        self.font = font
        self.font.change_color(color)

    def update(self, dt):
        pass