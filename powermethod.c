/* 
  Description
  Power method for calculating second largest eigenvalue of a sparse matrix.
  The motivation for this is to replace the current algorithm that I use in my
  expander graph generating algorithms for calculating eigenvalues - the current
  algorithm is too slow for the purpose of the project. Also, it does not take 
  advantage of the sparse matrices that the expander generating algorithm creates.

  Disclaimer (Rights of ownership): This implementation is a slight variation of the one 
  presented in Kevin Chang's unpublished thesis (Princeton).

  Author:   Vlad Burca
  Date:     November 24, 2013
  Updated:  November 24, 2013
*/


#include <math.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>


float powermethod(int** M, int n, float epsilon, int k) {

  float guess1 = 1;
  float guess2 = 10;

  float *eigenvector1 = (float*)calloc(n, sizeof(float));
  float *eigenvector2 = (float*)calloc(n, sizeof(float));
  float *vector3      = (float*)calloc(n, sizeof(float));

  int i, j;

  for (i = 0; i < n; i++)
    eigenvector1[i] = (float)rand() / RAND_MAX;

  while ( guess1 - guess2 <= -epsilon || guess1 - guess2 >= epsilon ) {

    float c = 0;
    float d = 0;
    float normconst = 0;

    for (i = 0; i < n; i++) {
      c += eigenvector1[i];
      vector3[i] = 0;
    }
    c = c / n;

    for (i = 0; i < n/2; i++)
      d += eigenvector1[i];
    for (i = n/2; i < n; i++)
      d -= eigenvector1[i];
    d = d / n;

    for (i = 0; i < n/2; i++)
      eigenvector2[i] = eigenvector1[i] - c - d;
    for (i = n/2; i < n; i++)
      eigenvector2[i] = eigenvector1[i] - c + d;

    for (i = 0; i < n; i++)
      normconst += eigenvector2[i] * eigenvector2[i];
    normconst = sqrt(normconst);

    for (i = 0; i < n; i++)
      eigenvector2[i] = eigenvector2[i] / normconst;

    for (i = 0; i < n; i++)
      for (j = 0; j < k; j++)
        vector3[i] += eigenvector2[(int)M[i][j]];

    for (i = 0; i < n; i++)
      eigenvector1[i] = 0;
    for (i = 0; i < n; i++)
      for (j = 0; j < k; j++)
        eigenvector1[i] += vector3[(int)M[i][j]];

    guess2 = guess1;
    guess1 = 0;

    for (i = 0; i < n; i++)
      guess1 += eigenvector2[i] * eigenvector1[i];

    guess1 = sqrt(guess1);
  }

  free(eigenvector1);
  free(eigenvector2);
  free(vector3);

  return guess1;
}


int main() {

  printf(" >>> Initializing Eigenvalue Computation <<< \n");

  FILE *params_file;
  params_file = fopen("params.aux", "r");
  int n, k;
  char name[20];
  float epsilon;
  fscanf(params_file, "%s %d %d %f", name, &n, &k, &epsilon);
  fclose(params_file);

  printf(" >>> %s Initializing matrix of dimensions (%d x %d) <<< \n", name, n, k);

  int** matrix;
  matrix = (int**)calloc(n, sizeof(int*));
  
  int i, j;

  for (i = 0; i < n; i++)
    matrix[i] = (int*)calloc(k, sizeof(int));

  FILE *matrix_file;
  matrix_file = fopen("matrix_H.aux", "r");

  int element_index;

  printf(" >>> %s Reading matrix from file ... <<< \n", name);

  for (i = 0; i < n; i++)
    for (j = 0; j < k; j++) {
      fscanf(matrix_file, "%d ", &element_index);
      matrix[i][j] = element_index;
    }

  fclose(matrix_file);

  // for (i = 0; i < n; i++) {
  //   printf ("\n");
  //   for (j = 0; j < k; j++)
  //     printf("%d ", matrix[i][j]);
  // }

  float eigenvalue;

  printf(" >>> %s Computing the eigenvalue for the matrix ... <<< \n", name);

  eigenvalue = powermethod(matrix, n, epsilon, k);

  printf(" >>> %s Computation done. Writing result to file ... \n", name);

  FILE *result_file;
  result_file = fopen("eigenvalue.aux", "w");

  fprintf(result_file, "%f", eigenvalue);

  fclose(result_file);

  printf(" >>> %s Result written to file. Eigenvalue computation is done. <<< \n", name);

  return 0;
}

