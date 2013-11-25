# G.A Margulis' algorithm for generating expander graphs

# Author:   Vlad Burca
# Date:     November 23, 2013
# Updated:  November 24, 2013


# MARGULIS EXPANDERS
# Description: 
# Generates the H matrix from matrices A and B.
# H is an adjacency matrix constructed by adding edges between nodes in A and B
# on the following rules:
#   (x, y) of A is connected to the following nodes of B:
#     (x, y)
#     (x + 1, y)
#     (x, y + 1)
#     (x + y, y)
#     (-y, x)


import numpy

import helpers


NAME = '[MARGULIS]'


def GENERATE_MARGULIS_EXPANDERS(size, cross_Z, A_indices, n):
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

      # connect to (x + 1, y) in B
      j = cross_Z.index(((x + 1) % n, y)) + size

      H[i][j] += 1
      H[j][i] += 1

      # connect to (x, y + 1) in B
      j = cross_Z.index((x, (y + 1) % n)) + size

      H[i][j] += 1
      H[j][i] += 1

      # connect to (x + y, y) in B
      j = cross_Z.index(((x + y) % n, y)) + size

      H[i][j] += 1
      H[j][i] += 1

      # connect to (-y, x) in B
      j = cross_Z.index(((-y) % n, x)) + size

      H[i][j] += 1
      H[j][i] += 1

  print NAME + " Generated adjacency matrix H."

  helpers.write_H_matrix(H, NAME)

  print NAME + " Calculating eigenvalues of H ... "

  eigenvalues = helpers.generate_eigenvalues(H, NAME)

  if output_eigenvalues == True:
    helpers.write_eigenvalues(NAME, eigenvalues)

  print NAME + " Calculated eigenvalues of H."  

  helpers.write_result(NAME, n, eigenvalues[1])  

#  print NAME + " Second highest eigenvalue = " + str(eigenvalues[1])