# Part A Evaluation Report: Comparing C and Python Sorting Implementations

## 1. Introduction

This report evaluates the tutor-provided C (`bubsort2.c`) and Python (`bubsort.py`) sorting programs after modification: both now read the `CPUPI.txt` data set, and the Python program additionally uses a more efficient sorting algorithm. It documents the modifications, justifies the algorithm choice with Big-O analysis, presents measured timings for the required data sizes, answers the assignment questions, and discusses the professional, legal and ethical issues involved.

## 2. The Data Set and the Original Programs

`CPUPI.txt` holds the digits of Pi to about one million decimal places - an effectively random digit distribution - grouped into sets of ten, giving **838,861 integer values** of up to ten digits each (groups beginning with zeros read as shorter integers, because leading zeros are dropped when tokens are parsed as numbers). The task is to sort these values into ascending order.

The original C program bubble-sorted a hard-coded array of eleven integers and printed it; the original Python program did the same for a small hard-coded list. Neither read any external data.

## 3. Modifications Made

### 3.1 C Program (`bubsort2.c`)

The bubble sort function itself was left **unchanged**, as required; only the data acquisition and output mechanisms were modified:

1. Opens and validates `CPUPI.txt`.
2. A first `fscanf` pass counts the numbers (the file spans 92,275 lines, so a fixed-size array is not possible).
3. Allocates exactly that much memory with `malloc`.
4. Rewinds the file and reads the values into the array.
5. Changes the array type from `int` to `long long` (ten-digit values exceed 32-bit range, max ~2.1 x 10^9); specifiers updated to `%lld`.
6. Times the sort with `clock()`.
7. An optional command-line argument limits the sort to the first *N* values, so the O(n^2) sort can be timed at each required size; without it, the full set is sorted.
8. Prints only a preview (first/last ten values) plus an automatic ascending-order verification, instead of all 838,861 values.
9. Frees the memory before exit.

### 3.2 Python Program (`bubsort.py`)

1. Reads all of `CPUPI.txt`, converting each whitespace-separated token to an `int`; handles a missing file and non-numeric data.
2. Keeps the original bubble sort for comparison, but sorts the data set with Python's built-in `list.sort()` (**Timsort**).
3. Times everything with `time.perf_counter()`.
4. Prints the first and last ten sorted values, verifies the result is ascending, and writes all 838,861 sorted values to `sorted_data_full.txt` - the submitted sorted data file.

## 4. Algorithm Selection and Justification

Bubble sort repeatedly steps through the list, comparing adjacent elements and swapping them when they are out of order. The tutor-provided implementation has no early-exit flag, so it always performs *n(n-1)/2* comparisons - O(n^2) (Cormen et al., 2022). For *n* = 838,861 that is approximately 3.52 x 10^11 comparisons, which explains the rapidly growing measured runtimes (Knuth, 1998). Bubble sort was retained in the C program because the assignment requires the original algorithm to be preserved there; it is the Python program whose algorithm had to be replaced.

The Python algorithm was replaced with **Timsort**, the implementation behind `list.sort()` and `sorted()` (Peters, 2002). Timsort is a hybrid, stable, adaptive algorithm derived from merge sort and insertion sort: it finds naturally ordered "runs", extends short ones with binary insertion sort, and merges them in a balanced way. Its worst and average cases are O(n log n), its best case O(n) on already-ordered data, and it needs O(n) auxiliary space. For *n* = 838,861 an O(n log n) sort performs roughly 838,861 x log2(838,861) ≈ 1.65 x 10^7 comparison operations - about four orders of magnitude fewer than bubble sort - and that difference dominates every other factor, including the raw speed of the underlying language.

Alternatives considered: insertion and selection sort (still O(n^2)); merge sort (O(n log n), but non-trivial to implement correctly in interpreted Python); quicksort (O(n^2) worst case without a robust pivot policy, and unstable); and counting/radix approaches (linear time is theoretically possible for bounded ten-digit keys, but the code complexity is unjustified against a one-line library sort). `list.sort()` was chosen because it is a well-tested, highly optimised component maintained by the Python Software Foundation (2026); reusing proven library code rather than reimplementing it is the standard professional choice.

## 5. Experimental Method

