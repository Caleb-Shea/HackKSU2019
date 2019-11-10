import pygame as pyg
import os

WIN_WIDTH = 1280
WIN_HEIGHT = 704

 # Custom events
timer_tick = pyg.USEREVENT + 1
pyg.time.set_timer(timer_tick, 1000)
player_death = pyg.event.Event(pyg.USEREVENT + 2)

color = {'bg' :    (200, 200, 250),
         'black' : (  0,   0,   0)}

mypath = os.path.dirname(os.path.realpath(__file__))
img_path = {'player1' : os.path.join(mypath, 'assets/imgs/player1.png'),
            'player2' : os.path.join(mypath, 'assets/imgs/player2.png'),
            'player3' : os.path.join(mypath, 'assets/imgs/player3.png'),
            'player4' : os.path.join(mypath, 'assets/imgs/player4.png'),
            'grass1'  : os.path.join(mypath, 'assets/imgs/grass1.png'),
            'grass2'  : os.path.join(mypath, 'assets/imgs/grass2.png'),
            'grass3'  : os.path.join(mypath, 'assets/imgs/grass3.png'),
            'grass4'  : os.path.join(mypath, 'assets/imgs/grass4.png'),
            'grass5'  : os.path.join(mypath, 'assets/imgs/grass5.png'),
            'stone'   : os.path.join(mypath, 'assets/imgs/stone1.png'),
            'tree'    : os.path.join(mypath, 'assets/imgs/tree.png'),
            'exit'    : os.path.join(mypath, 'assets/imgs/exit.png')}

font_path = os.path.join(mypath, 'assets/fonts/font.ttf')

sound_path = {'bg_music' : os.path.join(mypath, 'assets/sound/bg_music.ogg'),
              'death'    : os.path.join(mypath, 'assets/sound/death.ogg')}


lvl_data = {'1' : {'time' : 10,
                   'grass_pallet' : [1, 2, 2, 4],
                   'num_tiles' : (18, 9),
                   'player_spawn' : (960, 128),
                   'trees' : [(576, 448), (128, 256)],
                   'statics' : [(1088, 64, 'stone'), (128, 512, 'stone')],
                   'pitfalls' : [(128, 128, [1, 1, 1, 1]), (1088, 128, [1, 1, 0, 1]), (1088, 192, [0, 1, 0, 1]), (1088, 256, [0, 1, 0, 1]), (1088, 320, [0, 1, 0, 1]), (1088, 384, [0, 1, 1, 0]), (1024, 384, [1, 0, 1, 0]), (960, 384, [1, 0, 1, 0]), (896, 384, [1, 0, 1, 0]), (832, 384, [1, 0, 1, 0]), (768, 384, [1, 0, 1, 1]), (128, 320, [1, 1, 1, 1]), (576, 320, [1, 1, 1, 1])],
                   'exit' : (1152, 64),
                   'pushables' : []
                   },
            '2' : {'time' : 10,
                   'grass_pallet' : [1, 1, 1, 1, 2, 2, 4],
                   'trees' : [(128, 128), (256, 256), (512, 256), (512, 128), (640, 256), (704, 128), (896, 128), (1024, 256), (64, 256), (128, 320), (320, 384), (704, 384), (896, 384), (640, 192), (640, 448), (832, 192), (448, 64), (1024, 64), (256, 64), (448, 384)],
                   'num_tiles' : (18, 9),
                   'player_spawn' : (100, 600),
                   'exit' : (192, 256),
                   'pitfalls' : [(640, 256, [1, 1, 1, 1]), (1088, 512, [1, 1, 1, 1]), (128, 512, [1, 0, 1, 1]), (192, 512, [1, 1, 1, 0]), (832, 384, [1, 1, 1, 1]), (640, 128, [1, 1, 1, 1])],
                   'statics' : [],
                   'pushables' : []
                   },
            '3' : {'time' : 10,
                   'grass_pallet' : [1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                   'trees' : [],
                   'num_tiles' : (6, 6),
                   'player_spawn' : (128, 128),
                   'exit' : (384, 384),
                   'pitfalls' : [],
                   'statics' : [(256, 384, 'stone'), (384, 256, 'stone')],
                   'pushables' : [(256, 256, 'stone')]
                  },



            '5' : "lots of pads"


                   }
