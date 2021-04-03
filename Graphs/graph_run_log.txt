=============================================================================
2021-04-03 12:31:12.539922
Edges adding to graph...
[['M', 2, 'L'],
 ['L', 4, 'M'],
 ['M', 3, 'F'],
 ['L', 1, 'H'],
 ['H', 1, 'J'],
 ['J', 5, 'F'],
 ['H', 1, 'M'],
 ['J', 5, 'L'],
 ['J', 1, 'K'],
 ['H', 2, 'K'],
 ['K', 1, 'G'],
 ['G', 1, 'T'],
 ['K', 1, 'C']]

Adjacency List Graph-----------------------------------------------

Graph representation -

{'C': {},
 'F': {},
 'G': {'T': 1},
 'H': {'J': 1, 'K': 2, 'M': 1},
 'J': {'F': 5, 'K': 1, 'L': 5},
 'K': {'C': 1, 'G': 1},
 'L': {'H': 1, 'M': 4},
 'M': {'F': 3, 'L': 2},
 'T': {}}

Path of Depth First Search (DFS) using first vertex of first edge added-
['M', 'L', 'H', 'J', 'F', 'K', 'G', 'T', 'C']

Path of Breadth First Search (BFS) using the first vertex of first edge added-
['M', 'L', 'F', 'H', 'J', 'K', 'G', 'C', 'T']

Matrix Graph-----------------------------------------------

Graph representation -

[{'C': 8, 'F': 2, 'G': 6, 'H': 3, 'J': 4, 'K': 5, 'L': 1, 'M': 0, 'T': 7},
 [[None, 2, 3, None, None, None, None, None, None],
  [4, None, None, 1, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [1, None, None, None, 1, 2, None, None, None],
  [None, 5, 5, None, None, 1, None, None, None],
  [None, None, None, None, None, None, 1, None, 1],
  [None, None, None, None, None, None, None, 1, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None]]]

Path of Depth First Search (DFS) using first vertex of first edge added-
['M', 'L', 'H', 'J', 'F', 'K', 'G', 'T', 'C']

Path of Breadth First Search (BFS) using the first vertex of first edge added-
['M', 'L', 'F', 'H', 'J', 'K', 'G', 'C', 'T']

=============================================================================
