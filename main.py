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
    for i in range(1, lvl_data[level]['num_tiles'][0] + 1):
        for j in range(1, lvl_data[level]['num_tiles'][1] + 1):
            tile = BGTile(window, f"grass{random.choice(lvl_data[level]['grass_pallet'])}", 64*i, 64*j)
            bg_tiles.add(tile)

    return bg_tiles

def next_level(window, level, player,statics, pitfalls, trees):
    level = str(int(level) + 1)
    player.__init__(window, level)
    statics.empty()
    pitfalls.empty()
    trees.empty()


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
    statics = pyg.sprite.Group()
    static = Static(window, 'grass5', 300, 300)
    statics.add(static)
    static = Static(window, 'stone', 512, 512)
    statics.add(static)

    pitfalls = pyg.sprite.Group()
    pitfall = Pitfall(window, 128, 128, wall=[1, 0, 0, 1])
    pitfalls.add(pitfall)
    pitfall = Pitfall(window, 128, 192, wall=[0, 1, 1, 1])
    pitfalls.add(pitfall)
    pitfall = Pitfall(window, 192, 128, wall=[1, 1, 1, 0])
    pitfalls.add(pitfall)

    trees = pyg.sprite.Group()
    for pos in lvl_data[level]['trees']:
        tree = Tree(window, pos[0], pos[1])
        trees.add(tree)

    while True:

         # --- INPUT ---
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                terminate()
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    terminate()
                elif event.key == pyg.K_SPACE:
                    next_level(window, level, player, statics, pitfalls, trees)
                    level = str(int(level) + 1)
                    time = lvl_data[level]['time']
                    bg_tiles = init_grass(level)
                elif event.key == pyg.K_k:
                    player.die()
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
        for static in statics:
            static.render()
        border.render()

        for pit in pitfalls:
            pit.render()

        player.update(border.rect, statics, pitfalls, trees)
        player.render()

        for tree in trees:
            tree.render()

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
