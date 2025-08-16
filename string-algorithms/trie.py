"""
Algorithm: Trie (Prefix Tree)
Time Complexity:
    - Insert: O(m) where m = length of word
    - Search: O(m)
    - StartsWith: O(m)
    - Space: O(ALPHABET_SIZE x N x M) worst case
Category: Tree Data Structures / String Algorithms

Description:
    Tree-like data structure for efficient string prefix operations.
    Each node represents a character, paths represent words.
    Common prefixes share nodes, enabling fast prefix queries.

Use Cases:
    - Autocomplete systems
    - Spell checkers
    - IP routing tables
    - Phone directory search
    - Word games (Boggle, Scrabble)
    - Prefix matching in databases

LeetCode Problems:
    - Problem #208: Implement Trie
    - Problem #211: Design Add and Search Words
    - Problem #212: Word Search II
    - Problem #648: Replace Words
    - Problem #677: Map Sum Pairs
    - Problem #1032: Stream of Characters
"""

class TrieNode:
    def __init__(self):
        self.children = {} 
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        self.insert_helper(self.root, word, 0)

    def insert_helper(self, node, word, i):
        if i == len(word):
            node.is_end_of_word = True
            return

        if word[i] not in node.children:
            node.children[word[i]] = TrieNode()
        self.insert_helper(node.children[word[i]], word, i+1)

    def search(self, word):
        return self.search_helper(self.root, word, 0)
    
    def search_helper(self, node, word, i):
        if i == len(word):
            return node.is_end_of_word
        if word[i] not in node.children:
            return False

        return self.search_helper(node.children[word[i]], word, i+1)
    
    def starts_with(self, prefix):
        return self.starts_with_helper(self.root, prefix, 0)
    
    def starts_with_helper(self, node, prefix, i):
        if i == len(prefix):
            return True
        if prefix[i] not in node.children:
            return False

        return self.starts_with_helper(node.children[prefix[i]], prefix, i+1)

class TrieNode:
    def __init__(self):
        self.children = {} 
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        self.insert_helper(self.root, word, 0)

    def insert_helper(self, node, word, i):
        if i == len(word):
            node.is_end_of_word = True
            return

        if word[i] not in node.children:
            node.children[word[i]] = TrieNode()
        self.insert_helper(node.children[word[i]], word, i+1)

    def search(self, word):
        return self.search_helper(self.root, word, 0)
    
    def search_helper(self, node, word, i):
        if i == len(word):  # Fixed: check this first
            return node.is_end_of_word
            
        if word[i] not in node.children:
            return False
        
        return self.search_helper(node.children[word[i]], word, i+1)
    
    def starts_with(self, prefix):
        return self.starts_with_helper(self.root, prefix, 0)
    
    def starts_with_helper(self, node, prefix, i):
        if i == len(prefix):
            return True
        if prefix[i] not in node.children:
            return False

        return self.starts_with_helper(node.children[prefix[i]], prefix, i+1)


# Test cases
if __name__ == "__main__":
    # Test 1: Basic operations
    print("Test 1: Basic insert and search")
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.starts_with("app") == True
    print("✓ Passed")
    
    # Test 2: Overlapping words
    print("\nTest 2: Overlapping words")
    trie = Trie()
    trie.insert("app")
    trie.insert("apple")
    assert trie.search("app") == True
    assert trie.search("apple") == True
    assert trie.search("appl") == False
    assert trie.starts_with("appl") == True
    print("✓ Passed")
    
    # Test 3: No common prefix
    print("\nTest 3: Words with no common prefix")
    trie = Trie()
    trie.insert("cat")
    trie.insert("dog")
    assert trie.search("cat") == True
    assert trie.search("dog") == True
    assert trie.search("ca") == False
    assert trie.starts_with("ca") == True
    assert trie.starts_with("do") == True
    assert trie.starts_with("bat") == False
    print("✓ Passed")
    
    # Test 4: Empty string
    print("\nTest 4: Empty string")
    trie = Trie()
    trie.insert("")
    assert trie.search("") == True
    assert trie.starts_with("") == True
    print("✓ Passed")
    
    # Test 5: Single character
    print("\nTest 5: Single characters")
    trie = Trie()
    trie.insert("a")
    trie.insert("b")
    assert trie.search("a") == True
    assert trie.search("b") == True
    assert trie.search("c") == False
    assert trie.starts_with("a") == True
    print("✓ Passed")
    
    # Test 6: Case sensitivity
    print("\nTest 6: Case sensitivity")
    trie = Trie()
    trie.insert("Apple")
    trie.insert("apple")
    assert trie.search("Apple") == True
    assert trie.search("apple") == True
    assert trie.search("APPLE") == False
    print("✓ Passed")
    
    # Test 7: Common interview scenario
    print("\nTest 7: Dictionary of words")
    trie = Trie()
    words = ["the", "a", "there", "answer", "any", "by", "bye", "their"]
    for word in words:
        trie.insert(word)
    
    assert trie.search("the") == True
    assert trie.search("these") == False
    assert trie.starts_with("the") == True
    assert trie.starts_with("ther") == True
    assert trie.search("an") == False
    assert trie.starts_with("an") == True
    print("✓ Passed")
    
    # Test 8: Duplicate insertions
    print("\nTest 8: Duplicate insertions")
    trie = Trie()
    trie.insert("test")
    trie.insert("test")  # Insert same word again
    assert trie.search("test") == True
    print("✓ Passed")
    
    print("\n✅ All tests passed!")