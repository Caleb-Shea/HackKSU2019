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

def get_grass(window, x, y):
    return BGTile(window, f"grass{random.choice(grass_pallet)}", x, y)

def init_grass():
    bg_tiles = pyg.sprite.Group()
    for i in range(1, 19):
        for j in range(1, 10):
            tile = get_grass(window, 64*i, 64*j)
            bg_tiles.add(tile)

    return bg_tiles


if __name__ == '__main__':
    pyg.init()
    pyg.font.init()
    pyg.display.set_caption("Hack KState")
    window = pyg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    clock = pyg.time.Clock()
    score = 0
    level = 1
    time = lvl_data['lvl1']['time']


    font = pyg.font.Font(font_path, 28)

    player = Player(window)
    border = Border(window)
    bg_tiles = init_grass()
    tiles = pyg.sprite.Group()
    tile = Tile(window, 'grass5', 300, 300)
    tiles.add(tile)

    while True:

         # --- INPUT ---
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                terminate()
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    terminate()
            elif event.type == timer_tick:
                time -= 1


        event_keys = pyg.key.get_pressed()
        if event_keys[pyg.K_a]:
            if player.vel_x > -player.speed:
                player.vel_x -= player.accel
        if event_keys[pyg.K_d]:
            if player.vel_x < player.speed:
                player.vel_x += player.accel
        if event_keys[pyg.K_w]:
            if player.vel_y > -player.speed:
                player.vel_y -= player.accel
        if event_keys[pyg.K_s]:
            if player.vel_y < player.speed:
                player.vel_y += player.accel

        score_text = font.render(f"Score: {score}", True, color['black'])
        level_text = font.render(f"Level: {level}", True, color['black'])
        timer_text = font.render(f"Time Remaining: {time}", True, color['black'])

        window.fill(color['bg'])

        for bg_tile in bg_tiles:
            bg_tile.render()
        for tile in tiles:
            tile.render()
        border.render()

        player.update(border.rect, tiles)
        player.render()

        window.blit(score_text, (15, 15))
        window.blit(level_text, (1000, 15))
        window.blit(timer_text, (500, 15))

        pyg.display.flip()

        clock.tick(30)
