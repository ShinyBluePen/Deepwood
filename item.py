
import pygame

from settings import *


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

class Equipment(Item):
    def __init__(self):
        super().__init__()

    def weapon(self):
        pass

    def armor(self):
        pass

    def jewelry(self):
        pass

