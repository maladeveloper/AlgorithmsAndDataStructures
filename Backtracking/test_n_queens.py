from n_queens_problem import QueensNProblemGrid
import os
import shutil

##Variables 
result_dir_folder = "NQueensResults"
num_max_queens = 10
##

##Remove the folder if there since it would have the old solutions
try:

    shutil.rmtree(result_dir_folder)

except:

    pass

os.mkdir(result_dir_folder)

##Iterate through ever increasing number of queens
for queens in range(num_max_queens):

    log_name = "n_" + str(queens) + "_queens_problem_log.txt"

    log_path = os.path.join(result_dir_folder, log_name)

    my_queen_grid = QueensNProblemGrid(queens, log=True, log_name=log_path)

    del my_queen_grid


