
# Deepwood v0.1
# Michael D. Petty
# 26 FEB 2022

import pygame
import pygame_gui

import os
import time
import random

import settings
import creatures
import skills
import items
import light
import world

pygame.init()


def redraw_window():
    settings.WINDOW.blit()
    pygame.display.update()

manager = pygame_gui.UIManager((settings.WIDTH, settings.HEIGHT))

def main():
    pygame.display.set_caption("Deepwood")
    redraw_window()

    game_over = False
    player = creatures.Player(200, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        settings.CLOCK.tick(settings.FPS)
        pygame.display.update()

        if game_over == True:
            main_menu()

        keys = pygame.key.get_pressed()
        creatures.player_movement(keys, player)


def main_menu():
    start_game = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        if start_game == True:
            main()

main_menu()
