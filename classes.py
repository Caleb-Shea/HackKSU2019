import pygame as pyg

from constants import *


class Player(pyg.sprite.Sprite):
    def __init__(self, window):
        self.window = window
        self.image = pyg.image.load('')
        self.rect = self.image.get_rect()

        self.rect.x = WIN_WIDTH / 2
        self.rect.y = WIN_HEIGHT / 2


    def render(self):
        self.window.blit(self.image, self.rect)


class Tile(pyg.sprite.Sprite):
    def __init__(self, window, type, x, y):
        self.window = window
        self.image = pyg.image.load(img_path(type))
        self.rect = self.image.get_rect()

    def render(self):
        self.window.blit(self.image, self.rect)
