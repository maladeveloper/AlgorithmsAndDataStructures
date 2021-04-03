from pprint import pprint
from queue import Queue

class MatrixGraph:

    def __init__(self, list_rep=None):#list_rep is if adjacency list representation is passed into init

        self.name = "Matrix Graph"


        if list_rep is not None:

            self.convert_list_to_matrix(list_rep)
        
        else:

            self.vert_dict = dict()#Stores the index of the vertex

            self.index_dict = dict() #Stores the vertex of an index

            self.matrix_grph = [[None, None],[None,None]]

    '''
    Adds an edge to the graph
    edge: given in form (start vertex, weight, end vertex)
    '''
    def add_edge(self,edge):

        start_vert, weight, end_vert = edge[0], edge[1], edge[2]

        if start_vert == end_vert:#Cant add edges to a vertex to itself

            print(f'''"ERROR: Cannot add an edge { edge } from a vertex to itself !''')

        elif len(self.vert_dict) == 0:#The first vertex added need not connect to anything.

            self.add_to_dicts(start_vert, 0 )

            self.add_to_dicts(end_vert, 1)

            self.update_weight(start_vert, weight, end_vert)
        
        elif self.vert_dict.get(start_vert) is None:#Raise error if start vertex not in graph (not connecting to existing vertex!)

            print(f'''ERROR: Edge does not connect to pre-existing vertices! '{start_vert}' does not exist in graph!''')\

        elif self.vert_dict.get(end_vert) is None:# New row/coloumn must be added for new vertex

            self.add_to_dicts(end_vert, len(self.matrix_grph)) 

            self.matrix_grph.append([None]*len(self.matrix_grph))#Add a new row for this vertex

            [row.append(None) for row in self.matrix_grph] #Add new coloumn for this vertex
            
            self.update_weight(start_vert, weight, end_vert)

        else:#Both vertices exist so simply update the weight

            self.update_weight(start_vert, weight, end_vert)

    def add_to_dicts(self, vert, index):

        self.vert_dict[vert] = index

        self.index_dict[index] = vert


    def update_weight(self, start_vert, weight, end_vert):

        self.matrix_grph[self.vert_dict[start_vert]][self.vert_dict[end_vert]] = weight

    def add_many_edge(self, edges):

        for edge in edges:

            self.add_edge(edge)

    def dfs_path(self, start_vertex):

        path = []

        visited_vertices = set()

        def dfs_recurse(curr_vert):

            if curr_vert in visited_vertices:#Dont search through again

                return
            
            path.append(curr_vert)

            visited_vertices.add(curr_vert)

            row = self.matrix_grph[self.vert_dict[curr_vert]]
            
            for col in range(len(row)):

                if row[col] is not None:
                    
                    vertex = self.index_dict[col]

                    dfs_recurse(vertex)
        
        dfs_recurse(start_vertex)
        
        return path
    
    def bfs_path(self, start_vertex):

        path, visited_vertices, vertex_queue, curr_vertex = [start_vertex], set([start_vertex]), Queue(), start_vertex

        vertex_queue.put(start_vertex)

        while True:
            
            row = self.matrix_grph[self.vert_dict[curr_vertex]]

            for col in range(len(row)):

                if row[col] is not None:

                    vertex = self.index_dict[col]

                    if vertex not in visited_vertices:
                        
                        vertex_queue.put(vertex)

                        path.append(vertex)

                        visited_vertices.add(vertex)
            
            if vertex_queue.empty():

                break
            
            else:

                curr_vertex = vertex_queue.get()
        
        return path


    def print_out_grph(self, str_ret=False):

        if str_ret:

            return [self.vert_dict,self.matrix_grph]
            
        pprint([self.vert_dict,self.matrix_grph])
        
