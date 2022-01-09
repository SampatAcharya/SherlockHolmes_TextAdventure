_world = {}
starting_position = (0, 0)

def load_tiles(game_level):
    """Parses a file that describes the world space into the _world object"""
    # Note - Reads all the lines in the map and puts it in the variable row : ['|||LeaveCaveRoom|\n', '||EmptyCavePath|GiantSpiderRoom|\n', '||EmptyCavePath||\n', '||WolfRoom||\n', 'GiantSpiderRoom|EmptyCavePath|StartingRoom|EmptyCavePath|FindDaggerRoom\n']
    if game_level == 1:
        with open('location_1.txt', 'r') as f:
            rows = f.readlines()
    elif game_level == 2:
        with open('location_2.txt', 'r') as f:
            rows = f.readlines()
    else: 
        with open('location_3.txt', 'r') as f:
            rows = f.readlines()
    # Note - x_max will get the length of the rows i.e 5
    x_max = len(rows[0].split('|')) # Assumes all rows contain the same number of tabs
    # Note - length of the rows will also be 5, considering that the rows contains \n which denotes next line
    for y in range(len(rows)):
        # Note: cols will get the values between '| |'. so if its empty it will show like this -> ''. 
        # the values of cols at each iteration
        # ['', '', '', 'LeaveCaveRoom', '\n']
        # ['', '', 'EmptyCavePath', 'GiantSpiderRoom', '\n']
        # ['', '', 'EmptyCavePath', '', '\n']
        # ['', '', 'WolfRoom', '', '\n']
        # ['GiantSpiderRoom', 'EmptyCavePath', 'StartingRoom', 'EmptyCavePath', 'FindDaggerRoom\n']
        cols = rows[y].split('|')
        # x is the column and y is the row
        for x in range(x_max):
            # This is required because, as you can see that in the cols '\n' is also getting saved. Thats the reason we have to replace '\n' with ''
            tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
            # tile_name = cols[x]
            # this command is used to get the starting point of the game i.e. StartingRoom. 
            if tile_name == 'BakerStreet21':
                global starting_position
                starting_position = (x, y)
            # the esle part "getattr(__import__('tiles'), tile_name)(x, y)" gives the value of x and y with the text given in the tiles.py 
            # _world contains the position and the location of the map corresponding to the location. Go through "_world_content.txt" file to see for it is stored
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

def tile_exists(x, y):
    return _world.get((x, y))

