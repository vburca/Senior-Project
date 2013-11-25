# ALGORITHM METHODS for the generation of Expander Graphs

# Author:   Vlad Burca
# Date:     November 23, 2013
# Updated:  November 24, 2013


from angluin_expander import GENERATE_ANGLUIN_EXPANDERS
from margulis_expander import GENERATE_MARGULIS_EXPANDERS
from random_expander import GENERATE_RANDOM_EXPANDERS

# Explicit Methods
ANGLUIN_METHOD  = 'ANGLUIN'
MARGULIS_METHOD = 'MARGULIS'

# Random Methods
RANDOM_3        = 'RANDOM_3'
RANDOM_5        = 'RANDOM_5'


def EXPLICIT_METHOD(method_name, size, A_indices, n, EPSILON):
  if method_name == ANGLUIN_METHOD:
    GENERATE_ANGLUIN_EXPANDERS(size, A_indices, n, EPSILON)
  elif method_name == MARGULIS_METHOD:
    GENERATE_MARGULIS_EXPANDERS(size, A_indices, n, EPSILON)


def RANDOM_METHOD(method_name, output_adjacency):
  if method_name == RANDOM_3:
    GENERATE_RANDOM_EXPANDERS(degree=3, EPSILON=EPSILON)
  elif method_name == RANDOM_5:
    GENERATE_RANDOM_EXPANDERS(degree=5, EPSILON=EPSILON)

