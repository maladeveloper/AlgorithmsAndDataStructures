from matrix_graph import MatrixGraph
from adjacency_list_graph import AdjacencyListGraph
from pprint import pprint, pformat
import logging
import os
import datetime
import shutil

##Variables 
log_fname = "graph_run_log.txt"

##Setup logging
try:

    os.remove(log_fname)

except:

    pass

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        logging.FileHandler(log_fname),
        logging.StreamHandler()
        ]
    )

def log(log_str, prettify=False):

    if prettify:

        log_str = pformat(log_str)
    
    logging.info(log_str)
    
    

##

graph_reps = [AdjacencyListGraph(), MatrixGraph()]


edges = [
    ["M", 2, "L"], 
    ["L", 4, "M"],
    ["M", 3, "F"],
    ["L", 1, "H"],
    ["H", 1, "J"],
    ["J", 5, "F"],
    ["H", 1, "M"],
    ["J", 5, "L"],
    ["J", 1, "K"],
    ["H", 2, "K"],
    ["K", 1, "G"],
    ["G", 1, "T"],
    ["K", 1, "C"]
]
log("=============================================================================")
log(f'''{datetime.datetime.now()}''')
log(f'''Edges adding to graph...''')

log(edges, True)

for my_graph in graph_reps:

    log(f'''\n{my_graph.name}-----------------------------------------------\n''')
    
    my_graph.add_many_edge(edges)

    log("Graph representation -\n")
    
    log(my_graph.print_out_grph(True), True)

    log("\nPath of Depth First Search (DFS) using first vertex of first edge added-")

    log(my_graph.dfs_path( edges[0][0]), True)

    log("\nPath of Breadth First Search (BFS) using the first vertex of first edge added-")

    log(my_graph.bfs_path(edges[0][0]), True)

log("\n=============================================================================")

##Save log as md
shutil.copyfile(log_fname, log_fname.replace("txt", "md"))