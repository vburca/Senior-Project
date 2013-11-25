# HELPER METHODS for the generation of Expander Graphs

# Author:   Vlad Burca
# Date:     November 23, 2013
# Updated:  November 24, 2013

import yaml
import numpy
from numpy import linalg

import matrix_helper


def cleanup(extension):
  import os

  print "Removing all the " + extension + " files from the current directory"
  
  filelist = [ f for f in os.listdir(".") if f.endswith(extension) ]
  for f in filelist:
    os.remove(f)

  print "Cleaned up all the output files (*" + extension + ")"


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


def write_H_matrix(H, name):
  outfile_H = open(name.strip('[]') + "_matrix_H.out", "w")

  for row in H:
    for element in row:
      outfile_H.write(str(element) + ' ')
    outfile_H.write("\n")
  outfile_H.close()


def generate_eigenvalue(M, n, degree):
  EPSILON = 0.001
  return matrix_helper.powermethod(M, n, EPSILON, degree)


# def generate_eigenvalues(H, name):
#   eigenvalues = linalg.eigvals(H)
#   eigenvalues = numpy.sort(eigenvalues)[::-1]

#   return eigenvalues


# def write_eigenvalues(name, eigenvalues):
#   outfile_eigen = open(name.strip('[]') + "_eigenvalues.out", "w")

#   outfile_eigen.write(str(eigenvalues))
#   outfile_eigen.close()


def write_result(name, n, eigenvalue):
  import os

  name = name.strip('[]').lower()

  # Open file with initial results (if existent)
  if os.path.exists(name + ".results"):
    result_file = open(name + ".results", "r")
    results = yaml.safe_load(result_file)
    result_file.close()
  else:   # file does not exist / no previous results
    results = { name: {} }

  # If files are empty
  if not 'dict' in str(type(results)):
    results = { name: {} }

  # Update the new results
  results[name][n] = float(eigenvalue)

  # Open file to write new yaml dictionary
  result_file = open(name + ".results", "w")
  result_file.write(yaml.dump(results, default_flow_style=False))    # update results yaml dictionary
  result_file.close()
