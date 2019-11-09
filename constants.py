import os

WIN_WIDTH = 1280
WIN_HEIGHT = 704


color = {'bg' :    (200, 200, 250),
         'black' : (  0,   0,   0)}

mypath = os.path.dirname(os.path.realpath(__file__))
img_path = {'player1' : os.path.join(mypath, 'assets/imgs/player1.png'),
            'player2' : os.path.join(mypath, 'assets/imgs/player2.png'),
            'player3' : os.path.join(mypath, 'assets/imgs/player3.png'),
            'player4' : os.path.join(mypath, 'assets/imgs/player4.png'),
            'grass1' : os.path.join(mypath, 'assets/imgs/grass1.png'),
            'grass2' : os.path.join(mypath, 'assets/imgs/grass2.png'),
            'grass3' : os.path.join(mypath, 'assets/imgs/grass3.png'),
            'grass4' : os.path.join(mypath, 'assets/imgs/grass4.png'),
            'grass5' : os.path.join(mypath, 'assets/imgs/grass5.png'),
            'stone' : os.path.join(mypath, 'assets/imgs/stone1.png'),
            'tree' : os.path.join(mypath, 'assets/imgs/tree.png')}

font_path = os.path.join(mypath, 'assets/fonts/font.ttf')


lvl_data = {'1' : {'time' : 20, 'grass_pallet' : [1, 2, 2, 4], 'num_tiles' : (18, 9), 'player_spawn' : (1036, 544), 'trees' : [(576, 448), (128, 256)]},
            '2' : {'time' : 15, 'grass_pallet' : [1, 1, 1, 1, 2, 2, 4], 'num_tiles' : (18, 9), 'player_spawn' : (100, 600)}}
