
from settings import pygame, jn

from os import walk

from csv import reader


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def reflect(frames):
    reflected_frames = []

    for frame in frames:
        reflection = pygame.transform.flip(frame, True, False)
        reflected_frames.append(reflection)

    return reflected_frames

def import_folder(path):
    surface_list = []

    for _, __, image_files in walk(path):
        for image in image_files:
            full_path = jn(path, image)
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)

    return surface_list
