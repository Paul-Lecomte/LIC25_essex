// Bubble sort in C - Modified for the LIC25 End of Module Assignment
// - reads the data set to be sorted from CPUPI.txt (replaces the hard-coded array)
// - optional command-line argument limits the sort to the first N values so
//   that the O(n^2) bubble sort can be timed at different data sizes
// - times the sort with clock() and prints a short preview of the result
//   (instead of hundreds of thousands of numbers)

#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

// perform the bubble sort
void bubbleSort(long long array[], int size) {

  // loop to access each array element
  for (int step = 0; step < size - 1; ++step) {

    // loop to compare array elements
    for (int i = 0; i < size - step - 1; ++i) {

      // compare two adjacent elements
      // change > to < to sort in descending order
      if (array[i] > array[i + 1]) {

        // swapping occurs if elements
        // are not in the intended order
        long long temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
      }
    }
  }
}

// print the first and last values of the sorted region (short preview)
void printPreview(long long array[], int size) {
  int preview = size < 10 ? size : 10;
  printf("First %d values: ", preview);
  for (int i = 0; i < preview; ++i) {
    printf("%lld  ", array[i]);
  }
  printf("\nLast %d values:  ", preview);
  for (int i = size - preview; i < size; ++i) {
    printf("%lld  ", array[i]);
  }
  printf("\n");
}

// check that the values are in ascending order
int isSorted(long long array[], int size) {
  for (int i = 1; i < size; ++i) {
    if (array[i - 1] > array[i]) {
      return 0;
    }
  }
  return 1;
}

// Build the path to CPUPI.txt next to this source file, so the program can
// be run from any working directory. (When compiled with a relative source
// path, __FILE__ has no directory part and the current directory is used
// instead, so running from the part_a folder also works.)
void dataFilePath(char *out, size_t n) {
  char *slash;
  strncpy(out, __FILE__, n - 1);
  out[n - 1] = '\0';
  slash = strrchr(out, '\\');
  if (slash == NULL) {
    slash = strrchr(out, '/');
  }
  if (slash != NULL) {
    slash[1] = '\0';
  } else {
    out[0] = '\0';
  }
  if (strlen(out) + 9 < n) {
    strcat(out, "CPUPI.txt");
  }
}

int main(int argc, char *argv[]) {
  clock_t start, end;
  int sortCount;
  char dataPath[1024];

  // Open the data file for reading (kept next to this source file)
  dataFilePath(dataPath, sizeof dataPath);
  FILE *fp = fopen(dataPath, "r");
  if (fp == NULL) {
    perror(dataPath);
    return 1;
  }

  // First pass: count the numbers
  long long num;
  int count = 0;
  while (fscanf(fp, "%lld", &num) == 1) {
    count++;
  }

  // Allocate memory for the array
  long long *data = malloc(count * sizeof(long long));
  if (data == NULL) {
    perror("Error allocating memory");
    fclose(fp);
    return 1;
  }

  // Rewind and read the numbers into the array
  rewind(fp);
  int i = 0;
  while (fscanf(fp, "%lld", &data[i]) == 1) {
    i++;
  }

  fclose(fp);

  // Optional command-line argument: number of values to sort
  // (defaults to the full data set)
  sortCount = count;
  if (argc > 1) {
    sortCount = atoi(argv[1]);
    if (sortCount < 1 || sortCount > count) {
      sortCount = count;
    }
  }

  // Perform bubble sort and measure time
  start = clock();
  bubbleSort(data, sortCount);
  end = clock();

  printf("Values read from CPUPI.txt : %d\n", count);
  printf("Values sorted              : %d\n", sortCount);
  printf("Order                      : ascending\n");
  printPreview(data, sortCount);
  printf("Verification               : %s\n", isSorted(data, sortCount) ? "SORTED OK" : "NOT SORTED");
  double duration = ((double)end - start)/CLOCKS_PER_SEC;
  printf("Time taken to execute in seconds : %f\n", duration);

  // Free allocated memory
  free(data);
  return 0;
}