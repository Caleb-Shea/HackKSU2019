import pygame as pyg

from constants import *


class Player(pyg.sprite.Sprite):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.image = pyg.image.load(img_path['player'])
        self.rect = self.image.get_rect()

        self.speed = 8

        self.vel_x = 0
        self.vel_y = 0

        self.rect.x = WIN_WIDTH / 2
        self.rect.y = WIN_HEIGHT / 2

    def move_x(self):
        self.rect.x += self.vel_x

    def move_y(self):
        self.rect.y += self.vel_y

    def update(self):
        self.move_x()
        self.move_y()

        self.vel_x *= .8
        if abs(self.vel_x) < .1: self.vel_x = 0

        self.vel_y *= .8
        if abs(self.vel_y) < .1: self.vel_y = 0


    def render(self):
        self.window.blit(self.image, self.rect)


class Tile(pyg.sprite.Sprite):
    def __init__(self, window, type, x, y):
        super().__init__()
        self.window = window
        self.image = pyg.image.load(img_path[type])
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def render(self):
        self.window.blit(self.image, self.rect)

class Border(pyg.sprite.Sprite):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.image = pyg.Rect(64, 64, 1088, 512)
        self.rect = self.image.get_rect()

    def render(self):
        self.window.blit(self.image, self.rect)
