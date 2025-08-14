# Sorting Algorithms

Exploring both comparison and non-comparison based sorting algorithms.

### Comparison-Based Sorts
Algorithms that sort by comparing elements to determine their relative order. These are bounded by O(n log n) time complexity in the worst case.

Examples: QuickSort, MergeSort, HeapSort

### Non-Comparison Based Sorts
Algorithms that sort without directly comparing elements. Instead, they use the structure or properties of the data (digits, value ranges, etc.). Can achieve O(n) time complexity for specific data types.

Examples: Radix Sort, Counting Sort, Bucket Sort

# Implemented Algorithms

## Radix Sort

Processes integers by sorting digit-by-digit, from least to most significant.

**Components:**
- `get_max_digits()`: Finds maximum number of digits in array
- `get_digit()`: Extracts digit at specific position
- `counting_sort_by_digit()`: **Stable sort** for single digit position
- `radix_sort()`: Main algorithm combining the above

find max number of digits --> iterate through least significant to most significant digit --> each time put num into bucket based on digit
--> flatten digit buckets --> repeat process

**Complexity:**
- Time: O(d × (n + k)) where d = digits, n = elements, k = radix
- Space: O(n + k)
- Stable: Yes

**Key Insights:**
- Number of buckets depends on radix choice:
 - Binary (radix-2): 2 buckets, more passes
 - Decimal (radix-10): 10 buckets, balanced
 - Byte (radix-256): 256 buckets, fewer passes
- Maintains stability by processing from least to most significant digit
- Breaks O(n log n) barrier for integers

## Bucket Sort

Distributes elements into buckets based on their value range, sorts each bucket, then concatenates results.

**Components:**
- `get_bucket_index()`: Maps value to appropriate bucket based on range
- `bucket_sort()`: Main algorithm that distributes, sorts, and concatenates

**Process:**
1. Find min/max to determine range
2. Create n empty buckets
3. Distribute elements into buckets based on value: `bucket_index = (value - min) / (max - min) * num_buckets` (normalized)
4. Sort individual buckets (using insertion sort for small buckets or Timsort for larger ones)
5. Concatenate buckets in order

**Complexity:**
- Time: 
  - Best/Average: O(n + k) when uniformly distributed
  - Worst: O(n²) when all elements in one bucket
- Space: O(n + k) where k = number of buckets
- Stable: Yes (if stable sort used for buckets)

**Choosing Number of Buckets:**
- **n buckets for n elements**: Most common, aims for ~1 element per bucket with uniform distribution
- **√n buckets**: Memory efficient, reduces overhead, better when bucket sorting is efficient
- **n/k buckets**: Target k elements per bucket (e.g., n/5 for ~5 elements per bucket)
- Trade-offs:
  - More buckets: Less sorting work per bucket, more memory/overhead
  - Fewer buckets: Less memory, but more elements to sort per bucket
  
**Key Insights:**
- Assumes uniform distribution for optimal performance
- Degrades to O(n log n) with poor distribution (all elements clustered)
- Choice of sorting algorithm for individual buckets matters:
  - Insertion sort: Better for small buckets (<10-20 elements)
  - Timsort: Better for larger buckets
- Can recursively apply bucket sort to large buckets
- Originally designed for [0,1) range but easily adapted to any range (by normalizing)

## TODO

- Handle negative numbers in Radix Sort
- Implement Bucket Sort
- Implement Counting Sort
- Implement comparison-based sorts (QuickSort, MergeSort)
- Add performance benchmarks
- Implement MSD Radix Sort