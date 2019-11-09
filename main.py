import pygame as pyg


from classes import *
from constants import *


def terminate():
    pyg.quit()
    raise SystemExit()


def draw_border(window):
    pyg.draw.rect(window, color['black'], (64, 64, 1088, 512), 5)

if __name__ == '__main__':
    pyg.init()
    pyg.display.set_caption("Hack KState")
    window = pyg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    clock = pyg.time.Clock()

    player = Player(window)
    tiles = pyg.sprite.Group()

    for i in range(1, 19):
        for j in range(1, 10):
            tile = Tile(window, 'grass', 64*i, 64*j)
            tiles.add(tile)


    while True:

         # --- INPUT ---
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                terminate()
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    terminate()


        event_keys = pyg.key.get_pressed()
        if event_keys[pyg.K_a]:
            if player.vel_x > -16:
                player.vel_x -= 2
        if event_keys[pyg.K_d]:
            if player.vel_x < 16:
                player.vel_x += 2
        if event_keys[pyg.K_w]:
            if player.vel_y > -16:
                player.vel_y -= 2
        if event_keys[pyg.K_s]:
            if player.vel_y < 16:
                player.vel_y += 2






        window.fill(color['bg'])

        for tile in tiles:
            tile.render()
        draw_border(window)

        player.update()
        player.render()


        pyg.display.flip()

        clock.tick(30)
