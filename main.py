import pygame as pyg


from classes import *
from constants import *


def terminate():
    pyg.quit()
    raise SystemExit()

if __name__ == '__main__':
    pyg.init()
    pyg.display.set_caption("Hack KState")
    window = pyg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    clock = pyg.time.Clock()


    while True:

         # --- INPUT ---
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                terminate()
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    terminate()


        window.fill(color['bg'])
        pyg.display.flip()


        clock.tick(30)
