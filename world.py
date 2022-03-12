
import pygame

from settings import *
from tile import Tile
from creature import Creature
from player import Player

from debug import debug


class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        # Sprite group setup
        self.visible_sprites = Y_Sort_Camera_Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # Sprite setup
        self.create_world()

    def create_world(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE

                if col == "x":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], rock_sprite)
                if col == "t":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], tree_sprite)
                if col == "p":
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites, player_sprite)


    #     self.generate_terrain()
    #     # self.spawn_enemies()
    #     # self.spawn_friendly_creatures()
    #     # self.spawn_items()
    #     self.spawn_player()
    #
    # def generate_terrain(self):
    #     for row_index, row in enumerate(WORLD_MAP):
    #         for col_index, col in enumerate(row):
    #             x = col_index * TILESIZE
    #             y = row_index * TILESIZE
    #
    #             if col == "x":
    #                 tile.rock()
    #                 Tile((x, y), [self.visible_sprites, self.obstacle_sprites], rock_sprite)
    #             if col == "t":
    #                 # tile.tree()
    #                 Tile((x, y), [self.visible_sprites, self.obstacle_sprites], tree_sprite)
    #
    # #todo
    # def spawn_enemies(self):
    #     for row_index, row in enumerate(WORLD_MAP):
    #         for col_index, col in enumerate(row):
    #             x = col_index * TILESIZE
    #             y = row_index * TILESIZE
    #
    # #todo
    # def spawn_friendly_creatures(self):
    #     for row_index, row in enumerate(WORLD_MAP):
    #         for col_index, col in enumerate(row):
    #             x = col_index * TILESIZE
    #             y = row_index * TILESIZE
    #
    # #todo
    # def spawn_items(self):
    #     for row_index, row in enumerate(WORLD_MAP):
    #         for col_index, col in enumerate(row):
    #             x = col_index * TILESIZE
    #             y = row_index * TILESIZE
    #
    # def spawn_player(self):
    #     for row_index, row in enumerate(WORLD_MAP):
    #         for col_index, col in enumerate(row):
    #             x = col_index * TILESIZE
    #             y = row_index * TILESIZE
    #
    #             if col == "p":
    #                 self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites, player_sprite)

    def draw(self):
        self.player.update()
        self.visible_sprites.camera(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)

class Y_Sort_Camera_Group(pygame.sprite.Sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def camera(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos