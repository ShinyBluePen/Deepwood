import pygame
import settings
import skills


class Creature:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite

        self.description = ""
        self.vitality = 0       # health
        self.spirit = 0         # magical energy
        self.potential = 0      # unspent skill
        self.influence = None   # natural forces affecting
        self.speed = 1
        self.inventory = []
        self.race = None
        self.animal = None
        self.size = 0
        self.sex = None
        self.mask = pygame.mask.from_surface(self.sprite)   # collision

        def examine(description):
            self.description = description

        def draw(self, x, y):
            settings.WINDOW.blit(sprite, x, y)

        def movement(creature):
            creature = pygame.image.load("sprite")
            rect = creature.get_rect()
            speed = creature.speed
            sprite_rect = rect.move(speed)
            if sprite_rect.left < 0 or sprite_rect.right > settings.WIDTH:
                speed[0] = -speed[0]
            if sprite_rect.top < 0 or sprite_rect.bottom > settings.HEIGHT:
                speed[1] = -speed[1]

class Player(Creature):
    def __init__(self, x, y):
        super.__init__(x, y)

    def draw(self, x, y):
        settings.WINDOW.blit(settings.player_sprite, x, y)

    def player_movement(self, keys, player):
        vel = settings.PLAYER_VELOCITY
        WIDTH = settings.WIDTH
        HEIGHT = settings.HEIGHT
        if keys[pygame.K_a] and player.x - vel > 0:  # left
            player.x -= vel
        if keys[pygame.K_d] and player.x + vel + player.get_width() < WIDTH:  # right
            player.x += vel
        if keys[pygame.K_w] and player.y - vel > 0:  # up
            player.y -= vel
        if keys[pygame.K_s] and player.y + vel + player.get_height() < HEIGHT:  # down
            player.y += vel

class Animal(Creature):
    pass

class Deer(Animal):
    if self.sex == male:
        self.description = "A buck deer.  It has a crown of antlers."
    else:
        self.description = "A timid doe deer."

class Bird(Animal):
    self.description = "A colourful songbird.  It is singing a lovely song!"

class Frog(Animal):
    self.description = "A fat frog.  It looks delicious."

class Bear(Animal):
    self.description = "A frightening looking bear."

class Insect(Animal):
    self.description = "A lowly bug.  It might sting you if you try to grab it."

class Slug(Animal):
    self.description = "A slimy slug.  Considered a delicacy to the spider-people."

class Fox(Animal):
    self.description = "A crafty fox."