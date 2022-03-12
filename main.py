
# Deepwood v0.1
# Michael D. Petty
# 26 FEB 2022

import pygame

import random
import time
import sys
import os

from settings import *
from world import World
from creature import Creature

class Game:
    def __init__(self):
        pygame.init()
        self.screen     = WINDOW
        self.icon       = ICON
        self.caption    = MAIN_MENU_SPLASH
        self.clock      = CLOCK
        self.start_game = True
        self.game_over  = False
        self.world      = World()

    def draw(self):
        # Window
        fps          = round(self.clock.get_fps(), 2)
        location     = LOCATION_LIST[0]
        self.caption = pygame.display.set_caption(f"Deepwood - {location} - [{fps}]")

        # Graphics
        self.screen.fill("black")
        self.world.draw()
        pygame.display.update()

    def main_menu(self):
        while True:
            self.draw()
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.start_game:
                self.run()

    def run(self):
        while True:
            self.draw()
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_m:
                #         self.world.toggle_menu()

            if self.game_over:
                self.game_over = False
                self.main_menu()

def main():
    Deepwood = Game()
    Deepwood.main_menu()

if __name__ == "__main__":
    main()