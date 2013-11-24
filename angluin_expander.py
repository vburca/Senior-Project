# Dana Angluin's algorithm for generating expander

# Author:   Vlad Burca
# Date:     November 23, 2013
# Updated:  November 23, 2013


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


def GENERATE_ANGLUIN_EXPANDERS(size, cross_Z, A_indices, n):
  size_H = 2 * size

  print NAME + " Generating H of size " + str(size_H) + " x " + str(size_H) + " ... "

  H = numpy.zeros(shape=(size_H, size_H), dtype=numpy.int64)  # Generate H, empty adjacency matrix

  for row in A_indices:
    for element_index in row:   # Get the tuple index from the matrix of indices (A)
      x = cross_Z[element_index][0]   # Grab first value
      y = cross_Z[element_index][1]   # Grab second value

      i = cross_Z.index((x, y))       # Grab the index of the (x, y) element

      # connect to (x, y) in B
      j = cross_Z.index((x, y)) + size   # add the shift in the H indexing       

      H[i][j] += 1      # Increment the number of edges
      H[j][i] += 1      # symmetric by first diagonal

      # connect to (x + y, y) in B
      j = cross_Z.index(((x + y) % n, y)) + size

      H[i][j] += 1
      H[j][i] += 1

      # connect to (y + 1, -x) in B
      j = cross_Z.index(((y + 1) % n, (-x) % n)) + size

      H[i][j] += 1
      H[j][i] += 1

  print NAME + " Generated adjacency matrix H."

  helpers.write_H_matrix(H, NAME)

  print NAME + " Calculating eigenvalues of H ... "

  eigenvalues = helpers.generate_and_write_eigenvalues(H, NAME)

  print NAME + " Calculated eigenvalues of H."  

  print NAME + " Second highest eigenvalue = " + str(eigenvalues[1])