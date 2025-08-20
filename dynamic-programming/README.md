# Dynamic Programming

Solving optimization problems by breaking them into overlapping subproblems and building solutions bottom-up or top-down with memoization.

### Core Concepts
**Optimal Substructure**: Optimal solution contains optimal solutions to subproblems.
**Overlapping Subproblems**: Same subproblems appear multiple times.
**Memoization vs Tabulation**: Top-down recursive with cache vs bottom-up iterative with table.

### Pattern Categories

#### Linear DP
Single dimension problems where state depends on previous elements.
Examples: Kadane's Algorithm, House Robber, Longest Increasing Subsequence

#### Grid/2D DP
Two-dimensional problems often involving paths or string matching.
Examples: Edit Distance, Longest Common Subsequence, Unique Paths

#### Interval DP
Problems on ranges where we combine solutions of smaller intervals.
Examples: Matrix Chain Multiplication, Burst Balloons, Palindrome Partitioning

#### Knapsack Patterns
Resource allocation problems with constraints.
Examples: 0/1 Knapsack, Unbounded Knapsack, Coin Change

# Implemented Algorithms

## Kadane's Algorithm (Maximum Subarray)

Finds contiguous subarray with maximum sum in linear time using local optimization.

**Core Insight:**
At each position, decide whether to extend current subarray or start fresh:
1. **Extend current subarray if**: `subarray_sum + current > current`
2. **Start fresh if**: `subarray_sum + current < current`

**Components:**
- `max_ending_here`: Maximum sum ending at current position
- `max_so_far`: Global maximum found
- Decision: `max(nums[i], max_ending_here + nums[i])`

**Process:**
1. Initialize with first element
2. For each element, choose: extend or restart
3. Update global maximum if current sum is larger
4. Continue through array
5. Return global maximum

**Complexity:**
- Time: O(n) single pass
- Space: O(1) constant variables
- DP table version: O(n) space

**Key Insights:**
- Negative prefix never helps - discard it
- Every subarray must end somewhere - we find best at each position
- Can track indices with additional variables
- Basis for many subarray problems

**Variations:**
- **Maximum Product Subarray**: Track both max and min (negatives can flip)
- **Circular Array**: Max of regular Kadane and (total - min_subarray)
- **With One Deletion**: Track two states - with and without deletion

**Use Cases:**
- Maximum profit in stock trading
- Maximum sum in 2D matrix (apply to rows and columns)
- Image processing (brightest region)
- Time series analysis

**LeetCode Problems:**
- #53: Maximum Subarray
- #152: Maximum Product Subarray
- #918: Maximum Sum Circular Subarray
- #1186: Maximum Subarray Sum with One Deletion

## TODO

### Linear DP
- [ ] **Fibonacci Sequence**: Classic introduction to DP optimization
- [ ] **House Robber**: Decision at each step with constraint
- [ ] **Climbing Stairs**: Count paths with fixed steps
- [ ] **Longest Increasing Subsequence**: O(n log n) with patience sorting
- [ ] **Best Time to Buy/Sell Stock**: Multiple transaction variants

### Grid/2D DP
- [ ] **Edit Distance (Levenshtein)**: Minimum operations between strings
- [ ] **Longest Common Subsequence**: Classic string comparison
- [ ] **Unique Paths**: Count paths in grid with obstacles
- [ ] **Minimum Path Sum**: Optimal path through weighted grid
- [ ] **Dungeon Game**: Path planning with constraints

### Knapsack Patterns
- [ ] **0/1 Knapsack**: Each item used at most once
- [ ] **Unbounded Knapsack**: Unlimited copies of each item
- [ ] **Coin Change**: Minimum coins for target sum
- [ ] **Partition Equal Subset**: Split array into equal sums
- [ ] **Target Sum**: Ways to assign +/- to reach target

### Interval DP
- [ ] **Matrix Chain Multiplication**: Optimal parenthesization
- [ ] **Burst Balloons**: Maximize coins with dependencies
- [ ] **Palindrome Partitioning**: Minimum cuts for palindromes
- [ ] **Minimum Cost Tree From Leaf Values**: Build tree optimally

### String DP
- [ ] **Word Break**: Segment string using dictionary
- [ ] **Decode Ways**: Count decodings of numeric string
- [ ] **Distinct Subsequences**: Count occurrences as subsequence
- [ ] **Interleaving String**: Check if s3 is interleaving of s1, s2

### Advanced Patterns
- [ ] **Bitmask DP**: Subset problems with state compression
- [ ] **Digit DP**: Count numbers with properties
- [ ] **DP on Trees**: Optimization on tree structures
- [ ] **Probability DP**: Expected value problems
- [ ] **Game Theory DP**: Optimal play in games

### Optimization Techniques
- [ ] **Space Optimization**: Rolling arrays, state reduction
- [ ] **Monotonic Queue Optimization**: Sliding window maximum
- [ ] **Convex Hull Trick**: Optimize linear functions
- [ ] **Divide and Conquer Optimization**: Special recurrence forms