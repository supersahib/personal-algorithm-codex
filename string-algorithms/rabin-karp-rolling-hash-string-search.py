"""
Algorithm: Rabin-Karp String Matching
Time Complexity: O(n+m) average, O(nm) worst case
Space Complexity: O(1) excluding output
Category: String Algorithms

Description:
    Find all occurrences of pattern in text using rolling polynomial hash.  
    
    Key insight: Instead of rehashing the entire window O(m), we can update 
    the hash in O(1) by removing the leftmost character's contribution and 
    adding the new rightmost character.

    https://www.youtube.com/watch?v=BfUejqd07yo
    this video does great job explaining

    Let's say text is "abcdefghijk" and pattern is "bcde"

    we compute polynomial hash of abcd as
    h(abcd) = h(a,b,c,d) = (hash(a)*10^3 + hash(b)*10^2 + hash(c)*10^1 + hash(d)*10^0) mod 133 (some prime number)

    now we shift to bcde
    h(bcde) = (h(abcd) - hash(a)*10^3) * 10 + hash(e)*10^0

LeetCode Problems:
    - Problem #28: Find Index of First Occurrence
    - Problem #187: Repeated DNA Sequences
    - Problem #1044: Longest Duplicate Substring
"""

class RabinKarp:
    def __init__(self, base=256, prime=101):
        self.base = base
        self.prime = prime

    def search(self, text, pattern):
        """
        Find all occurrences of pattern in text using Rabin-Karp
        Args:
            text: string to search in
            pattern: string to search for
        Returns:
        list of starting indices where pattern occurs

        Time: O(?)
        Space: O(?)
        """
        if not pattern or len(pattern) > len(text):
            return []
        
        base = 256 # radix of our polynomial hash function (ie base our our number system. we have 256 unique digits/symbols)
        prime = 101 
        m, n = len(text), len(pattern)
        result = []

        pattern_hash, window_hash = 0,0
        # compute initial hashes
        for i in range(n):
          pattern_hash = (pattern_hash * base + ord(pattern[i])) % prime
          window_hash = (window_hash * base + ord(text[i])) % prime
        
        #precompute h = base^(m-1) % prime --> we do this to reuse each window. 
        # this is basically multiplier for left most character 
        h = 1 
        for i in range(n-1):
            h = (h * base) % prime

        #sliding window
        for i in range(m - n + 1):
          
          # Check if hashes match
          if window_hash == pattern_hash:
              # Verify actual string match because we can get collisions
              if text[i:i+n] == pattern:
                  result.append(i)
          
          #rolling hash
          if i < m - n:
              #remove leftmost
              window_hash  = (window_hash - ord(text[i]) * h) % prime
              window_hash = (window_hash * base + ord(text[i+n])) % prime

              # Handle negative values from modulo
              if window_hash < 0:
                  window_hash += prime
        return result

if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Basic cases
        {
            "input": ("ABABCABABA", "ABA"),
            "expected": [0, 2, 6, 8],
            "description": "Multiple overlapping matches"
        },
        {
            "input": ("AAAA", "AA"),
            "expected": [0, 1, 2],
            "description": "Overlapping pattern in repetitive text"
        },
        
        # Edge cases
        {
            "input": ("A", "A"),
            "expected": [0],
            "description": "Single character match"
        },
        {
            "input": ("ABCDEFG", "XYZ"),
            "expected": [],
            "description": "Pattern not found"
        },
        {
            "input": ("", "A"),
            "expected": [],
            "description": "Empty text"
        },
        {
            "input": ("ABC", ""),
            "expected": [],
            "description": "Empty pattern"
        },
        {
            "input": ("HELLO", "HELLO"),
            "expected": [0],
            "description": "Pattern equals entire text"
        },
        
        # Tricky cases
        {
            "input": ("AABAACAADAABAABA", "AABA"),
            "expected": [0, 9, 12],
            "description": "Pattern with repeated characters"
        },
        {
            "input": ("ABABABAB", "ABAB"),
            "expected": [0, 2, 4],
            "description": "Overlapping matches"
        },
        {
            "input": ("BBBBBBBBBBB", "BBB"),
            "expected": [0, 1, 2, 3, 4, 5, 6, 7, 8],
            "description": "All same character"
        },
        
        # Real-world like cases
        {
            "input": ("The quick brown fox jumps over the lazy dog", "the"),
            "expected": [31],  # Only the second "the" (lowercase)
            "description": "Case-sensitive search"
        },
        {
            "input": ("ababcabcabababd", "ababd"),
            "expected": [10],
            "description": "Pattern at end"
        },
        {
            "input": ("abcabcabcabc", "abcabcabc"),
            "expected": [0, 3],
            "description": "Overlapping complex pattern"
        },
        
        # Stress cases
        {
            "input": ("a" * 1000 + "b", "a" * 10 + "b"),
            "expected": [990],
            "description": "Long repetitive text"
        },
        {
            "input": ("GCATCGCAGAGAGTATACAGTACG", "GCAGAGAG"),
            "expected": [5],
            "description": "DNA sequence matching"
        }
    ]
    algo = RabinKarp()  # Or however you structure your class
    
    print("Running Rabin-Karp tests...")
    for i, test in enumerate(test_cases):
        text, pattern = test["input"]
        result = algo.search(text, pattern)  # or algo.solve()
        
        try:
            assert result == test["expected"], (
                f"Failed: {test['description']}\n"
                f"Input: text='{text[:20]}...', pattern='{pattern}'\n"
                f"Expected: {test['expected']}\n"
                f"Got: {result}"
            )
            print(f"✓ Test {i+1} passed: {test['description']}")
        except AssertionError as e:
            print(f"✗ Test {i+1} failed: {e}")
            
    print("\nAll tests completed!")