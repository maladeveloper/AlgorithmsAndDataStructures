from pprint import pprint
from queue import Queue

class AdjacencyListGraph:
    
    def __init__(self, matrix_ref=None):

        self.name = "Adjacency List Graph"

        if matrix_ref is not None:

            self.convert_matrix_to_list(matrix_ref)
        
        else:

            self.graph = dict()
    
    '''
    Adds an edge to the graph
    edge: given in form (start vertex, weight, end vertex)
    '''
    def add_edge(self,edge):

        start_vert, weight, end_vert = edge[0], edge[1], edge[2]

        if start_vert not in self.graph: #Is a problem if the start vertex is not present

            if len(self.graph) == 0: #Make an exeption for first vertex

                self.graph[start_vert], self.graph[end_vert] = {end_vert:weight}, dict()
            
            else:

                print(f'''ERROR: Cannot add this edge as this graph does not have the start vertex "{start_vert}"''')
        
        else:

            self.graph[start_vert][end_vert] = weight

            self.graph[end_vert] = {} if (end_vert not in self.graph) else self.graph[end_vert] #Add the end vertex too.

    '''
    Adds multiple edges to the graph from array.
    edge: given in form (start vertex, weight, end vertex)
    '''
    def add_many_edge(self, edges):

        for edge in edges:

            self.add_edge(edge)
    
    def dfs_path(self, vert):

        path = []

        visited_vertices = set()

        def dfs_recurse(curr_vert):

            if curr_vert in visited_vertices:

                return 
            
            path.append(curr_vert)

            visited_vertices.add(curr_vert)

            for vertex in self.graph[curr_vert]:

                dfs_recurse(vertex)
            
        dfs_recurse(vert)

        return path

    def bfs_path(self, start_vertex):

        path, visited_vertices, vertex_queue, curr_vertex = [start_vertex], set([start_vertex]), Queue(), start_vertex

        vertex_queue.put(start_vertex)
        
        while True:

            for vertex in self.graph[curr_vertex]:

                if vertex[0] not in visited_vertices:
                    
                    vertex_queue.put(vertex[0])

                    path.append(vertex)

                    visited_vertices.add(vertex)
            
            if vertex_queue.empty():

                break
            
            else:

                curr_vertex = vertex_queue.get()
        
        return path


    def print_out_grph(self, str_ret=False):

        if str_ret:

            return self.graph
            
        pprint(self.graph)
    



