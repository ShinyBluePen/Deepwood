

import pygame

import random, math, time, sys

from os.path import join as jn


# Game settings
WIDTH = 1600
HEIGHT = 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
ICON = pygame.display.set_icon(
    pygame.image.load(jn("assets", jn("graphics", jn("sprites", "17.png"))))
)
FPS = 60
CLOCK = pygame.time.Clock()
TIME = pygame.time.get_ticks()
TILESIZE = 64

HITBOX_OFFSET = {
    "player": (0, -26),
    "object": (0, -40),
    "grass": (0, -10),
    "invisible": (0, 0),
}

SPLASH_LIST = random.choice([
    "It's deep!",
    "Hello World!",
    "I'm lumber, Jack!",
    "Are you ready?"
    ]
)

MAIN_MENU_SPLASH = pygame.display.set_caption(f"Deepwood - {SPLASH_LIST}")

LOCATION_LIST = [
    "The Coast",
    "Forest Fringes",
    "Viridian Deep",
    "Gloom Woods",
    "Abyssal Depths",
]

# Colour settings
TEXT_COLOR = "#EEEEEE"
UI_BG_COLOR = "#222222"
UI_BORDER_COLOR = "#111111"
WATER_COLOR = "#71ddee"
HEALTH_COLOR = (255, 50, 50)  # red
ENERGY_COLOR = "aqua"
UI_BORDER_COLOR_ACTIVE = "gold"

# UI settings
BAR_HEIGHT = 35
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = jn("assets", jn("graphics", jn("font", "joystix.ttf")))
UI_FONT_SIZE = 36

# Menu settings
#   todo: main menu

#   todo: character menu (gear/etc)

#   todo: stats menu (stats/info/etc)

#   todo: inventory menu

#   todo: upgrade menu
TEXT_COLOR_SELECTED = "#111111"
BAR_COLOR = "#EEEEEE"
BAR_COLOR_SELECTED = "#111111"
UPGRADE_BG_COLOR_SELECTED = "#EEEEEE"
