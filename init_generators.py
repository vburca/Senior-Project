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

import helpers
import algorithms

# Constant names for the Explicit Methods
ANGLUIN_METHOD  = 'ANGLUIN'
MARGULIS_METHOD = 'MARGULIS'


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

helpers.write_indices_matrices(A_indices, B_indices)

if config_vars['init_generators']['generate_pair_matrices'] == True:
  returned_matrices = helpers.generate_pair_matrices(cross_Z, A_indices, B_indices, n)
  A = returned_matrices[0]
  B = returned_matrices[1]

  if config_vars['init_generators']['write_matrices_to_file'] == True:
    helpers.write_pair_matrices(A, B)

print "Generated matrices A and B."


algorithms.EXPLICIT_METHOD(ANGLUIN_METHOD, size, cross_Z, A_indices, n)
algorithms.EXPLICIT_METHOD(MARGULIS_METHOD, size, cross_Z, A_indices, n)

#GENERATE_RANDOM_EXPANDERS(degree=3)
#GENERATE_RANDOM_EXPANDERS(degree=5)

