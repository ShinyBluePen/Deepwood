

from settings import pygame, jn

from support import import_csv_layout, import_folder, reflect


###################
# Sprite settings #
###################

GRAPHICS = {
    "sprites": import_folder(jn("assets", jn("graphics", "sprites"))),
    "grass":   import_folder(jn("assets", jn("graphics", "grass"))),  # random grass
    "object":  import_folder(jn("assets", jn("graphics", "objects"))),  # mapped by tiled csv
    "weapons": {
        "sword":  import_folder(jn("assets", jn("graphics", jn("weapons", "sword")))),
        "lance":  import_folder(jn("assets", jn("graphics", jn("weapons", "lance")))),
        "axe":    import_folder(jn("assets", jn("graphics", jn("weapons", "axe")))),
        "rapier": import_folder(jn("assets", jn("graphics", jn("weapons", "rapier")))),
        "sai":    import_folder(jn("assets", jn("graphics", jn("weapons", "sai")))),
        },
    "monsters": {
        "bamboo":  import_folder(jn("assets", jn("graphics", jn("monsters", jn("bamboo", "idle"))))),  # GRAPHICS["monsters"]["bamboo"][0]
        "raccoon": import_folder(jn("assets", jn("graphics", jn("monsters", jn("raccoon", "idle"))))),
        "spirit":  import_folder(jn("assets", jn("graphics", jn("monsters", jn("spirit", "idle"))))),
        "squid":   import_folder(jn("assets", jn("graphics", jn("monsters", jn("squid", "idle"))))),
        },
    "magic": {
        "flame": pygame.image.load(jn("assets", jn("graphics", jn("particles", jn("flame", "fire.png"))))),
        "heal":  pygame.image.load(jn("assets", jn("graphics", jn("particles", jn("heal", "heal.png"))))),
        },
    "particles":{
        "magic": {
            "aura":  import_folder(jn("assets", jn("graphics", jn("particles", jn("aura", "frames"))))),
            "flame": import_folder(jn("assets", jn("graphics", jn("particles", jn("flame", "frames"))))),
            "heal":  import_folder(jn("assets", jn("graphics", jn("particles", jn("heal", "frames"))))),
            },
        "leafs": (
            import_folder(jn("assets", jn("graphics", jn("particles", "leaf1")))),
            import_folder(jn("assets", jn("graphics", jn("particles", "leaf2")))),
            import_folder(jn("assets", jn("graphics", jn("particles", "leaf3")))),
            import_folder(jn("assets", jn("graphics", jn("particles", "leaf4")))),
            import_folder(jn("assets", jn("graphics", jn("particles", "leaf5")))),
            import_folder(jn("assets", jn("graphics", jn("particles", "leaf6")))),
            reflect(import_folder(jn("assets", jn("graphics", jn("particles", "leaf1"))))),
            reflect(import_folder(jn("assets", jn("graphics", jn("particles", "leaf2"))))),
            reflect(import_folder(jn("assets", jn("graphics", jn("particles", "leaf3"))))),
            reflect(import_folder(jn("assets", jn("graphics", jn("particles", "leaf4"))))),
            reflect(import_folder(jn("assets", jn("graphics", jn("particles", "leaf5"))))),
            reflect(import_folder(jn("assets", jn("graphics", jn("particles", "leaf6"))))),
            ),
        "attacks": {
            'claw':        import_folder(jn("assets", jn("graphics", jn("particles", "claw")))),
            'slash':       import_folder(jn("assets", jn("graphics", jn("particles", "slash")))),
            'sparkle':     import_folder(jn("assets", jn("graphics", jn("particles", "sparkle")))),
            'leaf_attack': import_folder(jn("assets", jn("graphics", jn("particles", "leaf_attack")))),
            'thunder':     import_folder(jn("assets", jn("graphics", jn("particles", "thunder")))),
            },
        "deaths": {
            'squid':   import_folder(jn("assets", jn("graphics", jn("particles", "smoke_orange")))),
            'raccoon': import_folder(jn("assets", jn("graphics", jn("particles", "raccoon")))),
            'spirit':  import_folder(jn("assets", jn("graphics", jn("particles", "nova")))),
            'bamboo':  import_folder(jn("assets", jn("graphics", jn("particles", "bamboo")))),
            },
        }
    }

# print(GRAPHICS["particles"]["leafs"].values())

# Empty sprite
blank_sprite = GRAPHICS["sprites"][10]

