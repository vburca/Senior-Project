# Description: 
# Generates the initial matrices, A and B. The elements of A and B are from
# the cross product Z(n) x Z(n), n integer.
# We first generate the Z(n) set and then, using the indices of the elements
# of that set, we randomly assign them to position in A and B.

# Author:   Vlad Burca
# Date:     November 13, 2013
# Updated:  November 13, 2013

import yaml
import numpy 


def generate_pair_matrices():
  A_elements = list(cross_Z[element] for row in A_indices for element in row)     # Getting the actual element pairs from the index of the cross product
  A_elements_arr = numpy.array(A_elements, dtype=[('first', '<i4'), ('second', '<i4')])   # Transform list into a NumPy array for further transformations
  global A 
  A = A_elements_arr.reshape((n, n))    # Reshape into two dimensional NumPy array

  B_elements = list(cross_Z[element] for row in B_indices for element in row)
  B_elements_arr = numpy.array(B_elements, dtype=[('first', '<i4'), ('second', '<i4')])
  global B 
  B = B_elements_arr.reshape((n, n))


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


# MAIN

# Read n from configuration file
config_file = open("config.yaml", "r")
config_vars = yaml.safe_load(config_file)

n = config_vars['init_generators']['n']

print "Starting generation of matrices A and B with n = " + str(n) + " ... "

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

if config_vars['init_generators']['generate_pair_matrices'] == True:
  generate_pair_matrices()

  if config_vars['init_generators']['write_matrices_to_file'] == True:
    write_pair_matrices()

print "Matrices A and B are generated."


  