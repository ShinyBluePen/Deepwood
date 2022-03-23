
from settings import *
#   pygame
#   random
#   time
#   sys
#   os.path.join() as jn

from data import GRAPHICS


class Item:
    def __init__(self):
        self.consumable = ""
        self.charm = ""
        self.armor = ""
        self.weapon = ""
        self.jewelry = ""

    def consumable(self):
        pass

    def charm(self):
        pass

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.status.split("_")[0]  # take first index of split method which is the direction string
        self.sprite_type = "weapon"
        # graphics
        # self.image = GRAPHICS["weapons"][player.weapon][]

        # placement
        if direction == "right":
            self.image = GRAPHICS["weapons"][player.weapon][3]
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0, 16))
        elif direction == "left":
            self.image = GRAPHICS["weapons"][player.weapon][2]
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0, 16))
        elif direction == "up":
            self.image = GRAPHICS["weapons"][player.weapon][4]
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(-12, 0))
        else:  # direction == "down"
            self.image = GRAPHICS["weapons"][player.weapon][0]
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-12, 0))

class Equipment(Item):
    def __init__(self):
        super().__init__()

    def weapon(self):
        pass

    def armor(self):
        pass

    def jewelry(self):
        pass
