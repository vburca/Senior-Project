# ALGORITHM METHODS for the generation of Expander Graphs

# Author:   Vlad Burca
# Date:     November 23, 2013
# Updated:  November 24, 2013


from angluin_expander import GENERATE_ANGLUIN_EXPANDERS
from margulis_expander import GENERATE_MARGULIS_EXPANDERS
from random_expander import GENERATE_RANDOM_EXPANDERS

import methods


def EXPLICIT_METHOD(method_name, size, A_indices, n, EPSILON):
  if method_name == methods.ANGLUIN:
    print "Running ANGLUIN METHOD"
    #GENERATE_ANGLUIN_EXPANDERS(size, A_indices, n, EPSILON)
  elif method_name == methods.MARGULIS:
    print "Running MARGULIS METHOD"
    #GENERATE_MARGULIS_EXPANDERS(size, A_indices, n, EPSILON)


def RANDOM_METHOD(method_name, size_H, EPSILON, samples):
  if method_name == methods.RANDOM_3:
    print "Running RANDOM 3 METHOD"
    #GENERATE_RANDOM_EXPANDERS(K=3, size_H=size_H, EPSILON=EPSILON, samples=samples)
  elif method_name == methods.RANDOM_5:
    print "Running RANDOM 5 METHOD"
    #GENERATE_RANDOM_EXPANDERS(K=5, size_H=size_H, EPSILON=EPSILON, samples=samples)

