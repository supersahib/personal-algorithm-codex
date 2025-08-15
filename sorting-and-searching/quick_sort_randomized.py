import random
"""
"""

class QuickSortRandomized:
    def __init__(self):
        pass
    

    def sort(self, arr):
        self.quick_sort(arr, 0, len(arr)-1)
        return arr

    def quick_sort(self, arr, p, r):
        """
        Recursively sort array by partitioning around pivot.
        
        Args:
            arr: Array to sort
            p: Starting index (inclusive)
            r: Ending index (inclusive)
        """
        if p < r:
            q = self.partition_randomized(arr, p, r)
            self.quick_sort(arr, p, q-1)
            self.quick_sort(arr, q+1, r)
    
    def partition_randomized(self, arr, p, r):
        i = random.randint(p, r)
        arr[r], arr[i] = arr[i], arr[r]
        return self.partition(arr, p, r)


    def partition(self, arr, p , r):
        """
        Rearranges array so elements <= pivot 
        are on left, elements > pivot are on right.
        
        Invariant during scan:
        - arr[p..i] contains elements <= pivot
        - arr[i+1..j-1] contains elements > pivot
        - arr[j..r-1] not yet examined
        - arr[r] is pivot
        
        Args:
            arr: Array to partition
            p: Start index
            r: End index (pivot position)
        Returns:
            int: Final position of pivot
        """
        pivot = arr[r]
        i = p-1
        for j in range(p, r):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i+1
    
if __name__ == "__main__":
    test_cases = [
        # Basic test
        {
            "name": "Random array",
            "input": [3, 7, 1, 4, 6, 2, 5],
            "expected": [1, 2, 3, 4, 5, 6, 7]
        },
        # Edge cases
        {
            "name": "Single element",
            "input": [42],
            "expected": [42]
        },
        {
            "name": "Two elements",
            "input": [2, 1],
            "expected": [1, 2]
        },
        # Already sorted (worst case for fixed pivot)
        {
            "name": "Already sorted",
            "input": [1, 2, 3, 4, 5, 6, 7, 8],
            "expected": [1, 2, 3, 4, 5, 6, 7, 8]
        },
        # Reverse sorted (worst case for fixed pivot)
        {
            "name": "Reverse sorted",
            "input": [8, 7, 6, 5, 4, 3, 2, 1],
            "expected": [1, 2, 3, 4, 5, 6, 7, 8]
        },
        # Duplicates
        {
            "name": "Many duplicates",
            "input": [3, 5, 3, 5, 1, 3, 1, 5, 3],
            "expected": [1, 1, 3, 3, 3, 3, 5, 5, 5]
        },
        # All same
        {
            "name": "All identical",
            "input": [7, 7, 7, 7, 7],
            "expected": [7, 7, 7, 7, 7]
        },
        # Negatives
        {
            "name": "With negatives",
            "input": [-3, 5, -1, 0, 7, -2, 8, -1],
            "expected": [-3, -2, -1, -1, 0, 5, 7, 8]
        },
    ]
    
    sorter = QuickSortRandomized()
    
    print("Testing QuickSort Implementation:\n")
    for test in test_cases:
        arr = test["input"].copy()  # Preserve original for display
        result = sorter.sort(arr)
        passed = result == test["expected"]
        
        print(f"Test: {test['name']}")
        print(f"  Input:    {test['input']}")
        print(f"  Output:   {result}")
        print(f"  Expected: {test['expected']}")
        print(f"  {'✓ PASS' if passed else '✗ FAIL'}\n")