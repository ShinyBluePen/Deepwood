

from settings import *
from data import weapon_data
from data import magic_data


class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # bar
        self.hp_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.mp_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        # convert weapon dictionary and show equipped weapon in weapon box
        self.weapon_graphics = []
        for weapon in weapon_data.values():
            weapon_surface = weapon["graphic"]
            self.weapon_graphics.append(weapon_surface)

        # convert magic dictionary and show equipped magic in magic box
        self.magic_graphics = []
        for magic in magic_data.values():
            magic_surface = magic["graphic"]
            self.magic_graphics.append(magic_surface)

    def show_bar(self, current, maximum, bg_rect, colour):
        # draw bg
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # convert stat to pixel
        ratio = current / maximum
        width = bg_rect.width * ratio
        rect = bg_rect.copy()
        rect.width = width

        # draw bar
        pygame.draw.rect(self.display_surface, colour, rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 2)

    def show_potential(self, potential):
        text_surface = self.font.render(str(int(potential)), False, TEXT_COLOR)
        x = WIDTH - 14  # self.display_surface.get_size()[0]
        y = HEIGHT - 10  # self.display_surface.get_size()[1]
        text_rect = text_surface.get_rect(bottomright=(x, y))

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(10, 0))
        self.display_surface.blit(text_surface, text_rect)
        pygame.draw.rect(
            self.display_surface, UI_BORDER_COLOR, text_rect.inflate(10, 0), 2
        )

    def selection_box(self, left, top, switched):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        if switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 2)
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 2)

        return bg_rect

    def weapon_overlay(self, weapon_index, switched):
        bg_rect = self.selection_box(70, 810, switched)
        weapon_surface = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surface.get_rect(center=bg_rect.center)

        self.display_surface.blit(weapon_surface, weapon_rect)

    def magic_overlay(self, magic_index, switched):
        bg_rect = self.selection_box(10, 790, switched)
        magic_surface = self.magic_graphics[magic_index]
        magic_rect = magic_surface.get_rect(center=bg_rect.center)

        self.display_surface.blit(magic_surface, magic_rect)

    def display(self, player):
        self.show_bar(
            player.vitality, player.stats["hp"], self.hp_bar_rect, HEALTH_COLOR
        )
        self.show_bar(player.spirit, player.stats["mp"], self.mp_bar_rect, ENERGY_COLOR)
        self.show_potential(player.potential)
        self.magic_overlay(player.magic_index, player.magic_switching)
        self.weapon_overlay(player.weapon_index, player.weapon_switching)
