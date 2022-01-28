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


def load_sound(name):
    fullname = os.path.join("origin", "media", 'music', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        raise FileNotFoundError
    pygame.mixer.music.load(fullname)


def make_sound(name):
    """Функция загрузки музыки"""
    fullname = os.path.join("origin", "media", 'music', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        raise FileNotFoundError
    sound = pygame.mixer.Sound(fullname)
    return sound


def load_file(filename):
    fullname = os.path.join("origin", "media", filename)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        raise FileNotFoundError
    return fullname