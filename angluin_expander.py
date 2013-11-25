# Dana Angluin's algorithm for generating expander graphs

# Author:   Vlad Burca
# Date:     November 23, 2013
# Updated:  November 24, 2013


# ANGLUIN EXPANDERS
# Description: 
# Generates the H matrix from matrices A and B.
# H is an adjacency matrix constructed by adding edges between nodes in A and B
# on the following rules:
#   (x, y) of A is connected to the following nodes of B:
#     (x, y)
#     (x + y, y)
#     (y + 1, -x)


import numpy

import helpers


NAME = '[ANGLUIN]'


def GENERATE_ANGLUIN_EXPANDERS(size, cross_Z, A_indices, n, output_adjacency):
  size_H = 2 * size
  k = 3

  print NAME + " Generating H (adjacency list matrix) of size " + str(size_H) + " x " + str(k) + " ... "

  H = numpy.empty(shape=(size_H, k), dtype=numpy.int32)   # Generate H, empty adjacency list matrix

  for row in A_indices:
    for element_index in row:   # Get the tuple index from the matrix of indices (A)
      x = cross_Z[element_index][0]   # Grab first value
      y = cross_Z[element_index][1]   # Grab second value

      i = cross_Z.index((x, y))       # Grab the index of the (x, y) element

      # connect to (x, y) in B
      j = cross_Z.index((x, y)) + size   # add the shift in the H indexing       

      H[i][0] = j      # node with index i is connected to node with index j
      H[j][0] = i      # vice-versa

      # connect to (x + y, y) in B
      j = cross_Z.index(((x + y) % n, y)) + size

      H[i][1] = j
      H[j][1] = i

      # connect to (y + 1, -x) in B
      j = cross_Z.index(((y + 1) % n, (-x) % n)) + size

      H[i][2] = j
      H[j][2] = i


  print NAME + " Generated adjacency list matrix H."

  if output_adjacency == True:
    helpers.write_H_matrix(H, NAME)

  print NAME + " Calculating second highest eigenvalue of H ... "

  eigenvalue = helpers.generate_eigenvalue(H, size_H, k)

  print NAME + " Calculated highest eigenvalue of H."

  helpers.write_result(NAME, n, eigenvalue)  

#  print NAME + " Second highest eigenvalue = " + str(eigenvalue)