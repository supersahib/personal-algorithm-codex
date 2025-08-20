"""
Algorithm: Kadane's Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
Category: Dynamic Programming (Linear DP)

Description:
    Finds the maximum sum of any contiguous subarray
    Core insight: At each element, decide whether to:
    - Continue the previous subarray (add current element)
    - Start fresh from current element

Use Cases:
    - Maximum profit from stock prices
    - Maximum sum in circular arrays (variant)
    - Maximum product subarray (variant)
    - Image processing (maximum intensity region)

LeetCode Problems:
    - #53: Maximum Subarray
    - #152: Maximum Product Subarray
    - #918: Maximum Sum Circular Subarray
"""

class MaximumSubarray:
    def naive_approach(self, nums):
        """
        Brute force: Check all possible subarrays
        Time: O(n²) with optimized sum calculation
        """
        if not nums:
            return 0
        
        max_sum = float('-inf')
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)
        return max_sum
    
    def kadane_basic(self, nums):
        """
        Classic Kadane's Algorithm
        Time: O(n), Space: O(1)
        
        At each position i, we track:
        - max_ending_here: max sum of subarray ending at i
        - max_so_far: global maximum found

        1) extend the current subarray if:
            - subbaray + current > current
        2) start fresh with new subarray if:
            - subarray + current < current
        """
        if not nums:
            return 0
        
        max_ending_here = nums[0]
        max_so_far = nums[0]
        
        for i in range(1, len(nums)):
            # Key decision - extend or start fresh?
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_so_far, max_ending_here)        
        return max_so_far
    
    def kadane_with_indices(self, nums):
        """
        Return both max sum AND the subarray indices
        Useful for "find the actual subarray" problems
        """
        if not nums:
            return 0, -1, -1
        
        max_ending_here = nums[0]
        max_so_far = nums[0]
        
        # Track indices
        start = 0
        end = 0
        temp_start = 0
        
        for i in range(1, len(nums)):
            if nums[i] > max_ending_here + nums[i]:
                max_ending_here = nums[i]
                temp_start = i
            else:
                max_ending_here = max_ending_here + nums[i]
            
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                start = temp_start
                end = i
        return max_so_far, start, end
    
    def kadane_dp_table(self, nums):
        """
        DP table approach - same logic, more explicit
        dp[i] = max sum of subarray ending at index i
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])

        return max(dp)


# Test cases
if __name__ == "__main__":
    solver = MaximumSubarray()
    
    test_cases = [
        # Basic case
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),  # [4,-1,2,1]
        
        # All negative
        ([-5, -2, -8, -1, -4], -1),  # [-1]
        
        # All positive  
        ([1, 2, 3, 4, 5], 15),  # entire array
        
        # Single element
        ([5], 5),
        ([-3], -3),
        
        # Mixed
        ([5, -3, 5], 7),  # [5, -3, 5]
    ]
    
    for nums, expected in test_cases:
        result = solver.kadane_basic(nums)
        print(f"Array: {nums}")
        print(f"Expected: {expected}, Got: {result}")
        print()