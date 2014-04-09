# M Ajtai's algorithm for generating expander graphs

# Author:   Vlad Burca
# Date:     April 3, 2014
# Updated:  April 9, 2014


# AJTAI EXPANDERS
# Description: 



import numpy

import helpers


NAME = ''


# We will construct the Random 3-regular graph in the following way:
#  having a list of nodes of the graph (size_H nodes), we will first randomize the list;
#  then for each i element of the first half, first[i], we will connect it to:
#       second[ (i-1) % size(second) ]  , where size(second) is actually size_H / 2
#       second[ i ]
#       second[ (i+1) % size(second ]
def generate_random_3graph(size_H, K=3):
  H = numpy.empty(shape=(size_H, K), dtype=numpy.int32)   # Generate H, empty adjacency list matrix
  H[:] = -1     # Initialize it with all elements -1

  nodes = numpy.arange(0, size_H)   # Generate list of nodes from 0 to size_H - 1

  randomized_nodes = numpy.random.permutation(nodes)  # Randomize their positions so that we construct random K-regular

  splits = numpy.array_split(randomized_nodes, 2)   # Split the nodes into two halves

  first   = splits[0]   # First half
  second  = splits[1]   # Second half

  for i, node1 in enumerate(first):

    node1_1 = second[ (i-1) % numpy.size(second) ]
    node1_2 = second[ i ]
    node1_3 = second[ (i+1) % numpy.size(second) ]

    H[node1][0]                               = node1_1   # Create the edge (node1, node1_1)
    H[node1_1][helpers.get_rank(node1_1, H)]  = node1   # Create the edge (node1_1, node1)

    H[node1][1]                               = node1_2   # Create the edge (node1, node1_2)
    H[node1_2][helpers.get_rank(node1_2, H)]  = node1   # Create the edge (node1_2, node1)

    H[node1][2]                               = node1_3   # Create the edge (node1, node1_3)
    H[node1_3][helpers.get_rank(node1_3, H)]  = node1   # Create the edge (node1_3, node1)

  return H


# Swaps the edges edge1=(x, y) and edge2=(u, v) with (x, v) and (y, u)
# !! Note !! Even though the generation of random graphs does not create multi-edges,
#       this method MIGHT CREATE MULTI EDGES
def swap(edge1, edge2, H):
  x = edge1[0]
  y = edge1[1]
  u = edge2[0]
  v = edge2[1]

  iy = numpy.where(H[x]==y)[0][0]    # Get the index of y in the adjacency list of x
  ix = numpy.where(H[y]==x)[0][0]    # Get the index of x in the adjacency list of y
  iv = numpy.where(H[u]==v)[0][0]    # Get the index of v in the adjacency list of u
  iu = numpy.where(H[v]==u)[0][0]    # Get the index of u in the adjacency list of v  

  # Do the swap

  # Create (x, v)
  H[x][iy] = v
  H[v][iu] = x
  # Create (y, u)
  H[y][ix] = u
  H[u][iv] = y

  return H


def GENERATE_AJTAI_EXPANDERS(size_H, EPSILON, s, K=3):

  print "[" + str(size_H) + "]: " + "s= " + str(s) + "\t EPSILON= " + str(EPSILON)

