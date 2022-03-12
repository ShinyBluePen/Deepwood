
import pygame

from settings import *


class Creature(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite):
        super().__init__(groups)
        # Object attributes
        self.image      = sprite
        self.rect       = self.image.get_rect(topleft = pos)
        self.direction  = pygame.math.Vector2()
        self.location   = None
        self.mask       = pygame.mask.from_surface(self.image)
        self.hitbox = self.rect.inflate(-10, -10)

        # Resource attributes
        self.vitality     = 0   # health
        self.spirit       = 0   # magical energy
        self.potential    = 0   # unspent skill
        self.influence    = {}  # natural forces influencing creature.  Dictionary is {influence: weight}
        # Stat attributes
        self.luck         = 1   #   Influences include: (white  ) (Fate     )  MTG 4c factions:  MTG faction characteristics:
        self.speed        = 1   #       POWER           (yellow ) (Momentum )   Altruism          w  morality    /order      /peace      /rigid
        self.dexterity    = 1   #       SIN             (green  ) (Freedom  )   Growth            u  logic       /technology /knowledge
        self.strength     = 1   #       ORDER           (grey   ) (Power    )   Artifice          b  selfishness /pain       /sacrifice
        self.constitution = 1   #       GROWTH          (red    ) (Hunger   )   Chaos             r  impulse     /chaos      /freedom
        self.intelligence = 1   #       SPIRIT          (blue   ) (Logic    )   Aggression        g  instinct    /growth     /change
        self.charisma     = 1   #                       (purple ) (Emotion  )   Domain(5c)

        # Characteristic attributes
        self.inventory   = {}  # Dictionary.  Dictionary is {item: amount}
        self.race        = ""
        self.animal      = ""
        self.mutation    = ""
        self.size        = 0
        self.savagery    = 1
        self.sex         = random.choice(["male", "female"])
        self.description = ""

    def get_location(self):
        self.location = None

    def get_description(self):
        print(self.description)

    def draw(self):
        pygame.Surface.blit(WINDOW, self.image, (self.x, self.y))
        pygame.display.update()

    def movement(self):
        # if self.direction.magnitude() != 0:
        #     self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * self.speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * self.speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center

        # self.rect.center += self.direction * self.speed

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # left
                        self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # up
                        self.hitbox.top = sprite.hitbox.bottom


        #creature_rect = self.rect.move(speed)

        # Prevent creature from moving out of bounds.
        # if creature_rect.rect.left < 0 or creature_rect.rect.right > WIDTH:
        #     speed[0] = -speed[0]
        # if creature_rect.rect.top < 0 or creature_rect.rect.bottom > HEIGHT:
        #     speed[1] = -speed[1]