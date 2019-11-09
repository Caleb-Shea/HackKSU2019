import pygame as pyg
import random

from classes import *
from constants import *


 # Custom events
timer_tick = pyg.USEREVENT + 1
pyg.time.set_timer(timer_tick, 1000)

def terminate():
    pyg.quit()
    raise SystemExit()

def init_grass(level):
    bg_tiles = pyg.sprite.Group()
    for i in range(1, 19):
        for j in range(1, 10):
            tile = BGTile(window, f"grass{random.choice(lvl_data[level]['grass_pallet'])}", 64*i, 64*j)
            bg_tiles.add(tile)

    return bg_tiles

def next_level(window, level, player, tiles, pitfalls):
    level = str(int(level) + 1)
    player.__init__(window, level)
    tiles.empty()
    pitfalls.empty()


if __name__ == '__main__':
    pyg.init()
    pyg.font.init()
    pyg.display.set_caption("Hack KState")
    window = pyg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    clock = pyg.time.Clock()
    score = 0
    level = '1'
    time = lvl_data[level]['time']


    font = pyg.font.Font(font_path, 28)

    player = Player(window, level)
    border = Border(window)
    bg_tiles = init_grass(level)
    tiles = pyg.sprite.Group()
    tile = Tile(window, 'grass5', 300, 300)
    tiles.add(tile)
    tile = Tile(window, 'stone', 512, 512)
    tiles.add(tile)
    pitfalls = pyg.sprite.Group()
    pitfall = Pitfall(window, 128, 128)
    pitfalls.add(pitfall)

    while True:

         # --- INPUT ---
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                terminate()
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    terminate()
                elif event.key == pyg.K_SPACE:
                    next_level(window, level, player, tiles, pitfalls)
                    level = str(int(level) + 1)
                    time = lvl_data[level]['time']
                    bg_tiles = init_grass(level)
            elif event.type == timer_tick:
                time -= 1
                if time == 0:
                    player.die()
                    time = lvl_data[level]['time']



        event_keys = pyg.key.get_pressed()
        if event_keys[pyg.K_a]:
            if player.vel_x > -player.speed:
                player.vel_x -= player.accel
                player.image = pyg.image.load(img_path['player4'])
        if event_keys[pyg.K_d]:
            if player.vel_x < player.speed:
                player.vel_x += player.accel
                player.image = pyg.image.load(img_path['player2'])
        if event_keys[pyg.K_w]:
            if player.vel_y > -player.speed:
                player.vel_y -= player.accel
                player.image = pyg.image.load(img_path['player1'])
        if event_keys[pyg.K_s]:
            if player.vel_y < player.speed:
                player.vel_y += player.accel
                player.image = pyg.image.load(img_path['player3'])

        score_text = font.render(f"Score: {score}", True, color['black'])
        level_text = font.render(f"Level: {level}", True, color['black'])
        timer_text = font.render(f"Time Remaining: {time}", True, color['black'])
        death_text = font.render(f"Deaths: {player.deaths}", True, color['black'])

        window.fill(color['bg'])

        for bg_tile in bg_tiles:
            bg_tile.render()
        for tile in tiles:
            tile.render()
        border.render()

        for pit in pitfalls:
            pit.render()

        player.update(border.rect, tiles, pitfalls)
        player.render()

        window.blit(score_text, (15, 15))
        window.blit(level_text, (1075, 15))
        window.blit(timer_text, (700, 15))
        window.blit(death_text, (300, 15))

        pyg.display.flip()

        clock.tick(30)


def terrainGenList():
    gen = []
    for i in range(18):
        tmp = []
        for j in range(9):
            tmp.append(random.randint(1, 12))

        gen.append(tmp)

    return gen
