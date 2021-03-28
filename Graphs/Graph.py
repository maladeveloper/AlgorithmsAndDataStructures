class MatrixGraph:

    def __init__(self, list_rep=None):#list_rep is if adjacency list representation is passed into init

        if list_rep is not None:

            self.convert_list_to_matrix(list_rep)
        
        else:

            self.vert_dict = dict()#Stores the index of the vertex

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

            self.vert_dict[start_vert], self.vert_dict[end_vert] = 0, 1

            self.update_weight(start_vert, weight, end_vert)
        
        elif self.vert_dict.get(start_vert) is None:#Raise error if start vertex not in graph (not connecting to existing vertex!)

            print(f'''ERROR: Edge does not connect to pre-existing vertices! '{start_vert}' does not exist in graph!''')\

        elif self.vert_dict.get(end_vert) is None:# New row/coloumn must be added for new vertex

            self.vert_dict[end_vert] = len(self.matrix_grph) - 1

            self.matrix_grph = [row.append(None) for row in self.matrix_grph] #Add new coloumn for this vertex
            
            self.matrix_grph.append([None]*len(self.matrix_grph))#Add a new row for this vertex

            self.update_weight(start_vert, weight, end_vert)

        else:#Both vertices exist so simply update the weight

            self.update_weight(start_vert, weight, end_vert)



    def update_weight(self, start_vert, weight, end_vert):

        self.matrix_grph[self.vert_dict[start_vert]][self.vert_dict[end_vert]] = weight




        
