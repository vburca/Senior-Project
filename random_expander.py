# Random Method for generating expander graphs

# Author:   Vlad Burca
# Date:     November 24, 2013
# Updated:  November 24, 2013


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


def GENERATE_RANDOM_EXPANDERS(K, size_H, EPSILON):
  NAME = '[RANDOM' + str(K) + ']'

  print NAME + " Generating H (adjacency list matrix) of size " + str(size_H) + " x " + str(K) + " ... "

  H = numpy.empty(shape=(size_H, K), dtype=numpy.int32)   # Generate H, empty adjacency list matrix

  second_half = numpy.arange(size_H / 2, size_H)

  for edge in range(K):

    perm_half = numpy.random.permutation(second_half)

    for i in range(size_H/2):
      H[i][edge]              = perm_half[i]
      H[perm_half[i]][edge]   = i

  print NAME + " Generated adjacency list matrix H."

  print NAME + " Calculating second highest eigenvalue of H ... "

  eigenvalue = helpers.generate_eigenvalue(H, size_H, K, EPSILON, NAME)

  print NAME + " Calculated second highest eigenvalue of H."

  helpers.write_result(NAME, size_H, K, eigenvalue) 
  helpers.cleanup(".aux")