# World sprites (trees / rocks / etc)
rock_sprite = GRAPHICS["sprites"][14]
tree_sprite = GRAPHICS["sprites"][17]

# Character sprites
player_sprite = GRAPHICS["sprites"][13]

# Race sprites
bird_race_sprite   = GRAPHICS["sprites"][3]
fox_race_sprite    = GRAPHICS["sprites"][4]
frog_race_sprite   = GRAPHICS["sprites"][5]
human_race_sprite  = GRAPHICS["sprites"][6]
slug_race_sprite   = GRAPHICS["sprites"][7]
spider_race_sprite = GRAPHICS["sprites"][8]

# Creature sprites
bear_sprite   = GRAPHICS["sprites"][0]
bird_sprite   = GRAPHICS["sprites"][1]
fox_sprite    = GRAPHICS["sprites"][2]
deer_sprite   = GRAPHICS["sprites"][9]
frog_sprite   = GRAPHICS["sprites"][11]
insect_sprite = GRAPHICS["sprites"][12]
slug_sprite   = GRAPHICS["sprites"][15]


##################
# World settings #
##################

world_floor = pygame.image.load(jn("assets", jn("graphics", jn("tilemap", "ground.png")))).convert()

LAYOUTS = {
    "boundary": import_csv_layout(jn("assets", jn("world", "map_FloorBlocks.csv"))),
    "grass":    import_csv_layout(jn("assets", jn("world", "map_Grass.csv"))),
    "object":   import_csv_layout(jn("assets", jn("world", "map_Objects.csv"))),
    "creature": import_csv_layout(jn("assets", jn("world", "map_Entities.csv"))),
    }


#################
# Data settings #
#################

# enemy
monster_data = {
    'squid': {
        'health': 100,
        'exp': 100,
        'damage': 10,
        'attack_type': 'slash',
        'attack_sound': jn("assets", jn("audio", jn("attack", "slash.wav"))),
        'speed': 3,
        'resistance': 1.5,
        'attack_radius': 80,
        'notice_radius': 300
        },
    'raccoon': {
        'health': 300,
        'exp': 250,
        'damage': 40,
        'attack_type': 'claw',
        'attack_sound': jn("assets", jn("audio", jn("attack", "claw.wav"))),
        'speed': 2,
        'resistance': 1.5,
        'attack_radius': 120,
        'notice_radius': 300
        },
    'spirit': {
        'health': 100,
        'exp': 110,
        'damage': 8,
        'attack_type': 'thunder',
        'attack_sound': jn("assets", jn("audio", jn("attack", "fireball.wav"))),
        'speed': 4,
        'resistance': 1.5,
        'attack_radius': 60,
        'notice_radius': 300
        },
    'bamboo': {
        'health': 70,
        'exp': 120,
        'damage': 6,
        'attack_type': 'leaf_attack',
        'attack_sound': jn("assets", jn("audio", jn("attack", "slash.wav"))),
        'speed': 2,
        'resistance': 1.5,
        'attack_radius': 50,
        'notice_radius': 150
        }
    }

# weapons
weapon_data = {
    'sword': {
        'cooldown': 400,
        'damage': 15,
        'graphic': GRAPHICS["weapons"]["sword"][1]
        },
    'lance': {
        'cooldown': 800,
        'damage': 30,
        'graphic': GRAPHICS["weapons"]["lance"][1]
        },
    'axe': {
        'cooldown': 600,
        'damage': 20,
        'graphic': GRAPHICS["weapons"]["axe"][1]
        },
    'rapier': {
        'cooldown': 200,
        'damage': 10,
        'graphic': GRAPHICS["weapons"]["rapier"][1]
        },
    'sai': {
        'cooldown': 0,
        'damage': 5,
        'graphic': GRAPHICS["weapons"]["sai"][1]
        }
    }

# magic
magic_data = {
    'flame': {
        'strength': 5,
        'cost': 20,
        'graphic': GRAPHICS["magic"]["flame"]
        },
    'heal': {
        'strength': 10,
        'cost': 10,
        'graphic': GRAPHICS["magic"]["heal"]
        }
    }

# player
player_data = {
    "hp": 30,
    "mp": 15,
    "atk": 10,
    "mgk": 10,
    "speed": 3
    }

# todo

#   Level 1: The Coast


#   Level 2: Forest Fringes


#   Level 3: Viridian Deep


#   Level 4: Gloom Woods


#   Level 5: Abyssal Depths



# Audio
#######

# Effect sprites (lighting / skills(effects) / etc)
# Non-creature sprites (items / skills(icons) / etc)
