from pprint import pprint
import logging
import os
import datetime
import shutil
import time
from grid import Grid

'''
Problem: Given a NxN grid, how can you place N queens such that they do not attack each other?
Solutions to N queens problem are my own.
'''

class QueensNProblemGrid(Grid):

    def __init__(self, N, log=True, log_name="n_queens_log.txt"):

        super().__init__(N, N)

        self.N = N
        
        self.log = log

        self.log_name = log_name

        if self.log:

            self.create_logging()
    

        self.place_queens()

    def create_logging(self):
        
        logging.basicConfig(
            level=logging.INFO,
            format="%(message)s",
            handlers=[
                logging.FileHandler(self.log_name),
                logging.StreamHandler()
                ]
            )

        logging.getLogger().handlers = []

        logging.getLogger().addHandler(logging.FileHandler(self.log_name))

        logging.getLogger().addHandler(logging.StreamHandler())


        def log(log_str, prettify=False):

            if prettify:

                log_str = pformat(log_str)
            
            logging.info(log_str)
        
        self.log = log

    def find_next_positions(self, queen_pos, curr_positions):

        queen_row, queen_col = queen_pos[0], queen_pos[1]

        possible_pos = []

        ##Get all diagnoal positions from the queens position
        all_diags = self.get_all_diags(queen_pos, curr_positions)

        ##Iterate through each position and check if they are suitable.
        for pos in curr_positions:

            pos_row, pos_col = pos[0], pos[1]

            ##Check vertical and horizontal
            if queen_row != pos_row:

                 if queen_col != pos_col:

                    ##Check diagonals
                    if pos not in all_diags:

                        possible_pos.append(pos)

        return possible_pos
    
    def get_all_diags(self, queens_pos, curr_positions):

        row, col = queens_pos[0], queens_pos[1]
        
        all_diagonal_pos = []

        diag_dict = {
            "top_right":{
                "func": (lambda row, col: [row-1, col+1]),
                "not_end": False,
                "cur_row": row,
                "cur_col": col
            },
            "bottom_left":{
                "func":(lambda row, col: [row+1, col-1]),
                "not_end": False,
                "cur_row": row,
                "cur_col": col
            },
            "top_left":{
                "func":(lambda row, col: [row-1, col-1]),
                "not_end": False,
                "cur_row": row,
                "cur_col": col
            },
            "bottom_right":{
                "func":(lambda row, col: [row+1, col+1]),
                "not_end": False,
                "cur_row": row,
                "cur_col": col
            }
        }

        while True:

            not_end_arr = [diag["not_end"] for name, diag in diag_dict.items()]

            if  all(not_end_arr):

                break 

            for name, diagonal in diag_dict.items():

                if not diagonal["not_end"]:

                    check_row, check_col = diagonal["func"](diagonal["cur_row"], diagonal["cur_col"])

                    diagonal["cur_row"], diagonal["cur_col"] = check_row, check_col


                    if check_row >= 0 and check_col >= 0 and check_row < self.N and check_col < self.N:
                        
                        all_diagonal_pos.append([check_row, check_col])
                    
                    else:
                    
                        diagonal["not_end"] = True
        
        return all_diagonal_pos

    def place_queens(self):

        if self.log:

            self.log(f'''======================================================================================================\n{datetime.datetime.now()}\n''')
            
            self.log(f'''Problem description: Given a {self.N}x{self.N} grid, how can you place {self.N} queens such that they do not attack each other?''')

            self.log(f'''Legend:\n\tx- Squares under attack by queen\n\tQ- Queen\n\t#- Available Space''')

        final_positions = []

        final_available_positions = []

        def recurse_queens(partial_sol, next_positions):

            if self.log:
                
                self.log(f'''\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Current Board~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')

                self.log(self.partial_grid_log(partial_sol, next_positions))

                self.log(f'''Queens at Positions: {partial_sol}\nNext Available Queen Positions:{next_positions}''')

            ##If final solution has been found then return
            if len(final_positions) != 0:

                return

            #Check if partial solution can be final solution
            if len(partial_sol) == self.N:

                [final_positions.append(pos) for pos in partial_sol]

                [final_available_positions.append(pos) for pos in next_positions]

                return

            ##Base case of no next positions then return
            if len(next_positions) == 0:

                if self.log:

                    self.log(f'''No Available positions to place Queen - BACKTRACK !''')
                    
                    self.log(f'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        
                return

            if self.log:

                self.log(f'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')

        
            for pos in next_positions:

                if len(final_positions) != 0:

                    return

                next_part_sols = partial_sol[:]

                next_part_sols.append(pos)

                next_poss_pos = self.find_next_positions(pos, next_positions)

                recurse_queens( next_part_sols, next_poss_pos)

        all_starting_positions = []

        for row in range(self.N):

            for col in range(self.N):

                all_starting_positions.append([row, col])
        
        recurse_queens([], all_starting_positions)

        ##If there is no final positions then the queens cannot be placed on board.
        if len(final_positions) == 0:

            fail_str = f'''No Solutions exists.'''

            self.log(fail_str) if self.log else print(fail_str)

        else:

            pass_str = f'''Solution has be found!'''

            self.log(f'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''') if self.log else print("\n")

            self.log(pass_str) if self.log else print(pass_str)

            self.place_final_queens(final_positions)

            self.log(self.print_grid()) if self.log else print(self.print_grid())

    def partial_grid_log(self, partial_sol, available_pos):

        new_grid =  [["x"]*self.N for i in range(self.N)] 

        #Add the queens
        for queen_pos in partial_sol:

            row, col = queen_pos[0], queen_pos[1]

            new_grid[row][col] = "Q"

        
        #Add the available positions
        for pos in available_pos:

            new_grid[pos[0]][pos[1]] = "#"
        
        print_str = self.print_grid(grid=new_grid)

        return print_str

    def place_final_queens(self, final_pos):

        for pos in final_pos:

            self.place_element("Q", row=pos[0], col=pos[1])

    


        