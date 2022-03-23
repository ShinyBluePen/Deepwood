
from settings import pygame

from settings import TILESIZE


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos = (0, 0), groups = [], sprite_type = "", sprite = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = sprite
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10, -10)

        if sprite_type == "tree":
            # Do an offset
            self.rect = self.image.get_rect(topleft= (pos[0], pos[1] - TILESIZE))
            self.hitbox = self.rect.inflate(-10, -TILESIZE-10)

# class Rock(Tile):
#     def __init__(self, pos = (0, 0), groups = []):
#         super().__init__(groups)
#         self.image = rock_sprite
#
#         Tile(pos, groups, self.image)

# class tree(Tile):
#     def __init__(self, pos, groups, sprite):
#         super().__init__(groups)
#         for row_index, row in enumerate(WORLD_MAP):
#             for col_index, col in enumerate(row):
#                 x = col_index * TILESIZE
#                 y = row_index * TILESIZE
#                 if col == "t":
#                     Tile((x, y), [self.visible_sprites, self.obstacle_sprites], tree_sprite)