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


## Trie (Prefix Tree)

Tree structure where each node represents a character, enabling fast prefix operations and word lookups.

**Components:**
- `TrieNode`: Contains children dict/array and end-of-word flag
- `insert(word)`: Add word by creating path of nodes
- `search(word)`: Traverse path and verify word exists
- `starts_with(prefix)`: Check if any word has given prefix

**Process:**
1. Start at root node
2. For each character, create child node if missing
3. Mark last node as end-of-word
4. Search traverses path, checking nodes exist
5. Prefix search just verifies path exists (ignores end-of-word)

**Complexity:**
- Insert: O(m) where m = word length
- Search: O(m)
- Space: O(total characters × alphabet size) worst case
- Better than hash table for prefix operations

**Key Insights:**
- Common prefixes share nodes (memory efficient for dictionaries)
- Can use array[26] for lowercase-only (faster) or dict for any char (flexible)
- Supports wildcards and regex patterns with modified search
- Foundation for autocomplete and spell checkers

**Use Cases:**
- Autocomplete/type-ahead
- Spell checkers
- IP routing tables (binary trie)
- Phone directories
- Word games (valid word checking)

### Extensions:
- **Autocomplete**: DFS from prefix node to collect all completions
- **Wildcard Search**: Backtracking for pattern matching

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