All measurements were taken on one Windows 11 (64-bit) machine. The C program was compiled with Microsoft Visual Studio 2022 (MSVC `cl.exe` v14.44, x64, `/O2`) via the Visual C++ build-tools environment (Microsoft, 2026); Python 3.12.10 (CPython) served for the Python measurements. Both timers surround the sort call only - file reading and console output are excluded - using `clock()` in C and the monotonic high-resolution `time.perf_counter()` in Python (Python Software Foundation, 2026).

The sizes are exactly those required by the assignment - 100,000; 200,000; 500,000; 800,000 - taken as the first *N* values so every series sorts identical input. The efficient Python sort was additionally timed on all 838,861 values, and the C program was also run once on the complete set. Each figure is a single timed run; a few per cent of jitter should be expected.

Because bubble sort is O(n^2), measuring the Python bubble sort at the largest sizes was impractical (one 800,000-value run would take the better part of a day). It was measured at 1,000-20,000 values and extrapolated from the observed quadratic relationship; every extrapolated figure is prefixed "~" and labelled as such, and no estimate is presented as a measurement.

Threats to validity: runs were not repeated and averaged, and background processes can affect results. The C runtime grew x8.8 from 100,000 to 200,000 values rather than the x4 predicted by pure quadratic growth - consistent with the 1.6 MB array outgrowing the inner loop's CPU cache and with reduced sustained turbo clocks - after which growth returned close to quadratic (x6.9 vs x6.25 predicted; x2.6 vs x2.56 predicted).

## 6. Results

The main results table below shows measured values unless "~" marks an extrapolation.

| Data size | C bubble sort time | Python bubble sort time | Python sort time (Timsort) |
| ---------: | :------------------: | :----------------------: | :--------------------------: |
| 100,000 | 4.115 s (measured) | ~477 s (~8 min, extrapolated) | 0.0174 s (measured) |
| 200,000 | 36.211 s (measured) | ~1,910 s (~32 min, extrapolated) | 0.0393 s (measured) |
| 500,000 | 249.627 s (measured) | ~11,940 s (~3.3 h, extrapolated) | 0.1231 s (measured) |
| 800,000 | 645.251 s (measured) | ~30,600 s (~8.5 h, extrapolated) | ~0.23 s |
| 838,861 (full set) | 711.551 s (measured) | ~33,600 s (~9.3 h, extrapolated) | 0.2394 s (measured) |

Measured Python bubble sort timings confirm the quadratic trend: 1,000 values in 0.0298 s; 5,000 in 0.8057 s; 10,000 in 3.907 s; 20,000 in 19.096 s - x5 in data gives x27 in time, and x2 gives x4.9, both consistent with O(n^2). Timsort grew only from 0.000099 s to 0.0026 s over the same sizes (x26 for x20 data), consistent with O(n log n).

Three observations follow. First, compiled C bubble sort is roughly 116x faster than Python bubble sort on identical data (4.115 s vs ~477 s at 100,000 values) - the pure language effect. Second, Timsort in Python is roughly 237x faster than compiled C bubble sort at 100,000 values - the algorithm effect, which dwarfs the language effect. Third, the gap widens with size: at the full 838,861 values Timsort needed 0.2394 s against 711.6 s for the C bubble sort - about 3,000x longer.

One further observation concerns measurement practice itself: the non-quadratic jump between the two smallest C sizes shows why single-run desktop timings must be interpreted with care, and why complexity classes - not isolated seconds - are the reliable basis for extrapolation across orders of magnitude.

### 6.1 Answering the Assignment Questions

**Were you able to sort the data in Python faster than the compiled bubble sort in C?** Yes - at every data size, by large margins: 0.0174 s against 4.115 s at 100,000 values (about 237x), and 0.2394 s against 711.551 s on the full set (about 2,970x). The result holds for all the data sizes listed.

**Did it work for all the data sizes listed?** Yes. The Python program sorted 100,000; 200,000; 500,000 and all 838,861 values without error, verified the result, and wrote the sorted values to `sorted_data_full.txt`. The C program likewise sorted every size it was run at (100,000 through 800,000 and the full set), reporting "SORTED OK" each time; only its runtime becomes impractical.

## 7. Discussion: Comparing the Two Languages

### 7.1 The algorithm effect dominates the language effect

The measurements separate the two effects cleanly. Holding the algorithm constant (bubble sort in both), compiled C beats interpreted Python by roughly 116x at 100,000 values - the pure language effect (native machine code versus bytecode interpretation). Holding the language constant (Python), replacing bubble sort with Timsort improves performance by roughly 26,000x at the same size (~477 s vs 0.0174 s) - the pure algorithm effect. Because the algorithm effect is more than two hundred times larger than the language effect, the interpreted Python program with the good algorithm defeats the compiled C program with the poor one by two to three orders of magnitude at every size here - as asymptotic analysis predicts: compilers multiply the constant factor, while the growth curve decides the outcome as n grows.

### 7.2 What each language made easy

The C version required careful engineering: dynamic memory allocation sized from a first file pass, a matched `free`, format specifiers consistent with `long long`, and a configured compiler toolchain before anything could run; compiler warnings (such as MSVC's C4996 deprecation warnings for `fscanf`) had to be assessed rather than blindly ignored. The payoff is direct control - a native executable running the same algorithm about 116x faster than Python. The Python version needed far less code: reading the file takes three lines and sorting is one method call, optimised by the Python core developers (Peters, 2002). The trade-offs are interpreter overhead for anything not delegated to C-coded built-ins and no manual memory management; the built-in sort also adapts to partially ordered input, which the fixed bubble sort never can.

These are development-model differences, not merely syntax differences. C follows a compile-link-run model: types are fixed ahead of time and whole classes of errors surface before the program runs, at the cost of a slower edit-test cycle. Python's edit-run model, with dynamic typing and no separate compile step, shortens development at the cost of finding some errors only at run time. For business applications, Python's model typically reduces development and maintenance effort, while C's model typically delivers more predictable shipped performance.

### 7.3 Practical guidance arising

Choose the algorithm first, then the language that best fits the project. Where an efficient library sort exists - as in Python, in C (`qsort`, C++ `std::sort`) and virtually every modern standard library - hand-written quadratic sorts have no place in production data processing. Bubble sort remains valuable for teaching and trivially small inputs. For this data set the whole task completes in well under a second with the right algorithm; the real bottleneck is human decision-making, not computation.

### 7.4 Lessons for software development

Four lessons carry over to professional practice. First, algorithm selection matters most: before optimising language-level details, confirm that the fundamental algorithm suits the problem scale. Second, leverage standard libraries: well-tested, optimised library functions outperform hand-written equivalents and cut development time - Python's sort replaced roughly twenty lines of bubble sort with a single method call. Third, consider data characteristics: properties such as partial ordering are exploited by adaptive algorithms like Timsort but are invisible to a fixed bubble sort. Fourth, measure rather than assume: the true magnitudes found here - 237x and 2,970x - would have been easy to underestimate with back-of-envelope reasoning alone.

## 8. Professional, Legal and Ethical Considerations

**Professional competence and tool selection.** A computing professional is expected to know and critically select the standard methodologies, tools and libraries of the trade (Bentley and McIlroy, 1993). Hand-writing a quadratic sort when a maintained O(n log n) implementation sits in the standard library is a competence failure as much as a performance one; the duty is to justify tool choices with evidence and to measure rather than assume.

**Honest reporting and reproducibility.** Performance claims must be evidenced and reproducible - hence the exact compiler version, flags, interpreter version and timing functions stated in Section 5, and the clear separation of measured from extrapolated values. Presenting estimates as measurements, or mixing figures from different program versions, would breach research integrity; inconsistent draft figures previously held in this project were replaced by a single measured data set for that reason.

**Referencing and academic integrity.** Timsort was designed by Tim Peters and documented in PEP 229 (Peters, 2002), and the analytical framework comes from standard textbooks (Cormen et al., 2022; Knuth, 1998); failing to credit such sources would be plagiarism. Harvard referencing is used throughout, and any generative-AI assistance in drafting must be disclosed and clearly marked rather than submitted as unaided work.

**Professional codes of conduct.** Bodies such as BCS, the Chartered Institute for IT, publish codes of conduct requiring practitioners to act in the public interest, maintain their competence, and be honest about the limitations of their work (BCS, 2022). The behaviours exercised in this exercise - citing sources, documenting methods, reporting measurements honestly, and considering the wider impact of inefficient systems - are direct applications of that code rather than academic formalities.

**Intellectual property and licensing.** Python is distributed by the Python Software Foundation under a permissive open-source licence; the MSVC Community toolchain is licensed by Microsoft for individual and small-team use; the textbooks cited are copyrighted works. Professionals must respect these regimes when choosing and reusing tools and code.

**Data protection.** `CPUPI.txt` contains only Pi digits - no personal data - but the same file-reading code pointed at customer records would engage the UK GDPR and the Data Protection Act 2018 (Information Commissioner's Office, 2024). One fidelity issue is worth noting: parsing the ten-digit groups as integers silently drops leading zeros, so the output is numerically correct but not a byte-for-byte transformation of the input; handling real records would require preserving such formatting.

**Environmental responsibility.** An O(n^2) algorithm where O(n log n) is available wastes computation at scale: bubble sort performs roughly 2,000x more comparison work than Timsort on this data set. At data-centre scale, avoidable inefficiency is an ethical as well as an economic cost; refusing to ship it is part of responsible engineering.

**Professional reflection.** The exercise mirrors real legacy-code maintenance: changes were minimal, documented in the source, and built-in verification checks that output is genuinely sorted. Building correctness into code rather than trusting it is a habit worth keeping.

## 9. Conclusion

Both tutor-provided programs were successfully modified to read the 838,861-value data set from `CPUPI.txt`; the Python program was additionally upgraded to Timsort. The submitted sorted data file contains all 838,861 values in ascending order, verified programmatically.

Measured on this machine, the compiled C bubble sort needed 4.115 s, 36.211 s, 249.627 s, 645.251 s and 711.551 s for 100,000; 200,000; 500,000; 800,000 and all 838,861 values, while Python's Timsort sorted those sizes in 0.0174 s to 0.2394 s. Python therefore sorted the data faster than the compiled C bubble sort at every size - by about 237x at 100,000 values and about 2,970x on the full set - because O(n log n) beats O(n^2) by orders of magnitude at these scales. With the algorithm held constant, compiled C retains an approximately 116x advantage over interpreted Python. The lesson: algorithm selection first, language and tooling second, and measurement - never assumption - as the final arbiter.

Practical recommendations from this exercise are: audit legacy code for algorithmic inefficiency before optimising anything else; default to standard-library sorting unless profiling proves otherwise; and record measurement conditions whenever performance claims will be reported.

## 10. References (Harvard Referencing Style)

1. Bentley, J.L. and McIlroy, M.D. (1993) 'Engineering a sort function', *Software - Practice and Experience*, 23(11), pp.1249-1265. DOI: 10.1002/spe.4380231105.

2. Cormen, T.H., Leiserson, C.E., Rivest, R.L. and Stein, C. (2022) *Introduction to Algorithms*. 4th ed. Cambridge, Massachusetts: MIT Press.

3. Information Commissioner's Office (2024) *UK GDPR and data protection*. Available at: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/ (Accessed: 13 October 2026).

4. Kernighan, B.W. and Ritchie, D.M. (1988) *The C Programming Language*. 2nd ed. Englewood Cliffs, New Jersey: Prentice Hall.

5. Knuth, D.E. (1998) *The Art of Computer Programming, Volume 3: Sorting and Searching*. 2nd ed. Reading, Massachusetts: Addison-Wesley.

6. Microsoft (2026) *Build C and C++ projects on the command line (MSVC)*. Available at: https://learn.microsoft.com/en-us/cpp/build/building-on-the-command-line (Accessed: 13 October 2026).

7. Peters, T. (2002) *PEP 229: Sorting Python*. Available at: https://peps.python.org/pep-0229/ (Accessed: 13 October 2026).

8. Python Software Foundation (2026) *Built-in Types - list.sort()*. Available at: https://docs.python.org/3/library/stdtypes.html#list.sort (Accessed: 13 October 2026).

9. Python Software Foundation (2026) *time - Time access and conversions*. Available at: https://docs.python.org/3/library/time.html (Accessed: 13 October 2026).

10. BCS, The Chartered Institute for IT (2022) *BCS Code of Conduct*. Available at: https://www.bcs.org/standards-and-professions/code-of-conduct/ (Accessed: 13 October 2026).
