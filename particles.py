

from settings import pygame, random

from data import GRAPHICS

class AnimationPlayer:
    def __init__(self):
        self.frames = GRAPHICS["particles"]

    def create_grass_particles(self, pos, groups):
        frames = random.choice(self.frames["leafs"])
        Particle(pos, frames, groups)

    def create_particles(self, pos, style, frames, groups):
        frames = self.frames[style][frames]
        Particle(pos, frames, groups)

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(groups)
        self.sprite_type = "magic"
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = frames
        for frame in frames:
            self.image = frame # .get_rect(center = self.frame_index)
            self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()