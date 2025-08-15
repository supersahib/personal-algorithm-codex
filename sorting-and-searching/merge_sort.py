"""
Algorithm: Merge Sort
Time Complexity: O(n log n) - all cases (best, average, worst)
Space Complexity: O(n) - for temporary arrays during merge
Category: Comparison-based, Divide-and-Conquer, Stable Sort

Description:
    MergeSort divides the array recursively into halves until single elements
    remain, then merges them back in sorted order. The key insight is that 
    merging two sorted arrays can be done in O(n) time. The algorithm:
    
    1. Divide: Split array into two halves
    2. Conquer: Recursively sort both halves
    3. Combine: Merge the sorted halves
    
    The sentinel optimization (using ∞) simplifies the merge by eliminating
    boundary checks. Stability is maintained by always taking from the left
    array when elements are equal (left[i] <= right[j]).

LeetCode Problems:
    - Problem #148: Sort List (merge sort on linked list)
    - Problem #315: Count of Smaller Numbers After Self (merge sort + count)
    - Problem #493: Reverse Pairs (merge sort modification)
    - Problem #327: Count of Range Sum (merge sort application)
    - Problem #23: Merge k Sorted Lists (uses merge concept)
    - Problem #88: Merge Sorted Array (the merge operation itself)
    - Problem #912: Sort an Array (classic sorting problem)
"""

class MergeSort:
    def __init__(self):
        pass
    
    def sort(self, arr):
        self.merge_sort(arr, 0, len(arr)-1)
        return arr

    def merge(self, arr, p, q, r):
        """Merge two sorted subarrays using sentinel approach"""

        left = arr[p:q+1]
        right = arr[q+1:r+1]

        #sentinel cards to help with comparison
        left.append(float('inf'))
        right.append(float('inf'))

        i, j = 0,0
        for k in range(p, r+1):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

    def merge_sort(self, arr, p, r):
        """
        Divide array in half recursively, merge sorted halves.
        
        The recursion depth is always log n, giving us the log n factor in complexity.
        """
        if p < r:
            q = (p + r) // 2
            self.merge_sort(arr, p, q)
            self.merge_sort(arr, q+1, r)
            self.merge(arr, p, q ,r)

# Test cases
if __name__ == "__main__":
    sorter = MergeSort()
    
    test_cases = [
        # Basic cases
        {"name": "Simple array", 
         "input": [3, 1, 4, 1, 5, 9, 2, 6],
         "expected": [1, 1, 2, 3, 4, 5, 6, 9]},
        
        # Edge cases
        {"name": "Empty array",
         "input": [],
         "expected": []},
        
        {"name": "Single element",
         "input": [42],
         "expected": [42]},
        
        {"name": "Two elements",
         "input": [2, 1],
         "expected": [1, 2]},
        
        # Stability test (preserves order of equal elements)
        {"name": "Duplicates (stability check)",
         "input": [3, 1, 4, 1, 5, 1, 2],
         "expected": [1, 1, 1, 2, 3, 4, 5]},
        
        # Already sorted
        {"name": "Already sorted",
         "input": [1, 2, 3, 4, 5],
         "expected": [1, 2, 3, 4, 5]},
        
        # Reverse sorted
        {"name": "Reverse sorted",
         "input": [5, 4, 3, 2, 1],
         "expected": [1, 2, 3, 4, 5]},
        
        # All same elements
        {"name": "All identical",
         "input": [7, 7, 7, 7, 7],
         "expected": [7, 7, 7, 7, 7]},
        
        # Negative numbers
        {"name": "With negatives",
         "input": [-3, 5, -1, 7, 0, -2, 8],
         "expected": [-3, -2, -1, 0, 5, 7, 8]},
        
        # Floating point
        {"name": "Floating point",
         "input": [3.14, 2.71, 1.41, 2.23, 1.73],
         "expected": [1.41, 1.73, 2.23, 2.71, 3.14]},
    ]
    
    print("Testing MergeSort Implementation:\n")
    for test in test_cases:
        arr = test["input"].copy()  # Preserve original
        result = sorter.sort(arr)
        passed = result == test["expected"]
        
        print(f"Test: {test['name']}")
        print(f"  Input:    {test['input']}")
        print(f"  Output:   {result}")
        print(f"  Expected: {test['expected']}")
        print(f"  ✓ PASS" if passed else f"  ✗ FAIL")
        print()