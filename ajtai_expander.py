# M Ajtai's algorithm for generating expander graphs

# Author:   Vlad Burca
# Date:     April 3, 2014
# Updated:  April 9, 2014


# AJTAI EXPANDERS
# Description: 



import numpy

import helpers


NAME = ''


def generate_random_graph(K, size_H):
  H = numpy.empty(shape=(size_H, K), dtype=numpy.int32)   # Generate H, empty adjacency list matrix

  return H


def GENERATE_AJTAI_EXPANDERS(K, size_H, EPSILON, s):

  print "[" + str(size_H) + "]: " + "s= " + str(s) + "\t EPSILON= " + str(EPSILON)

