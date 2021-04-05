class Grid:

    def __init__(self, row, col):

        self.row, self.col = row, col

        self.grid = self.create_grid()
    
    def create_grid(self):

        return [[None] * self.col for i in range(self.row)]  
    
    
    def place_element(self, element, row=None, col=None):

        ##Checks on row and col types and range
        if row is None or col is None:

            print("ERROR: Pass in Row and Coloumn.")
        
        elif type(row) != int or type(col) != int:

            print("ERROR: Row and Coloumn must be type int.")
        
        elif row > (self.row -1):

            print("ERROR: Row index out of range.")
        
        elif col > (self.col -1):

            print("ERROR: Coloumn index out of range.")
        
        else:#Now we can place the element

            self.grid[row][col] = element

    def print_grid(self, grid=None):

        grid = self.grid if grid is None else grid

        print_str = "\n"

        print_str += "-" * (self.col * 2)

        #print_str += "\n"

        for row_pos in range(len(grid)):

            print_str += "\n"

            for elem in grid[row_pos]:

                if elem is None:

                    print_str += "#"
                
                else:

                    print_str += str(elem)
                
                print_str += " "
            
            print_str += "\n"
                
        print_str += "-" * (self.col * 2)

        print_str += "\n"

        return print_str