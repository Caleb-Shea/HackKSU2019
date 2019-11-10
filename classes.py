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

        self.speed = 8
        self.accel = 2

        self.vel_x = 0
        self.vel_y = 0

        self.deaths = deaths
        self.death_effect = pyg.mixer.Sound(sound_path['death'])
        self.death_effect.set_volume(.3)

        self.level = level
        self.rect.x = lvl_data[str(level)]['player_spawn'][0]
        self.rect.y = lvl_data[str(level)]['player_spawn'][1]

        self.pushing = False

    def die(self):
        self.death_effect.play()
        pyg.event.post(player_death)
        self.__init__(self.window, self.level, self.deaths + 1)

    def move_x(self):
        self.rect.x += self.vel_x / 2
        if not self.pushing:
            self.rect.x += self.vel_x / 2

    def move_y(self):
        self.rect.y += self.vel_y / 2
        if not self.pushing:
            self.rect.y += self.vel_y / 2

    def border_check(self, border):
        if not pyg.Rect.colliderect(self.rect, border):
            self.die()

    def img_collision(self, imgs, level):
        if level == '4':
            for img in imgs:
                if pyg.Rect.colliderect(self.rect, img.rect):
                    self.die()

    def collide_x(self, tiles, pitfalls, trees, pushables):
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

        for push in pushables:
            if pyg.Rect.colliderect(self.rect, push.rect):
                self.pushing = True
                if self.vel_x < 0:
                    push.rect.right = self.rect.left
                    push.vel_x = self.vel_x

                    push.collide_x(tiles, pitfalls, trees, pushables)
                    self.vel_x = push.vel_x

                elif self.vel_x > 0:
                    push.rect.left = self.rect.right
                    push.vel_x = self.vel_x

                    push.collide_x(tiles, pitfalls, trees, pushables)
                    self.vel_x = push.vel_x

            else:
                self.pushing = False

    def collide_y(self, tiles, pitfalls, trees, pushables):
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

        for push in pushables:
            if pyg.Rect.colliderect(self.rect, push.rect):
                self.pushing = True
                if self.vel_y < 0:
                    push.rect.bottom = self.rect.top
                    push.vel_y = self.vel_y

                    push.collide_y(tiles, pitfalls, trees, pushables)
                    self.vel_y = push.vel_y

                elif self.vel_y > 0:
                    push.rect.top = self.rect.bottom
                    push.vel_y = self.vel_y

                    push.collide_y(tiles, pitfalls, trees, pushables)
                    self.vel_y = push.vel_y

            else:
                self.pushing = False

    def update(self, border, tiles, pitfalls, trees, pushables, imgs, level):
        self.move_x()
        self.collide_x(tiles, pitfalls, trees, pushables)
        self.move_y()
        self.collide_y(tiles, pitfalls, trees, pushables)

        self.vel_x *= .8
        if abs(self.vel_x) < .1: self.vel_x = 0

        self.vel_y *= .8
        if abs(self.vel_y) < .1: self.vel_y = 0

        self.border_check(border)
        self.img_collision(imgs, level)

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
    def __init__(self, window, num_tiles):
        super().__init__()
        self.window = window
        self.rect = pyg.Rect(64, 64, 64 * num_tiles[0], 64 * num_tiles[1])

    def render(self):
        pyg.draw.rect(self.window, color['black'], self.rect, 5)

class Pitfall(pyg.sprite.Sprite):
    def __init__(self, window, x, y, wall):
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


class Exit(pyg.sprite.Sprite):
    def __init__(self, window, level):
        super().__init__()
        self.window = window
        self.image = pyg.image.load(img_path['exit'])
        self.rect = self.image.get_rect()

        self.rect.x = lvl_data[level]['exit'][0]
        self.rect.y = lvl_data[level]['exit'][1]

        self.level = level

    def render(self):
        self.window.blit(self.image, self.rect)


class Pushable(pyg.sprite.Sprite):
    def __init__(self, window, x, y, img):
        super().__init__()
        self.window = window
        self.image = pyg.image.load(img_path[img])
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.vel_x = 0
        self.vel_y = 0

    def border_check(self, border):
        if not pyg.Rect.colliderect(self.rect, border):
            self.kill()

    def collide_x(self, tiles, pitfalls, trees, pushables):
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

        for push in pushables:
            if not push.rect == self.rect:
                if pyg.Rect.colliderect(self.rect, push.rect):
                    if self.vel_x < 0:
                        push.rect.right = self.rect.left
                        push.vel_x = self.vel_x
                    elif self.vel_x > 0:
                        push.rect.left = self.rect.right
                        push.vel_x = self.vel_x

    def collide_y(self, tiles, pitfalls, trees, pushables):
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

        for push in pushables:
            if not push.rect == self.rect:
                if pyg.Rect.colliderect(self.rect, push.rect):
                    if self.vel_y < 0:
                        push.rect.top = self.rect.bottom
                        push.vel_y = self.vel_y
                    elif self.vel_y > 0:
                        push.rect.bottom = self.rect.top
                        push.vel_y = self.vel_y

    def update(self, border):
        self.border_check(border)

    def render(self):
        self.window.blit(self.image, self.rect)
