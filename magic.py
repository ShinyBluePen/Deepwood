
from settings import pygame, jn

from settings import TILESIZE

from random import randint

class Magic:
    def __init__(self, animation_player):
        self.animation_player = animation_player
        self.sounds = {
            "heal": pygame.mixer.Sound(jn("assets", jn("audio", "heal.wav"))),
            "flame": pygame.mixer.Sound(jn("assets", jn("audio", "fire.wav"))),
        }

    def heal(self, player, strength, cost, groups):
        if player.spirit >= cost:
            self.sounds["heal"].play()
            player.vitality += strength
            player.spirit -= cost

            offset = pygame.math.Vector2(0, 60)

            self.animation_player.create_particles(player.rect.center, "magic", "aura", groups)
            self.animation_player.create_particles(player.rect.center - offset, "magic", "heal", groups)

    def flame(self, player, cost, groups):
        if player.spirit >= cost:
            self.sounds["flame"].play().set_volume(0.2)
            player.spirit -= cost

            if player.get_status() == "idle":
                pass

            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)
            else:
                direction = pygame.math.Vector2(0, 1)

            for i in range(1, 6 + int((player.stats["mgk"]//10))):
                    offset_x = (direction.x * i) * TILESIZE
                    offset_y = (direction.y * i) * TILESIZE
                    for flame in range(randint(1, player.stats["mgk"]//10)):
                        # player facing direction
                        if direction.x:
                            x = player.rect.centerx + offset_x + randint(-TILESIZE // 2, TILESIZE // 2)
                            y = player.rect.centery + randint(-TILESIZE // 2, TILESIZE // 2)
                            self.animation_player.create_particles((x,y), 'magic', "flame", groups)
                        else:
                            x = player.rect.centerx + randint(-TILESIZE // 2, TILESIZE // 2)
                            y = player.rect.centery + offset_y + randint(-TILESIZE // 2, TILESIZE // 2)
                            self.animation_player.create_particles((x,y), 'magic', "flame", groups)