

from settings import pygame, random, math, jn, TILESIZE

from data import GRAPHICS, monster_data, weapon_data, magic_data, player_data

from support import import_folder


class Creature(pygame.sprite.Sprite):
    def __init__(self, pos, groups, image):
        super().__init__(groups)
        self.image  = image
        self.rect   = self.image.get_rect(topleft = pos).inflate(-10, -10)
        self.hitbox = self.rect.inflate(-20, -40)
        # self.hitbox_outline = pygame.Rect(self.hitbox)

        self.image_outline = pygame.Rect(self.image.get_rect())
        self.rect_outline = pygame.Rect(self.image.get_rect().inflate(-10, -10))
        self.hitbox_outline = pygame.Rect(self.image.get_rect().inflate(-20, -40))

        # movement / graphics
        self.frame_index = 0
        self.animation_speed = 0.05
        self.direction = pygame.math.Vector2()
        self.location  = None
        # self.mask = pygame.mask.from_surface(self.image)

        # i-frames
        self.vulnerable = True
        self.hit_last = None
        self.invulnerable_time = 300

        # Resource attributes
        self.stats = []
        self.vitality  = 1   # health
        self.spirit    = 1   # magical energy
        self.potential = 500   # unspent skill
        self.influence = {}  # natural forces influencing creature.  Dictionary is {influence: weight}

        # Stat attributes
        self.luck         = 1   #   Influences include: (white  ) (Fate     )  MTG 4c factions:  MTG faction characteristics:
        self.speed        = 1   #       POWER           (yellow ) (Momentum )   Altruism          w  morality    /order      /peace      /rigid
        self.dexterity    = 1   #       SIN             (green  ) (Freedom  )   Growth            u  logic       /technology /knowledge
        self.strength     = 1   #       ORDER           (grey   ) (Power    )   Artifice          b  selfishness /pain       /sacrifice
        self.constitution = 1   #       GROWTH          (red    ) (Hunger   )   Chaos             r  impulse     /chaos      /freedom
        self.intelligence = 1   #       SPIRIT          (blue   ) (Logic    )   Aggression        g  instinct    /growth     /change
        self.charisma     = 1   #                       (purple ) (Emotion  )   Domain(5c)

        # Characteristic attributes
        self.inventory   = {}  # Dictionary.  Dictionary is {item: amount}
        self.race        = ""
        self.animal      = ""
        self.mutation    = ""
        self.size        = 1
        self.savagery    = 1
        self.sex         = random.choice(["male", "female"])
        self.description = ""

    def get_location(self):
        self.location = None

    def get_description(self):
        print(self.description)

    def draw(self):
        # pygame.Surface.blit(WINDOW, self.image, (self.x, self.y))
        pygame.display.update()

    def movement(self):
        # if self.direction.magnitude() != 0:
        #     self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * self.stats["speed"]
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * self.stats["speed"]
        self.collision("vertical")
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # moving up
                        self.hitbox.top = sprite.hitbox.bottom

        # creature_rect = self.rect.move(speed)

        # Prevent creature from moving out of bounds.
        # if creature_rect.rect.left < 0 or creature_rect.rect.right > WIDTH:
        #     speed[0] = -speed[0]
        # if creature_rect.rect.top < 0 or creature_rect.rect.bottom > HEIGHT:
        #     speed[1] = -speed[1]

    def wave_value(self):
        wave = math.sin(pygame.time.get_ticks()/10)
        if wave >= 0:
            return 255
        else:
            return 0


class Player(Creature):
    def __init__(self,
                 pos,
                 groups,
                 obstacle_sprites,
                 image,
                 attack_create,
                 attack_destroy,
                 magic_create,
                 ):
        super().__init__(pos, groups, image)
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

        self.max_stats = {
            "hp": 300,
            "mp": 150,
            "atk": 100,
            "mgk": 100,
            "speed": 7
            }
        self.upgrade_cost = {
            "hp": 100,
            "mp": 100,
            "atk": 100,
            "mgk": 100,
            "speed": 100
            }

        # damage

        # sound
        self.weapon_attack_sound = pygame.mixer.Sound(jn("assets", jn("audio", "sword.wav")))
        self.weapon_attack_sound.set_volume(0.2)

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
            self.weapon_attack_sound.play()

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
            self.speed = self.stats["speed"]
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
        # if self.vitality <= 0:
        #     self.kill()

        pygame.draw.rect(self.image, "red", self.image_outline, 1)
        pygame.draw.rect(self.image, "green", self.rect_outline, 1)
        pygame.draw.rect(self.image, "blue", self.hitbox_outline, 1)

    def get_full_weapon_damage(self):
        base = self.stats["atk"]
        weapon = weapon_data[self.weapon]["damage"]
        return base + weapon

    def get_full_magic_damage(self):
        base = self.stats["mgk"]
        spell = magic_data[self.magic]["strength"]
        return base + spell

    def get_value_by_index(self, index):
        return list(self.stats.values())[index]

    def get_cost_by_index(self, index):
        return list(self.upgrade_cost.values())[index]

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


