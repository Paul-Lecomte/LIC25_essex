# Bubble sort in Python - Modified for the LIC25 End of Module Assignment
# - reads the data set to be sorted from CPUPI.txt (replaces the hard-coded list)
# - keeps the original bubble sort (O(n^2)) for comparison purposes
# - uses Python's built-in sort (Timsort, O(n log n)) as the efficient algorithm
# - times every sort with time.perf_counter()
# - writes the full sorted data set to sorted_data_full.txt
# - paths are resolved relative to this script, so it runs from any working directory

import time
from pathlib import Path

# Files live next to this script (part_a/)
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "CPUPI.txt"
OUTPUT_FILE = BASE_DIR / "sorted_data_full.txt"

def bubbleSort(array):
    """Original bubble sort implementation - O(n^2)"""
    n = len(array)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def efficientSort(array):
    """Efficient sorting using Python's built-in Timsort - O(n log n)"""
    array.sort()

def main():
    # Read the data from CPUPI.txt (next to this script)
    try:
        with open(DATA_FILE, "r") as f:
            # Read all content and split by whitespace
            data_str = f.read().split()
            # Convert each string to integer
            data = [int(num) for num in data_str]
    except FileNotFoundError:
        print("Error: CPUPI.txt not found.")
        return
    except ValueError as e:
        print(f"Error converting data to integers: {e}")
        return

    print("Dataset size: {} numbers".format(len(data)))
    print()

    # 1. Compare bubble sort with the efficient sort on sizes that are
    #    practical for the O(n^2) bubble sort (100,000+ values would take
    #    hours in Python, so larger sizes are covered by extrapolation
    #    in the evaluation report)
    bubble_sizes = [1000, 5000, 10000, 20000]
    for size in bubble_sizes:
        if size > len(data):
            continue
        subset = data[:size]
        subset_copy = subset.copy()

        # Time bubble sort
        start = time.perf_counter()
        bubbleSort(subset)
        bubble_time = time.perf_counter() - start

        # Time efficient sort
        start = time.perf_counter()
        efficientSort(subset_copy)
        efficient_time = time.perf_counter() - start

        print("Size {:>6}: Bubble Sort = {:.6f}s, Timsort = {:.6f}s".format(
            size, bubble_time, efficient_time))

    # 2. Time the efficient sort (Timsort) on every data size required
    #    by the assignment
    print()
    for size in [100000, 200000, 500000, len(data)]:
        if size > len(data):
            continue
        subset = data[:size].copy()
        start = time.perf_counter()
        efficientSort(subset)
        elapsed = time.perf_counter() - start
        label = " (full dataset)" if size == len(data) else ""
        print("Size {:>6}: Timsort = {:.6f}s{}".format(size, elapsed, label))

    # 3. Sort the full data set and write the submission output file
    full_data = data.copy()
    start = time.perf_counter()
    efficientSort(full_data)
    total_time = time.perf_counter() - start

    print()
    print("Full data set sorted in {:.6f}s".format(total_time))
    print("First 10 sorted values:", full_data[:10])
    print("Last 10 sorted values: ", full_data[-10:])
    print("Verified ascending:", full_data == sorted(full_data))

    try:
        with open(OUTPUT_FILE, "w") as f:
            for num in full_data:
                f.write(str(num) + "\n")
    except IOError as e:
        print(f"Error writing to file: {e}")
        return

    print("Sorted data written to", OUTPUT_FILE.name)
    print()
    print("Note: bubble sort grows quadratically (O(n^2)); for 100,000+")
    print("values it becomes impractical in Python, which is why the")
    print("efficient O(n log n) Timsort is used for the full data set.")

if __name__ == "__main__":
    main()