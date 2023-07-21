import numpy as np
import classes.tile as tile

class Supermarket():
    """_summary_
    """
    
    def __init__(self, size, blocked_tiles, locations):
        # create a grid of the specified size
        arr = np.empty(size, dtype=object)
        
        # iterate over the array and initialize Tile objects
        for i in range(size[0]):
            for j in range(size[1]):
                # assign Tile object with coordinates set as (i, j)
                arr[i, j] = tile.Tile('', [i, j], True, True)
                
                # check if tile is blocked
                if [i,j] in blocked_tiles:
                    arr[i, j].is_accessible = False
                else:
                    arr[i, j].is_accessible = True
                    
                # check if tile is any location
                if [i,j] in list(locations.values()):
                    for key, value in locations.items():
                        if value == [i,j]:
                            arr[i,j].location = key
        
        self.grid = arr
        
    

    