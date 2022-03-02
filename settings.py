import pygame
import os
import time
import random


#################
# Set constants #
#################

WIDTH = 600
HEIGHT = 600
WINDOW = pygame.display.set_mode(WIDTH, HEIGHT)

FPS = 60
CLOCK = pygame.time.Clock()

PLAYER_VELOCITY = 5
AREA = ""

###############
# Load Assets #
###############

# World sprites (trees / rocks / etc)


# Character sprites
player_sprite = pygame.image.load(os.path.join("Assets", "filename"))

# Race sprites
human_race_sprite = pygame.image.load(os.path.join("Assets", "filename"))
slug_race_sprite = pygame.image.load(os.path.join("Assets", "filename"))
fox_race_sprite = pygame.image.load(os.path.join("Assets", "filename"))
bird_race_sprite = pygame.image.load(os.path.join("Assets", "filename"))
frog_race_sprite = pygame.image.load(os.path.join("Assets", "filename"))
spider_race_sprite = pygame.image.load(os.path.join("Assets", "filename"))

# Creature sprites
deer_sprite = pygame.image.load(os.path.join("Assets", "filename"))
bear_sprite = pygame.image.load(os.path.join("Assets", "filename"))
bird_sprite = pygame.image.load(os.path.join("Assets", "filename"))
frog_sprite = pygame.image.load(os.path.join("Assets", "filename"))
fox_sprite = pygame.image.load(os.path.join("Assets", "filename"))
insect_sprite = pygame.image.load(os.path.join("Assets", "filename"))
slug_sprite = pygame.image.load(os.path.join("Assets", "filename"))

# Non-creature sprites (items / skills(icons) / etc)


# Effect sprites (lighting / skills(effects) / etc)


# Audio


#


