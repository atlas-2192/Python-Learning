"""
Clone of 2048 game.
"""

#import poc_2048_gui        
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    ret_line = [0 for dummy_x in xrange(len(line))]
    ret_index = 0
    pre_v = -1
    for i in range ( 0, len(line) ):
        if line[i] != 0:
            if  line[i] == pre_v:
                ret_line[ret_index] = pre_v*2
                ret_index += 1
                pre_v=-1
            else:
                if pre_v == -1:                
                    pre_v = line[i]
                else:
                    ret_line[ret_index] = pre_v
                    ret_index += 1
                    pre_v = line[i]
    if pre_v != -1:
        ret_line[ret_index] = pre_v
    return ret_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    matrix = []
    grid_height = 0
    grid_width = 0
    
    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.matrix = [[0 for dummy_x in xrange(self.grid_width)] for dummy_x in xrange(self.grid_height)] 
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return "["+ ''.join(str(e) for e in self.matrix) + "]"

    def get_grid_height(self):
        """
        Get the height of the board.
        """        
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        #global OFFSETS
        if OFFSETS[direction] == (1,0):      #UP            
            for j in range(0, self.grid_width):
                process_list = []
                for i in range(0, self.grid_height):
                    process_list.append(self.matrix[i][j])
                process_list = merge(process_list)
                for i in range(0, self.grid_height):
                    self.matrix[i][j] = process_list[i]
        elif OFFSETS[direction] == (-1,0):   #DOWN        
            for j in range(0, self.grid_width):
                process_list = []
                for i in range(0, self.grid_height):
                    process_list.append(self.matrix[self.grid_height-1-i][j])
                process_list = merge(process_list)
                for i in range(0, self.grid_height):
                    self.matrix[self.grid_height-1-i][j] = process_list[i]
        elif OFFSETS[direction] == (0,1):    #LEFT            
            for i in range(0, self.grid_height):
                self.matrix[i] = merge(self.matrix[i])
        elif OFFSETS[direction] == (0,-1):   #RIGHT
            for i in range(0, self.grid_height):
                process_list = []
                for j in range(0, self.grid_width):
                    process_list.append( self.matrix[i][self.grid_width-1-j] )
                process_list = merge(process_list)
                for j in range(0, self.grid_width):
                    self.matrix[i][self.grid_width-1-j] = process_list[j]                
        self.new_tile()
        print self
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        ary_index = -1
        val_array = []
        for i in range(0, self.grid_height):
            for j in range(0, self.grid_width):             
                ary_index += 1
                if self.matrix[i][j] == 0:
                    #print "i=",i,"j=",j,"is empty index=",ary_index
                    val_array.append(ary_index)
        if len(val_array) > 0:
            #print "empty ary size=", str(len(val_array))
            ary_index = random.randint(0, len(val_array)-1)
            #print "random index=", ary_index
            ary_index = val_array[ary_index]
            #print "empty index=", ary_index
            if ary_index >= self.grid_width:
                index_x = ary_index // self.grid_width
            else:
                index_x = 0
            index_y = ary_index % self.grid_width
            #print "index x=",index_x, "y=", index_y
            if self.matrix[index_x][index_y] != 0:
                print "ERROR"
            #print "x=",index_x,"y=",index_y
            if random.randint(0,100) > 90:
                self.matrix[index_x][index_y] = 4 
                #print "x=",index_x,"y=",index_y
            else:
                self.matrix[index_x][index_y] = 2
     
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.matrix[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.matrix[row][col]
 
    
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
game = TwentyFortyEight(4, 4)
print game
game.set_tile(0,0,2)
game.set_tile(1,1,2)
game.set_tile(2,2,2)
game.set_tile(3,3,2)
print game
game.move(UP)
print game