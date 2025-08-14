# String Algorithms

Exploring pattern matching, string processing, and text manipulation algorithms.

### Pattern Matching
Algorithms that find occurrences of patterns within text. Range from naive O(nm) to sophisticated linear-time approaches using preprocessing.

Examples: Rabin-Karp, KMP, Boyer-Moore, Z-Algorithm

### String Processing
Algorithms for analyzing, transforming, and extracting information from strings.

Examples: Suffix Arrays, Tries, String Hashing, Longest Common Substring

# Implemented Algorithms

## Rabin-Karp
https://www.youtube.com/watch?v=BfUejqd07yo

Uses rolling polynomial hash to find pattern occurrences in text efficiently.

**Components:**
- Initial hash computation for pattern and first window
- `h = base^(m-1) % prime`: Precomputed multiplier for leftmost character
- Rolling hash update: Remove leftmost, shift, add rightmost
- String verification on hash matches (handle collisions)

**Process:**
1. Compute pattern hash and initial window hash
2. Slide window through text
3. On hash match → verify actual string match
4. Roll hash: `new_hash = (old_hash - left_char * h) * base + right_char`
5. Continue sliding until end of text

**Complexity:**
- Time: O(n+m) average, O(nm) worst case (many collisions)
- Space: O(1) excluding output
- Multiple pattern search: O(k(n+m)) for k patterns

**Key Insights:**
- Base (radix) should be ≥ alphabet size (256 for ASCII)
- Prime modulus reduces hash collisions
- Rolling hash enables O(1) window updates vs O(m) rehashing
- String verification needed due to hash collisions
- Worst case occurs with repetitive text (e.g., "aaa...a")

**Use Cases:**
- Plagiarism detection
- DNA sequence matching
- Finding repeated substrings
- Multiple pattern search (simpler than Aho-Corasick)

## TODO

### Pattern Matching
- [ ] **KMP**: Failure function for O(n+m) guaranteed
- [ ] **Boyer-Moore**: Skip characters using bad character/good suffix
- [ ] **Z-Algorithm**: Linear time pattern matching
- [ ] **Aho-Corasick**: Multiple patterns simultaneously

### String Processing  
- [ ] **Trie**: Prefix tree for fast lookups
- [ ] **Suffix Array**: Sorted suffixes for substring queries
- [ ] **Manacher's**: Find palindromes in O(n)
- [ ] **Rolling Hash Applications**: Longest duplicate substring

### Advanced
- [ ] **Suffix Tree**: O(n) construction, powerful queries
- [ ] **Burrows-Wheeler Transform**: Compression preprocessing
- [ ] **Rope Data Structure**: Efficient string concatenation