class Enemy(Creature):
    def __init__(self,
                 monster,
                 pos,
                 groups,
                 obstacle_sprites,
                 damage_player,
                 death_particles,
                 add_potential
                 ):
        super().__init__(pos, groups, image= GRAPHICS["monsters"][monster][0])
        self.sprite_type = "enemy"

        # graphics
        self.import_monster_assets(monster)
        self.status = "idle"
        self.image = self.animations[self.status][self.frame_index]

        # movement
        self.obstacle_sprites = obstacle_sprites

        # stats
        self.monster = monster
        self.stats = monster_data[self.monster]
        self.vitality       = self.stats["health"]
        self.potential      = self.stats["exp"]
        self.speed          = self.stats["speed"]
        self.strength       = self.stats["damage"]
        self.resistance     = self.stats["resistance"]
        self.attack_radius  = self.stats["attack_radius"]
        self.notice_radius  = self.stats["notice_radius"]
        self.attack_type    = self.stats["attack_type"]

        # player interaction
        self.can_attack = True
        self.attack_last = None
        self.attack_cooldown = 1000
        self.damage_player = damage_player
        self.death_particles = death_particles
        self.add_potential = add_potential

        # offsets
        if monster == "raccoon":
            self.rect = self.image.get_rect(center= (pos[0]+32, pos[1])) # ((pos[0] - TILESIZE - 16), (pos[1] - 2*TILESIZE)))
            self.hitbox = self.rect.inflate((-20 - TILESIZE), (-40 - 2*TILESIZE))
            self.hitbox_outline = pygame.Rect(self.image.get_rect().inflate((-20 - TILESIZE), (-40 - 2*TILESIZE)))

        # sounds
        self.death_sound = pygame.mixer.Sound(jn("assets", jn("audio", "death.wav")))
        self.death_sound.set_volume(0.1)
        self.hit_sound = pygame.mixer.Sound(jn("assets", jn("audio", "hit.wav")))
        self.hit_sound.set_volume(0.1)
        self.attack_sound = pygame.mixer.Sound(self.stats["attack_sound"])
        self.attack_sound.set_volume(0.1)


    def import_monster_assets(self, monster):
        character_path = jn("assets", jn("graphics", jn("monsters", monster)))

        self.animations = {
            "attack": [],
            "idle": [],
            "move": [],
            }

        for animation in self.animations.keys():
            full_path = jn(character_path, animation)
            self.animations[animation] = import_folder(full_path)

    def get_player_distance_direction(self, player):
        enemy_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(player.rect.center)
        distance = (player_vector - enemy_vector).magnitude()
        if distance > 0:
            direction = (player_vector - enemy_vector).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != "attack":
                self.frame_index = 0
            self.status = "attack"
        elif distance <= self.notice_radius:
            self.status = "move"
        else:
            self.status = "idle"

    def actions(self, player):
        if self.status == "attack":
            self.attack_sound.play()
            self.attack_last = pygame.time.get_ticks()
            self.damage_player(self.strength, "attacks", self.attack_type)
            self.can_attack = False
        elif self.status == "move":
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def animate(self):
        animation = self.animations[self.status]
        self.animation_speed = 0.1

        # draw animation frames
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            # attack cooldown
            if self.status == "attack":
                self.can_attack = False
            self.frame_index = 0

            # random idle
            if self.status == "idle":
                self.image = random.choice(animation)

        # set each image frame
        if self.status != "idle":
            self.image = animation[int(self.frame_index)]

        self.rect = self.image.get_rect(center = self.hitbox.center)

        # debugging image and rect dimensions
        # pygame.draw.rect(self.image, "red", pygame.Rect(self.image.get_rect()), 1)
        # pygame.draw.rect(self.image, "blue", pygame.Rect((self.hitbox.topleft), (self.hitbox.size)), 1)
        pygame.draw.rect(self.image, "red", self.image_outline, 1)
        pygame.draw.rect(self.image, "green", self.rect_outline, 1)
        pygame.draw.rect(self.image, "blue", self.hitbox_outline, 1)

        #flicker
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if not self.can_attack:
            if current_time - self.attack_last >= self.attack_cooldown:
                self.can_attack = True

        if not self.vulnerable:
            if current_time - self.hit_last >= self.invulnerable_time:
                self.vulnerable = True

    def get_damage(self, player, attack_type):
        if self.vulnerable:
            self.hit_sound.play()
            # chase player
            self.direction = self.get_player_distance_direction(player)[1]

            if attack_type == "weapon":
                self.vitality -= player.get_full_weapon_damage()
            else:
                attack_type == "magic"
                self.vitality -= player.get_full_magic_damage()

            # i-frame timer
            self.hit_last = pygame.time.get_ticks()
            self.vulnerable = False

    def check_death(self):
        if self.vitality <=0:
            self.death_particles(self.rect.center, "deaths", self.monster)
            self.add_potential(self.potential)
            self.death_sound.play()
            self.kill()

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistance

    def update(self):
        self.hit_reaction()
        self.movement()
        self.animate()
        self.cooldowns()
        self.check_death()

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)