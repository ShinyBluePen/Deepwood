
from settings import pygame
from settings import jn

from settings import PLAYER_VELOCITY
from data import weapon_data
from data import magic_data
from data import player_data

from support import import_folder

from creature import Creature


class Player(Creature):
    def __init__(self,
                 pos,
                 groups,
                 obstacle_sprites,
                 sprite,
                 attack_create,
                 attack_destroy,
                 magic_create,
                 ):
        super().__init__(pos, groups, sprite)
        self.obstacle_sprites = obstacle_sprites

        # graphics
        self.import_player_assets()
        self.status = "down"

        # movement
        self.attack_speed = 1
        self.attack_create = attack_create
        self.attack_destroy = attack_destroy

        # weapon
        self.attacking = False
        self.attack_cooldown = 100
        self.attack_last = None

        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.weapon_switching = False
        self.weapon_switch_cooldown = 200
        self.weapon_last_switch = None

        # magic
        self.casting = False
        self.cast_cooldown = 1000 # - int(self.stats["mgk"]) * 10
        self.cast_last = None

        self.magic_create = magic_create
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.magic_switching = False
        self.magic_switch_cooldown = 200
        self.magic_last_switch = None

        # stats
        self.stats = player_data
        self.vitality = self.stats["hp"]
        self.spirit = self.stats["mp"]
        self.strength = self.stats["atk"]
        self.intelligence = self.stats["mgk"]
        self.speed = self.stats["speed"]

        # damage

        # sound

    def import_player_assets(self):
        character_path = jn("assets", jn("graphics", "player"))

        self.animations = {
            'up':           [], 'down':        [], 'left':      [], 'right':       [],
            'right_idle':   [], 'left_idle':   [], 'up_idle':   [], 'down_idle':   [],
            'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []
            }

        for animation in self.animations.keys():
            full_path = jn(character_path, animation)
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()

        # move
        if keys[pygame.K_w]:  # up
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_s]:  # down
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0
        # x
        if keys[pygame.K_d]:  # right
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_a]:  # left
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.x = 0

        # attack
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_last = pygame.time.get_ticks()  # run one time
            self.attack_create()

        # magic
        if keys[pygame.K_LSHIFT] and not self.casting:
            self.casting = True
            self.cast_last = pygame.time.get_ticks()  # run one time
            style = list(magic_data.keys())[self.magic_index]
            strength = magic_data[style]["strength"] + self.stats["mgk"]
            cost = magic_data[style]["cost"]
            self.magic_create(style, strength, cost)

        # controls such as [m] for menu, [i] for inventory, etc.
        # weapon switching
        if keys[pygame.K_LALT] and not self.weapon_switching:
            self.weapon_switching = True
            self.weapon_last_switch = pygame.time.get_ticks()  # run one time

            if self.weapon_index < len(list(weapon_data.keys())) - 1:
                self.weapon_index += 1
            else:
                self.weapon_index = 0

            self.weapon = list(weapon_data.keys())[self.weapon_index]

        # magic switching
        if keys[pygame.K_LCTRL] and not self.magic_switching:
            self.magic_switching = True
            self.magic_last_switch = pygame.time.get_ticks()  # run one time

            if self.magic_index < len(list(magic_data.keys())) - 1:
                self.magic_index += 1
            else:
                self.magic_index = 0

            self.magic = list(magic_data.keys())[self.magic_index]

    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if "idle" not in self.status and "attack" not in self.status:
                self.status = self.status + "_idle"

        # attack status
        if self.attacking:
            self.speed = self.attack_speed
            if "attack" not in self.status:
                if "idle" in self.status:
                    self.status = self.status.replace("_idle", "_attack")
                else:
                    self.status = self.status + "_attack"
        else:
            self.speed = PLAYER_VELOCITY
            if "attack" in self.status:
                self.status = self.status.replace("_attack", "")

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_last >= self.attack_cooldown + weapon_data[self.weapon]["cooldown"]:
                self.attacking = False
                self.attack_destroy()

        if self.weapon_switching:
            if current_time - self.weapon_last_switch >= self.weapon_switch_cooldown:
                self.weapon_switching = False

        if self.casting:
            if current_time - self.cast_last >= self.cast_cooldown:
                self.casting = False
                # self.magic_destroy()

        if self.magic_switching:
            if current_time - self.magic_last_switch >= self.magic_switch_cooldown:
                self.magic_switching = False

        if not self.vulnerable:
            if current_time - self.hit_last >= self.invulnerable_time:
                self.vulnerable = True

    def animate(self):
        animation = self.animations[self.status]

        # draw animation frames
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set each image frame
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        # flicker
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

        # kill player if no health remaining
        if self.vitality <= 0:
            self.kill()

    def get_full_weapon_damage(self):
        base = self.stats["atk"]
        weapon = weapon_data[self.weapon]["damage"]
        return base + weapon

    def get_full_magic_damage(self):
        base = self.stats["mgk"]
        spell = magic_data[self.magic]["strength"]
        return base + spell

    def regeneration(self):
        if self.spirit < self.stats["mp"]:
            self.spirit += 0.002 * self.stats["mgk"]
        else:
            self.spirit -= 0.005

        if self.vitality >= self.stats["hp"]:
            self.vitality -= 0.05

    def update(self):
        self.regeneration()
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.movement()

        # if keys[pygame.K_a] and self.x - self.speed > 0:
        #     self.x -= self.speed    # Right
        # if keys[pygame.K_d] and self.x + self.speed + self.sprite.get_width() < WIDTH:
        #     self.x += self.speed    # up
        # if keys[pygame.K_w] and self.y - self.speed > 0:
        #     self.y -= self.speed    # down
        # if keys[pygame.K_s] and self.y + self.speed + self.sprite.get_height() < HEIGHT:
        #     self.y += self.speed
