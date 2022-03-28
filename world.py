

from settings import pygame, random, TILESIZE

from data import player_sprite, world_floor, LAYOUTS, GRAPHICS

from ui import UI

from tile import Tile

from item import Weapon

from creature import Enemy, Player

from particles import AnimationPlayer

from magic import Magic

from upgrade import Upgrade


class World:
    """
    Create and update the world and all objects within.  Manage interactions that happen within the world environment.

        Returns:
            World object \n

        Functions:
            create_world, \n
            attack_create, \n
            player_attack_logic, \n
            attack_destroy, \n
            magic_create(style, strength, cost), \n
            damage_player(amount, style, attack_type), \n
            death_particles(pos, particle_type, frames), \n
            draw

        Attributes:
            display_surface, \n
            visible_sprites, \n
            obstacle_sprites, \n
            attack_current, \n
            attack_sprites, \n
            attackable_sprites, \n
            create_world, \n
            ui, \n
            animation_player, \n
            magic_player
    """
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False

        # Sprite group setup
        self.visible_sprites = Y_Sort_Camera_Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # attack sprites
        self.attack_current = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # Sprite setup
        self.create_world()

        # ui
        self.ui = UI()
        self.upgrade = Upgrade(self.player)

        # particles
        self.animation_player = AnimationPlayer()
        self.magic_player = Magic(self.animation_player)

        # cooldowns
        self.collide_last = None
        self.collide_cooldown = 400

    def create_world(self):
        for style, layout in LAYOUTS.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE

                        if style == "boundary":
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], "invisible", GRAPHICS["sprites"][10])

                        if style == "grass":
                            random_grass = random.choice(GRAPHICS[style])
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites], "grass", random_grass)

                        if style == "object":
                            surface = GRAPHICS["object"][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites], "object", surface)

                        if style == "creature":
                            if col == "394":
                                self.player = Player(
                                    (x, y),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    player_sprite,
                                    self.attack_create,
                                    self.attack_destroy,
                                    self.magic_create,
                                    )
                            else:
                                if col == "390":
                                    monster = "bamboo"  # Enemy(monster, (x, y), [self.visible_sprites], self.obstacle_sprites)
                                elif col == "391":
                                    monster = "spirit"  # Enemy("spirit", (x, y), [self.visible_sprites], self.obstacle_sprites)
                                elif col == "392":
                                    monster = "raccoon"  # Enemy("raccoon", (x, y), [self.visible_sprites], self.obstacle_sprites)
                                elif col == "393":
                                    monster = "squid"  # Enemy("squid", (x, y), [self.visible_sprites], self.obstacle_sprites)

                                Enemy(
                                    monster,
                                    (x, y),
                                    [self.visible_sprites, self.attackable_sprites],
                                    self.obstacle_sprites,
                                    self.damage_player,
                                    self.death_particles,
                                    self.add_potential,
                                    )

    def attack_create(self):
        self.attack_current = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)

                if collision_sprites:
                    for target_sprite in collision_sprites:
                        pos = target_sprite.rect.center

                        if target_sprite.sprite_type == "grass":
                            for leaf in range(random.randint(3, 6)):
                                offset = pygame.math.Vector2(0, 64)
                                self.animation_player.create_grass_particles(pos - offset, [self.visible_sprites])
                            target_sprite.kill()

                        elif target_sprite.sprite_type == "object":
                            for leaf in range(random.randint(0, 0)):
                                offset = pygame.math.Vector2(random.randint(-64, 64), random.randint(-10, 54))
                                self.animation_player.create_grass_particles(pos - offset, [self.visible_sprites])

                        else:
                            target_sprite.get_damage(self.player, attack_sprite.sprite_type)

    def attack_destroy(self):
        if self.attack_current:
            self.attack_current.kill()
        self.attack_current = None

    def magic_create(self, style, strength, cost):
        cost = cost - self.player.stats["mgk"]//5

        if style == "heal":
            self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])

        if style == "flame":
            self.magic_player.flame(self.player, cost, [self.visible_sprites, self.attack_sprites])

    def damage_player(self, amount, style, attack_type):
        if self.player.vulnerable:
            self.player.vitality -= amount
            self.player.vulnerable = False
            self.player.hit_last = pygame.time.get_ticks()
            if self.player.vitality <= 0:
                pass
            # spawn particles
            self.animation_player.create_particles(self.player.rect.center, style, attack_type, [self.visible_sprites])

    def death_particles(self, pos, particle_type, frames):
        self.animation_player.create_particles(pos, particle_type, frames, [self.visible_sprites])

    def add_potential(self, amount):
        self.player.potential += amount

    def toggle_menu(self):
        # flip bool value
        self.game_paused = not self.game_paused

    def draw(self):
        self.visible_sprites.camera(self.player)
        self.ui.display(self.player)

        if self.game_paused:
            self.upgrade.display()
        else:
            # Debug().debug(self.player.magic_create.style)
            self.player.update()
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
            self.player_attack_logic()

class Y_Sort_Camera_Group(pygame.sprite.Group):
    """
    Sort objects by their Y position and draw lower Y objects over higher Y value objects.

        Returns:
            None

        Functions:
            camera(player) \n
            enemy_update(player) \n

        Attributes:
            display_surface \n
            half_width \n
            half_height \n
            offset \n
            floor_surface \n
            floor_rect \n
    """
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # Create floor
        self.floor_surface = world_floor
        self.floor_rect = self.floor_surface.get_rect(topleft = (0, 0))

    def camera(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Draw the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        # Draw objects by their center y position
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "enemy"]
        for enemy in enemy_sprites:
            enemy.enemy_update(player)

# todo: old code
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
    #
    # def spawn_enemies(self):
    #     for row_index, row in enumerate(WORLD_MAP):
    #         for col_index, col in enumerate(row):
    #             x = col_index * TILESIZE
    #             y = row_index * TILESIZE
    #
    #
    # def spawn_friendly_creatures(self):
    #     for row_index, row in enumerate(WORLD_MAP):
    #         for col_index, col in enumerate(row):
    #             x = col_index * TILESIZE
    #             y = row_index * TILESIZE
    #
    #
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