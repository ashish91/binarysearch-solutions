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
#
#
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




