# Description
# Power method for calculating second largest eigenvalue of a sparse matrix.
# The motivation for this is to replace the current algorithm that I use in my
# expander graph generating algorithms for calculating eigenvalues - the current
# algorithm is too slow for the purpose of the project. Also, it does not take 
# advantage of the sparse matrices that the expander generating algorithm creates.

# Disclaimer: This is a Python implementation of the power method described in 
# Kevin Chang's unpublished thesis (Princeton) - his implementation is done in C.

# Author:   Vlad Burca
# Date:     November 24, 2013
# Updated:  November 24, 2013

import random
import math


def powermethod(MATRIX, n, epsilon, k):

  guess1 = 1
  guess2 = 10
  eigenvector1 = [0] * n 
  eigenvector2 = [0] * n
  vector3 = []

  for i in range(n):
    eigenvector1[i] = random.random()

  while (guess1 - guess2) <= -epsilon or (guess1 - guess2) >= epsilon:

    # print (guess1 - guess2)

    c = 0
    d = 0
    normconst = 0
    test = 0

    c = sum(eigenvector1)
    vector3 = [0] * n
    c = c / n

    d = sum(eigenvector1[:n/2])
    d -= sum(eigenvector1[n/2:])

    d = d / n

    for i in range(n/2):
      eigenvector2[i] = eigenvector1[i] - c - d

    for i in range(n/2, n):
      eigenvector2[i] = eigenvector1[i] - c + d

    for i in range(n):
      normconst += eigenvector2[i]**2

    normconst = math.sqrt(normconst)

    for i in range(n):
      eigenvector2[i] = eigenvector2[i] / normconst

    for i in range(n):
      for j in range(k):
        vector3[i] += eigenvector2[int(MATRIX[i][j])]

    eigenvector1 = [0] * n

    for i in range(n):
      for j in range(k):
        eigenvector1[i] += vector3[int(MATRIX[i][j])]

    guess2 = guess1
    guess1 = 0

    for i in range(n):
      guess1 += eigenvector2[i] * eigenvector1[i]

    guess1 = math.sqrt(guess1)

  return guess1


# DEBUGGING CODE

# A = [ [ 4, 4, 6 ],
#       [ 4, 5, 7 ],
#       [ 6, 6, 7 ], 
#       [ 5, 5, 7 ],
#       [ 0, 0, 1 ],
#       [ 1, 3, 3 ],
#       [ 0, 2, 2 ],
#       [ 1, 2, 3 ] ]

# n = 2
# degree = 3
# n_sq = n * n
# size = 2 * n_sq

# print powermethod(A, size, 0.00001, degree)

