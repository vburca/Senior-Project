# Description: 
# Generates the initial matrices, A and B. The elements of A and B are from
# the cross product Z(n) x Z(n), n integer.
# We first generate the Z(n) set and then, using the indices of the elements
# of that set, we randomly assign them to position in A and B.

# Runs the algorithms set in the config.yaml file

# Author:   Vlad Burca
# Date:     November 13, 2013
# Updated:  November 24, 2013

import yaml
import numpy 
from numpy import linalg

import helpers
import algorithms
import methods


# MAIN

def generate_expanders():
  # Read n from configuration file
  config_file = open("config.yaml", "r")
  config_vars = yaml.safe_load(config_file)
  config_file.close()


  # Clean existing .out files
  if config_vars['params']['cleanup'] == True:
    helpers.cleanup(".out")


  n       = config_vars['params']['n']
  EPSILON = config_vars['params']['epsilon']

  # Generate Z(n)
  #Z_n = list(xrange(n))


  size = n * n

  # Generate matrices A and B only if the algorithms that require them are
  # configured to run
  if  helpers.check_configured_run(methods.ANGLUIN, methods.MARGULIS):
    print "Generating matrices A and B with n = " + str(n) + " ... "

    # Generate the elements of  A and B using indices from the cross product
    indices_of_pairs = numpy.arange(size)   # Generate array of indices of the cross product

    A_indices = numpy.random.permutation(indices_of_pairs).reshape((n, n)) # Randomize in matrix positions
    B_indices = numpy.random.permutation(indices_of_pairs).reshape((n, n)) # Randomize in matrix positions

    if config_vars['params']['output_indices_matrices'] == True:
      helpers.write_indices_matrices(A_indices, B_indices)

    if config_vars['params']['output_initializer_matrices'] == True:
      returned_matrices = helpers.generate_pair_matrices(A_indices, B_indices, n)
      A = returned_matrices[0]
      B = returned_matrices[1]

      helpers.write_pair_matrices(A, B)

    print "Generated matrices A and B."


  # EXPLICIT ALGORITHMS
  if config_vars['algorithms'][methods.ANGLUIN] == True:
    print ''
    algorithms.EXPLICIT_METHOD(method_name=methods.ANGLUIN, 
                               size=size, 
                               A_indices=A_indices, 
                               n=n, 
                               EPSILON=EPSILON)

  if config_vars['algorithms'][methods.MARGULIS] == True:
    print ''
    algorithms.EXPLICIT_METHOD(method_name=methods.MARGULIS, 
                               size=size, 
                               A_indices=A_indices, 
                               n=n, 
                               EPSILON=EPSILON)

  if config_vars['algorithms'][methods.AJTAI] == True:
    print ''
    c = config_vars['params']['c']
    s = c * numpy.log(n)
    algorithms.EXPLICIT_METHOD(method_name=methods.AJTAI, 
                               size=2 * size, 
                               EPSILON=EPSILON, 
                               s=s)

  # RANDOM ALGORITHMS
  if config_vars['algorithms'][methods.RANDOM_3] == True:
    print ''
    samples = config_vars['params']['random_graphs_samples']
    algorithms.RANDOM_METHOD(methods.RANDOM_3, 2 * size, EPSILON, samples)

  if config_vars['algorithms'][methods.RANDOM_5] == True:
    print ''
    samples = config_vars['params']['random_graphs_samples']
    algorithms.RANDOM_METHOD(methods.RANDOM_5, 2 * size, EPSILON, samples)


print '\n'

# DEBUGGING CODE

# generate_expanders()