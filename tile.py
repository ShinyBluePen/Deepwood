
import pygame

from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite):
        super().__init__(groups)
        self.image = sprite
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10, -10)

        self.boundary = bool

# class Rock(Tile):
#     def __init__(self, pos, groups, sprite):
#         super().__init__(pos, groups, sprite)
#         pos    = self.rect
#         groups = [self.visible_sprites, self.obstacle_sprites]
#         sprite = rock_sprite
#
#         Tile(pos, groups, sprite)

# class tree(Tile):
#     def __init__(self, pos, groups, sprite):
#         super().__init__(groups)
#         for row_index, row in enumerate(WORLD_MAP):
#             for col_index, col in enumerate(row):
#                 x = col_index * TILESIZE
#                 y = row_index * TILESIZE
#                 if col == "t":
#                     Tile((x, y), [self.visible_sprites, self.obstacle_sprites], tree_sprite)