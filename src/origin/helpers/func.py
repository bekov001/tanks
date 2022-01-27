import pygame
import os
import sys


def load_image(name, colorkey=None):
    """Функция загрузки изображения"""
    fullname = os.path.join("origin","media", 'img', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        raise FileNotFoundError
    image = pygame.image.load(fullname)
    return image


def load_music(name):
    """Функция загрузки музыки"""
    fullname = os.path.join("origin", "media", 'music', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        raise FileNotFoundError
    music = pygame.mixer.music.load(fullname)
    return music
