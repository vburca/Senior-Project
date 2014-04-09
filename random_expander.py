# Random Method for generating expander graphs

# Author:   Vlad Burca
# Date:     November 24, 2013
# Updated:  November 25, 2013


# Description:
# The algorithm is based on Kevin Chang's unpublished thesis (Princeton).
# The method involves a set of n nodes that are divided into half. The
# second half is randomly permuted and then the nodes of the first half
# are paired (connected to, through an edge) to the nodes of the permuted half,
# in order. This process is being done k (DEGREE) times, so that the resulting
# graph will be a k-regular bipartite graph - bipartite due to the division
# of the initial set of n nodes.
# Chang's conjectured that for a big enough n, these Random Expanders are 
# going to be Ramanujan.

import numpy

import helpers


NAME = ''


def generate_expander(K, size_H):
  H = numpy.empty(shape=(size_H, K), dtype=numpy.int32)   # Generate H, empty adjacency list matrix
  H[:] = -1     # Initialize it with all elements -1

  second_half = numpy.arange(size_H / 2, size_H)

  for edge in range(K):

    perm_half = numpy.random.permutation(second_half)

    for i in range(size_H/2):
      H[i][edge]              = perm_half[i]
      H[perm_half[i]][edge]   = i

  return H


def GENERATE_RANDOM_EXPANDERS(K, size_H, EPSILON, samples):

  NAME = '[RANDOM' + str(K) + ']'

  print NAME + " Generating " + str(samples) + " H (adjacency list matrices) of size " + str(size_H) + " x " + str(K) + " ... "
  print "\n"

  eigenvalue = 0

  for sampling in range(samples):
    print NAME + " ##  " + str(sampling) + "  //  " + str(samples) + "  ## "

    H = generate_expander(K, size_H)
    eigenvalue_aux = helpers.generate_eigenvalue(H, size_H, K, EPSILON, NAME)

    eigenvalue += eigenvalue_aux

  eigenvalue = eigenvalue / samples

  print NAME + " Calculated average of second highest eigenvalue for " + str(samples) + " matrices H."

  helpers.write_result(NAME, size_H, K, eigenvalue) 
  helpers.cleanup(".aux")

