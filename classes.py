import pygame as pyg
import os
from pygame.math import Vector2

from constants import *


class Player(pyg.sprite.Sprite):
    def __init__(self, window, level, deaths=0):
        super().__init__()
        self.window = window
        self.image = pyg.image.load(img_path['player1'])
        self.blit_rect = self.image.get_rect()

        self.rect = self.blit_rect.inflate(-12, -12)

        self.speed = 12
        self.accel = 3

        self.vel_x = 0
        self.vel_y = 0

        self.deaths = deaths

        self.level = level
        self.rect.x = lvl_data[str(level)]['player_spawn'][0]
        self.rect.y = lvl_data[str(level)]['player_spawn'][1]

    def die(self):
        self.__init__(self.window, self.level, self.deaths + 1)

    def move_x(self):
        self.rect.x += self.vel_x

    def move_y(self):
        self.rect.y += self.vel_y

    def border_check(self, border):
        if not pyg.Rect.colliderect(self.rect, border):
            self.die()

    def collide_x(self, tiles, pitfalls, trees):
        for tile in tiles:
            if pyg.Rect.colliderect(self.rect, tile.rect):
                if self.vel_x < 0:
                    self.rect.left = tile.rect.right
                    self.vel_x = 0
                elif self.vel_x > 0:
                    self.rect.right = tile.rect.left
                    self.vel_x = 0

        for pit in pitfalls:
            if pyg.Rect.colliderect(self.rect, pit.rect):
                self.die()

        for tree in trees:
            if pyg.Rect.colliderect(self.rect, tree.rect):
                if self.vel_x < 0:
                    self.rect.left = tree.rect.right
                    self.vel_x = 0
                elif self.vel_x > 0:
                    self.rect.right = tree.rect.left
                    self.vel_x = 0

    def collide_y(self, tiles, pitfalls, trees):
        for tile in tiles:
            if pyg.Rect.colliderect(self.rect, tile.rect):
                if self.vel_y < 0:
                    self.rect.top = tile.rect.bottom
                    self.vel_y = 0
                elif self.vel_y > 0:
                    self.rect.bottom = tile.rect.top
                    self.vel_y = 0

        for pit in pitfalls:
            if pyg.Rect.colliderect(self.rect, pit.rect):
                self.die()

        for tree in trees:
            if pyg.Rect.colliderect(self.rect, tree.rect):
                if self.vel_y < 0:
                    self.rect.top = tree.rect.bottom
                    self.vel_y = 0
                elif self.vel_y > 0:
                    self.rect.bottom = tree.rect.top
                    self.vel_y = 0

    def update(self, border, tiles, pitfalls, trees):
        self.move_x()
        self.collide_x(tiles, pitfalls, trees)
        self.move_y()
        self.collide_y(tiles, pitfalls, trees)

        self.vel_x *= .8
        if abs(self.vel_x) < .1: self.vel_x = 0

        self.vel_y *= .8
        if abs(self.vel_y) < .1: self.vel_y = 0

        self.border_check(border)

        self.blit_rect.center = self.rect.center


    def render(self):
        self.window.blit(self.image, self.blit_rect)


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

class Static(pyg.sprite.Sprite):
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

class Pitfall(pyg.sprite.Sprite):
    def __init__(self, window, x, y, wall=[1, 1, 1, 1]):
        super().__init__()
        self.window = window
        self.image = pyg.Surface((64, 64))
        self.image.fill(color['bg'])
        self.blit_rect = self.image.get_rect()

        self.blit_rect.x = x
        self.blit_rect.y = y

        self.rect = self.blit_rect.inflate(-40, -40)

        self.wall = wall

    def render(self):
        self.window.blit(self.image, self.blit_rect)

        if self.wall[0]:
            pyg.draw.line(self.window, color['black'], (self.blit_rect.x, self.blit_rect.y), (self.blit_rect.x + 64, self.blit_rect.y), 5)
        if self.wall[1]:
            pyg.draw.line(self.window, color['black'], (self.blit_rect.x + 64, self.blit_rect.y), (self.blit_rect.x + 64, self.blit_rect.y + 64), 5)
        if self.wall[2]:
            pyg.draw.line(self.window, color['black'], (self.blit_rect.x, self.blit_rect.y + 64), (self.blit_rect.x + 64, self.blit_rect.y + 64), 5)
        if self.wall[3]:
            pyg.draw.line(self.window, color['black'], (self.blit_rect.x, self.blit_rect.y), (self.blit_rect.x, self.blit_rect.y + 64), 5)

class Tree(pyg.sprite.Sprite):
    def __init__(self, window, x, y):
        super().__init__()
        self.window = window
        self.image = pyg.image.load(img_path['tree'])
        self.blit_rect = self.image.get_rect()


        self.blit_rect.x = x
        self.blit_rect.y = y

        self.rect = self.blit_rect.inflate(-128, -128)

    def render(self):
        self.window.blit(self.image, self.blit_rect)
