# HELPER METHODS for the generation of Expander Graphs

# Author:   Vlad Burca
# Date:     November 23, 2013
# Updated:  November 24, 2013

import yaml
import numpy
import subprocess
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
  A_elements = list()
  for row in A_indices:
    for element in row:
      A_element = (element / n, element % n)    # Re-generating the actual element pairs from the index of the cross product
      A_elements.append(A_element)
  A_elements_arr = numpy.array(A_elements, dtype=[('first', '<i4'), ('second', '<i4')])   # Transform list into a NumPy array for further transformations
  # global A 
  A = A_elements_arr.reshape((n, n))    # Reshape into two dimensional NumPy array

  B_elements = list()
  for row in B_indices:
    for element in row:
      B_element = (element / n, element % n)
      B_elements.append(B_element)
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

def write_H_params(size_H, k, EPSILON, NAME):
  outfile_params = open("params.aux", "w")

  outfile_params.write(str(NAME) + " " + str(size_H) + " " + str(k) + " " + str(EPSILON))
  outfile_params.close()


def write_H_matrix(H, NAME):
  print NAME + " Writing matrix H to file ... "

  outfile_H = open("matrix_H.aux", "w")

  for row in H:
    for element in row:
      outfile_H.write(str(element) + ' ')
    outfile_H.write("\n")
  outfile_H.close()

  print NAME + " Done writing to file."


def run_c_commands():
  # Compile C power method code
  print "Compiling the C Eigenvalue Computation ... "
  p = subprocess.Popen("gcc -o powermethod powermethod.c", shell=True)
  p.communicate()
  print "Running C Eigenvalue Computation ... "
  p = subprocess.Popen("./powermethod", shell=True)
  p.communicate()


def read_from_c_results():
  result_file = open("eigenvalue.aux", "r")
  eigenvalue = result_file.read()

  result_file.close()

  return float(eigenvalue)


def generate_eigenvalue(H, size_H, k, EPSILON, NAME):
  write_H_params(size_H, k, EPSILON, NAME)
  write_H_matrix(H, NAME)

  run_c_commands()

  return read_from_c_results()


def generate_eigenvalue_old(M, n, degree):
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
