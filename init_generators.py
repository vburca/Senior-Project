# Description: 
# Generates the initial matrices, A and B. The elements of A and B are from
# the cross product Z(n) x Z(n), n integer.
# We first generate the Z(n) set and then, using the indices of the elements
# of that set, we randomly assign them to position in A and B.

# Author:   Vlad Burca
# Date:     November 13, 2013
# Updated:  November 20, 2013

import yaml
import numpy 
from numpy import linalg


def generate_pair_matrices():
  A_elements = list(cross_Z[element] for row in A_indices for element in row)     # Getting the actual element pairs from the index of the cross product
  A_elements_arr = numpy.array(A_elements, dtype=[('first', '<i4'), ('second', '<i4')])   # Transform list into a NumPy array for further transformations
  global A 
  A = A_elements_arr.reshape((n, n))    # Reshape into two dimensional NumPy array

  B_elements = list(cross_Z[element] for row in B_indices for element in row)
  B_elements_arr = numpy.array(B_elements, dtype=[('first', '<i4'), ('second', '<i4')])
  global B 
  B = B_elements_arr.reshape((n, n))


def write_indices_matrices():
  outfile_A = open("indices_matrix_A.out", "w")
  outfile_B = open("indices_matrix_B.out", "w")

  for row in A_indices:
    for element in row:
      outfile_A.write(str(element) + ' ')
    outfile_A.write("\n")
  outfile_A.close()

  for row in B_indices:
    for element in row:
      outfile_B.write(str(element) + ' ')
    outfile_B.write("\n")
  outfile_B.close()


def write_pair_matrices():
  outfile_A = open("matrix_A.out", "w")
  outfile_B = open("matrix_B.out", "w")

  for row in A:
    for element in row:
      outfile_A.write(str(element) + ' ')
    outfile_A.write("\n")
  outfile_A.close()

  for row in B:
    for element in row:
      outfile_B.write(str(element) + ' ')
    outfile_B.write("\n")
  outfile_B.close()


def write_H_matrix():
  outfile_H = open("matrix_H.out", "w")

  for row in H:
    for element in row:
      outfile_H.write(str(element) + ' ')
    outfile_H.write("\n")
  outfile_H.close()


def generate_and_write_eigenvalues():
  global eigen_values
  eigen_values = linalg.eigvals(H)
  eigen_values = numpy.sort(eigen_values)

  outfile_eigen = open("eigen_H.out", "w")

  outfile_eigen.write(eigen_values)
  outfile_eigen.close()



# MAIN

# Read n from configuration file
config_file = open("config.yaml", "r")
config_vars = yaml.safe_load(config_file)

n = config_vars['init_generators']['n']

print "Generating matrices A and B with n = " + str(n) + " ... "

# Generate Z(n)
Z_n = list(xrange(n))


# Generate cross product Z(n) x Z(n)
cross_Z = list((Zi, Zj) for Zi in Z_n for Zj in Z_n)
cross_Z_arr = numpy.array(cross_Z)    # Generating NumPy Array of the cross product


# Generate the elements of  A and B using indices from the cross product
size = n * n

indices_of_cross_Z = numpy.arange(size)   # Generate array of indices of the cross product

A_indices = numpy.random.permutation(indices_of_cross_Z).reshape((n, n)) # Randomize in matrix positions
B_indices = numpy.random.permutation(indices_of_cross_Z).reshape((n, n)) # Randomize in matrix positions

write_indices_matrices()

if config_vars['init_generators']['generate_pair_matrices'] == True:
  generate_pair_matrices()

  if config_vars['init_generators']['write_matrices_to_file'] == True:
    write_pair_matrices()

print "Generated matrices A and B."



# Description: 
# Generates the H matrix from matrices A and B.
# H is an adjacency matrix constructed by adding edges between nodes in A and B
# on the following rules:
#   (x, y) of A is connected to the following nodes of B:
#     (x, y)
#     (x + y, y)
#     (y + 1, -x)

size_H = 2 * size

print "Generating H of size " + str(size_H) + " x " + str(size_H) + " ... "

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

print "Generated adjacency matrix H."

write_H_matrix()

print "Calculating eigenvalues of H ... "

generate_and_write_eigenvalues()

print "Calculated eigenvalues of H."  

print "Second highest eigenvalue = " + str(eigen_values[1])

