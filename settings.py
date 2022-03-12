
import pygame

import random
import time
import sys
import os


#################
# Set constants #
#################

# Game settings
WIDTH       = 900
HEIGHT      = 600
WINDOW      = pygame.display.set_mode((WIDTH, HEIGHT))
ICON        = pygame.display.set_icon(pygame.image.load(os.path.join("Assets", "tree.png")))
SPLASH_LIST = random.choice([
    "It's deep!",
    "Hello World!",
    "I'm lumber, Jack!",
    "Are you ready?"
    ])
MAIN_MENU_SPLASH = pygame.display.set_caption(f"Deepwood - {SPLASH_LIST}")

FPS      = 60
CLOCK    = pygame.time.Clock()
TILESIZE = 64

PLAYER_VELOCITY = 2
LOCATION_LIST = [
    "The Coast",
    "Forest Fringes",
    "Viridian Deep",
    "Gloom Woods",
    "Abyssal Depths"
    ]

# Map
#   x = rock
#   p = player
WORLD_MAP = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]

# Colour settings
TEXT_COLOR             = '#EEEEEE'
UI_BG_COLOR            = '#222222'
UI_BORDER_COLOR        = '#111111'
WATER_COLOR            = '#71ddee'
HEALTH_COLOR           = 'red'
ENERGY_COLOR           = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# UI settings
BAR_HEIGHT       = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE    = 80
UI_FONT          = '../graphics/font/joystix.ttf'
UI_FONT_SIZE     = 18

# Menu settings
#   upgrade menu
TEXT_COLOR_SELECTED       = '#111111'
BAR_COLOR                 = '#EEEEEE'
BAR_COLOR_SELECTED        = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

###########################
# Load Assets as surfaces #
###########################

SPRITE_SIZE = (60, 60)

# Empty sprite
blank_sprite = pygame.image.load(os.path.join("Assets", "blank.png")).convert_alpha()

# World sprites (trees / rocks / etc)
tree_sprite = pygame.image.load(os.path.join("Assets", "tree.png")).convert_alpha()
rock_sprite = pygame.image.load(os.path.join("Assets", "rock.png")).convert_alpha()

# Character sprites
player_sprite = pygame.image.load(os.path.join("Assets", "player.png")).convert_alpha()

# Race sprites
human_race_sprite   = pygame.image.load(os.path.join("Assets", "civ_human.png")).convert_alpha()
slug_race_sprite    = pygame.image.load(os.path.join("Assets", "civ_slug.png")).convert_alpha()
fox_race_sprite     = pygame.image.load(os.path.join("Assets", "civ_fox.png")).convert_alpha()
bird_race_sprite    = pygame.image.load(os.path.join("Assets", "civ_bird.png")).convert_alpha()
frog_race_sprite    = pygame.image.load(os.path.join("Assets", "civ_frog.png")).convert_alpha()
spider_race_sprite  = pygame.image.load(os.path.join("Assets", "civ_spider.png")).convert_alpha()

# Creature sprites
deer_sprite     = pygame.image.load(os.path.join("Assets", "deer.png")).convert_alpha()
bear_sprite     = pygame.image.load(os.path.join("Assets", "bear.png")).convert_alpha()
bird_sprite     = pygame.image.load(os.path.join("Assets", "bird.png")).convert_alpha()
frog_sprite     = pygame.image.load(os.path.join("Assets", "frog.png")).convert_alpha()
fox_sprite      = pygame.image.load(os.path.join("Assets", "fox.png")).convert_alpha()
insect_sprite   = pygame.image.load(os.path.join("Assets", "insect.png")).convert_alpha()
slug_sprite     = pygame.image.load(os.path.join("Assets", "slug.png")).convert_alpha()

# Non-creature sprites (items / skills(icons) / etc)


# Effect sprites (lighting / skills(effects) / etc)


# Audio


##############
# Level maps #
##############

#   Level 1: The Coast


#   Level 2: Forest Fringes


#   Level 3: Viridian Deep


#   Level 4: Gloom Woods


#   Level 5: Abyssal Depths

