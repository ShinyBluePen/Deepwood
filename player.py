
import pygame

from settings import *
from creature import Creature


class Player(Creature):
    def __init__(self, pos, groups, obstacle_sprites, sprite):
        super().__init__(pos, groups, sprite)
        self.speed = PLAYER_VELOCITY
        self.obstacles  = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        # y
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        # x
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        # todo: Other input functionality such as [m] for menu, [i] for inventory, etc.

    def update(self):
        self.input()
        self.movement()

        # if keys[pygame.K_a] and self.x - self.speed > 0:
        #     self.x -= self.speed    # Right
        # if keys[pygame.K_d] and self.x + self.speed + self.sprite.get_width() < WIDTH:
        #     self.x += self.speed    # up
        # if keys[pygame.K_w] and self.y - self.speed > 0:
        #     self.y -= self.speed    # down
        # if keys[pygame.K_s] and self.y + self.speed + self.sprite.get_height() < HEIGHT:
        #     self.y += self.speed