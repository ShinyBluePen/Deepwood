
import pygame

from settings import *
from creature import Creature

class Civilization(Creature):
    def __init__(self, pos, groups, sprite):
        super().__init__(pos, groups, sprite)