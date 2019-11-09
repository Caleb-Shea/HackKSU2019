import pygame as pyg

from constants import *


class Player(pyg.sprite.Sprite):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.image = pyg.image.load(img_path['player'])
        self.image = pyg.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()

        self.speed = 16
        self.accel = 2

        self.vel_x = 0
        self.vel_y = 0

        self.rect.x = WIN_WIDTH / 2
        self.rect.y = WIN_HEIGHT / 2

    def move_x(self):
        self.rect.x += self.vel_x

    def move_y(self):
        self.rect.y += self.vel_y

    def border_check(self, border):
        if self.rect.bottom > border.bottom:
            self.vel_y = 0
            self.rect.bottom = border.bottom

        if self.rect.top < border.top:
            self.vel_y = 0
            self.rect.top = border.top

        if self.rect.left < border.left:
            self.vel_x = 0
            self.rect.left = border.left

        if self.rect.right > border.right:
            self.vel_x = 0
            self.rect.right = border.right

    def collide_x(self, tiles):
        for tile in tiles:
            if pyg.Rect.colliderect(self.rect, tile.rect):
                if self.vel_x < 0:
                    self.rect.left = tile.rect.right
                    self.vel_x = 0
                elif self.vel_x > 0:
                    self.rect.right = tile.rect.left
                    self.vel_x = 0

    def collide_y(self, tiles):
        for tile in tiles:
            if pyg.Rect.colliderect(self.rect, tile.rect):
                if self.vel_y < 0:
                    self.rect.top = tile.rect.bottom
                    self.vel_y = 0
                elif self.vel_y > 0:
                    self.rect.bottom = tile.rect.top
                    self.vel_y = 0

    def update(self, border, tiles):
        self.move_x()
        self.collide_x(tiles)
        self.move_y()
        self.collide_y(tiles)

        self.vel_x *= .8
        if abs(self.vel_x) < .1: self.vel_x = 0

        self.vel_y *= .8
        if abs(self.vel_y) < .1: self.vel_y = 0

        self.border_check(border)

    def render(self):
        self.window.blit(self.image, self.rect)


class BGTile(pyg.sprite.Sprite):
    def __init__(self, window, type, x, y):
        super().__init__()
        self.window = window
        self.image = pyg.image.load(img_path[type])
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

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
        self.rect = pyg.Rect(64, 64, 1152, 576)

    def render(self):
        pyg.draw.rect(self.window, color['black'], (64, 64, 1152, 576), 5)
