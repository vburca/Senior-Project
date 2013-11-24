# ALGORITHM METHODS for the generation of Expander Graphs

# Author:   Vlad Burca
# Date:     November 23, 2013
# Updated:  November 23, 2013


from angluin_expander import GENERATE_ANGLUIN_EXPANDERS
from margulis_expander import GENERATE_MARGULIS_EXPANDERS
from random_expander import GENERATE_RANDOM_EXPANDERS

# Explicit Methods
ANGLUIN_METHOD  = 'ANGLUIN'
MARGULIS_METHOD = 'MARGULIS'

# Random Methods
RANDOM_3        = 'RANDOM_3'
RANDOM_5        = 'RANDOM_5'


def EXPLICIT_METHOD(method_name, size, cross_Z, A_indices, n):
  if method_name == ANGLUIN_METHOD:
    GENERATE_ANGLUIN_EXPANDERS(size, cross_Z, A_indices, n)
  elif method_name == MARGULIS_METHOD:
    GENERATE_MARGULIS_EXPANDERS(size, cross_Z, A_indices, n)


def RANDOM_METHOD(method_name):
  if method_name == RANDOM_3:
    GENERATE_RANDOM_EXPANDERS(degree=3)
  elif method_name == RANDOM_5:
    GENERATE_RANDOM_EXPANDERS(degree=5)

