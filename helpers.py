# HELPER METHODS for the generation of Expander Graphs

# Author:   Vlad Burca
# Date:     November 23, 2013
# Updated:  November 23, 2013

import numpy
from numpy import linalg


def generate_pair_matrices(cross_Z, A_indices, B_indices, n):
  A_elements = list(cross_Z[element] for row in A_indices for element in row)     # Getting the actual element pairs from the index of the cross product
  A_elements_arr = numpy.array(A_elements, dtype=[('first', '<i4'), ('second', '<i4')])   # Transform list into a NumPy array for further transformations
  # global A 
  A = A_elements_arr.reshape((n, n))    # Reshape into two dimensional NumPy array

  B_elements = list(cross_Z[element] for row in B_indices for element in row)
  B_elements_arr = numpy.array(B_elements, dtype=[('first', '<i4'), ('second', '<i4')])
  # global B 
  B = B_elements_arr.reshape((n, n))
  return [A, B]


def write_indices_matrices(A_indices, B_indices):
  outfile_A = open("indices_matrix_A.out", "w")
  outfile_B = open("indices_matrix_B.out", "w")

  for row in A_indices:
    for element in row:
      outfile_A.write(str(element) + ' ')
    outfile_A.write("\n")
  outfile_A.close()

  for row in B_indices:
    for element in row:
      outfile_B.write(str(element) + ' ')
    outfile_B.write("\n")
  outfile_B.close()


def write_pair_matrices(A, B):
  outfile_A = open("matrix_A.out", "w")
  outfile_B = open("matrix_B.out", "w")

  for row in A:
    for element in row:
      outfile_A.write(str(element) + ' ')
    outfile_A.write("\n")
  outfile_A.close()

  for row in B:
    for element in row:
      outfile_B.write(str(element) + ' ')
    outfile_B.write("\n")
  outfile_B.close()


def write_H_matrix(H):
  outfile_H = open("matrix_H.out", "w")

  for row in H:
    for element in row:
      outfile_H.write(str(element) + ' ')
    outfile_H.write("\n")
  outfile_H.close()


def generate_and_write_eigenvalues(H):
  eigenvalues = linalg.eigvals(H)
  eigenvalues = numpy.sort(eigenvalues)[::-1]

  outfile_eigen = open("eigen_H.out", "w")

  outfile_eigen.write(str(eigenvalues))
  outfile_eigen.close()

  return eigenvalues