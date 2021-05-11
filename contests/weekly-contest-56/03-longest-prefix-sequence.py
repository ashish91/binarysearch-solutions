# Longest Prefix Sequence
#
# You are given a list of lowercase alphabet strings words.
# Return the length of the longest sequence of words where each previous word is
# the prefix of the next word and the next word has just one new character appended.
# You can rearrange words in any order.
#
# Constraints
#
# 0 ≤ n ≤ 100,000 where n is the length of words
# 1 ≤ m ≤ 100,000 where m is the length of the longest string in words
#
# Solution 1
# ----------
#
# Using DP with hash table
#
# n - No of words
# m - Max characters per word
#
# Sorting will take nlogn and comparison of two strings will take m
#
# Time Complexity: O(nmlog(n))
# Space Complexity: O(nm)
class Solution:
  def solve(self, words):
    words.sort()
    dp = defaultdict(int)

    lps = 0
    for word in words:
      dp[word] = dp[word[:-1]] + 1
      lps = max(lps, dp[word])

    return lps

# Solution 2
# ----------
#
# Using Trie
#
# n - No of words
# m - Max characters per word
#
# O(nm) comes from Trie since total no of nodes will be total no of chars
# Insert will take that much time since each char needs to be added
#
# Time Complexity: O(nmlog(n)+O(nm))
# Space Complexity: O(nm)
class TrieNode:
  def __init__(self):
    self.children = defaultdict(TrieNode)
    self.isWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root

    for c in word:
      node = node.children[c]

    node.isWord = True

  def search(self, word):
    node = self.root
    count = 0

    for c in word:
      node = node.children[c]
      if node.isWord:
        count += 1

    return count

class Solution:
  def solve(self, words):
    words.sort()
    trie = Trie()
    lps = 0
    for word in words:
      trie.insert(word)
      lps = max(lps, trie.search(word))

    return lps




