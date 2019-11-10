import pygame as pyg
import random

from classes import *
from constants import *


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

def next_level(window, level, player,statics, pitfalls, trees, pushables, imgs):
    level = str(int(level) + 1)
    player.__init__(window, level)
    statics.empty()
    pitfalls.empty()
    trees.empty()
    pushables.empty()
    imgs.empty()

def game_init():
    font30 = pyg.font.Font(font_path, 30)
    fin_text2 = font30.render("[PRESS SPACE TO BEGIN]", True, color['black'])

    bg = pyg.image.load(img_path['open_bg']).convert()
    window.blit(bg, (0, 0))
    window.blit(fin_text2, (WIN_WIDTH / 3, WIN_HEIGHT - 50))

    pyg.display.flip()

    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                terminate()
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_SPACE:
                    return

def game_over(score, deaths):
    font48 = pyg.font.Font(font_path, 48)
    font30 = pyg.font.Font(font_path, 30)
    if score > 0:
        fin_text1 = font48.render("YOU WIN", True, color['white'])
    else:
        fin_text1 = font48.render("YOU LOSE", True, color['white'])
    fin_text2 = font48.render(f"Score: {score}", True, color['white'])
    fin_text3 = font48.render(f"Deaths: {deaths}", True, color['white'])
    fin_text4 = font30.render("[PRESS SPACE TO QUIT]", True, color['white'])

    window.fill(color['black'])

    window.blit(fin_text1, (WIN_WIDTH / 3, 100))
    window.blit(fin_text2, (WIN_WIDTH / 3, 300))
    window.blit(fin_text3, (WIN_WIDTH / 3, 400))
    window.blit(fin_text4, (WIN_WIDTH / 3, WIN_HEIGHT - 50))


    pyg.display.flip()

    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                terminate()
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_SPACE:
                    terminate()

    terminate()


if __name__ == '__main__':
    pyg.init()
    pyg.font.init()
    pyg.mixer.init()
    pyg.display.set_caption("Lorem Ipsum")
    window = pyg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    bg_music = pyg.mixer.Sound(sound_path['bg_music'])
    bg_music.play(-1)

    clock = pyg.time.Clock()
    paused = False

    score = 0
    level = '1'
    time = lvl_data[level]['time']

    font = pyg.font.Font(font_path, 28)

    player = Player(window, level)
    border = Border(window, lvl_data[level]['num_tiles'])
    exit = Exit(window, level)

    time_death = True

    bg_tiles = init_grass(level)
    statics = pyg.sprite.Group()
    for data in lvl_data[level]['statics']:
        static = Static(window, data[2], data[0], data[1])
        statics.add(static)

    pushables = pyg.sprite.Group()
    for data in lvl_data[level]['pushables']:
        pushable = Pushable(window, data[0], data[1], data[2])
        pushables.add(pushable)

    imgs = pyg.sprite.Group()
    for data in lvl_data[level]['imgs']:
        img = Static(window, data[2], data[0], data[1])
        imgs.add(img)

    pitfalls = pyg.sprite.Group()
    for data in lvl_data[level]['pitfalls']:
        pit = Pitfall(window, data[0], data[1], wall=data[2])
        pitfalls.add(pit)

    trees = pyg.sprite.Group()
    for pos in lvl_data[level]['trees']:
        tree = Tree(window, pos[0], pos[1])
        trees.add(tree)



    game_init()

    while True:
        if paused:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    terminate()
                elif event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:
                        terminate()
                    elif event.key == pyg.K_TAB:
                        paused = False
        else:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    terminate()
                elif event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:
                        terminate()
                    elif event.key == pyg.K_TAB:
                        paused = True
                elif event.type == timer_tick:
                    if time_death:
                        time -= 1
                        if time == 0:
                            player.die()
                            time = lvl_data[level]['time']
                elif event.type == player_death.type:
                    time = lvl_data[level]['time']

            event_keys = pyg.key.get_pressed()
            if event_keys[pyg.K_a] or event_keys[pyg.K_LEFT]:
                if player.vel_x > -player.speed:
                    player.vel_x -= player.accel
                    player.image = pyg.image.load(img_path['player4'])
            if event_keys[pyg.K_d] or event_keys[pyg.K_RIGHT]:
                if player.vel_x < player.speed:
                    player.vel_x += player.accel
                    player.image = pyg.image.load(img_path['player2'])
            if event_keys[pyg.K_w] or event_keys[pyg.K_UP]:
                if player.vel_y > -player.speed:
                    player.vel_y -= player.accel
                    player.image = pyg.image.load(img_path['player1'])
            if event_keys[pyg.K_s] or event_keys[pyg.K_DOWN]:
                if player.vel_y < player.speed:
                    player.vel_y += player.accel
                    player.image = pyg.image.load(img_path['player3'])


            if pyg.Rect.colliderect(player.rect, exit.rect):
                if level == num_levels:
                    game_over(score, player.deaths)
                else:
                    score += lvl_data[level]['time'] + time - 5 * player.deaths
                    next_level(window, level, player, statics, pitfalls, trees, pushables, imgs)
                    level = str(int(level) + 1)
                    time = lvl_data[level]['time']
                    bg_tiles = init_grass(level)
                    exit.__init__(window, level)
                    border.__init__(window, lvl_data[level]['num_tiles'])
                    for pos in lvl_data[level]['trees']:
                        tree = Tree(window, pos[0], pos[1])
                        trees.add(tree)
                    for pos in lvl_data[level]['pitfalls']:
                        pit = Pitfall(window, pos[0], pos[1], pos[2])
                        pitfalls.add(pit)
                    for data in lvl_data[level]['statics']:
                        static = Static(window, data[2], data[0], data[1])
                        statics.add(static)
                    for data in lvl_data[level]['pushables']:
                        pushable = Pushable(window, data[0], data[1], data[2])
                        pushables.add(pushable)
                    for data in lvl_data[level]['imgs']:
                        img = Static(window, data[2], data[0], data[1])
                        imgs.add(img)

            score_text = font.render(f"Score: {score}", True, color['black'])
            level_text = font.render(f"Level: {level}", True, color['black'])
            timer_text = font.render(f"Time Remaining: {time}", True, color['black'])
            death_text = font.render(f"Deaths: {player.deaths}", True, color['black'])


            window.fill(color['bg'])
            for pushable in pushables: pushable.update(border)

            for bg_tile in bg_tiles: bg_tile.render()
            border.render()
            for static in statics: static.render()
            for img in imgs: img.render()
            for pushable in pushables: pushable.render()
            for pit in pitfalls: pit.render()

            exit.render()

            player.update(border.rect, statics, pitfalls, trees, pushables, imgs, level)
            player.render()

            for tree in trees: tree.render()

            window.blit(score_text, (15, 15))
            window.blit(level_text, (1075, 15))
            window.blit(timer_text, (700, 15))
            window.blit(death_text, (300, 15))

            pyg.display.flip()

            clock.tick(30)
