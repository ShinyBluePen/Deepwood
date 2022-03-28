

from settings import pygame

from settings import TILESIZE, HITBOX_OFFSET


class Tile(pygame.sprite.Sprite):
    def __init__(
        self,
        pos=(0, 0),
        groups=[],
        sprite_type="",
        sprite=pygame.Surface((TILESIZE, TILESIZE)),
    ):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = sprite
        self.rect = self.image.get_rect(topleft=pos).inflate(-10, -10)
        self.hitbox = self.rect.inflate(-10, -10)

        self.image_outline = pygame.Rect(self.image.get_rect())
        self.rect_outline = pygame.Rect(self.image.get_rect().inflate(-10, -10))
        self.hitbox_outline = pygame.Rect(self.image.get_rect().inflate(-10, -74))

        offset = HITBOX_OFFSET[sprite_type]

        pygame.draw.rect(self.image, "red", self.image_outline, 1)
        pygame.draw.rect(self.image, "green", self.rect_outline, 1)
        pygame.draw.rect(self.image, "blue", self.hitbox_outline, 1)

        if sprite_type == "object":
            # Do an offset
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))
            self.hitbox = self.rect.inflate(-10, -TILESIZE - 10)


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
