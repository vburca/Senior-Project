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

def GENERATE_RANDOM_EXPANDERS(degree, output_adjacency):
  print "Empty"