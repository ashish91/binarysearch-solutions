# class Tree:
#   def __init__(self, val, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def solve(self, root):
    maxsum = -float('infinity')
    def dfs(node):
      nonlocal maxsum
      left, right = 0,0
      if node.left is not None:
        left = dfs(node.left)
      if node.right is not None:
        right = dfs(node.right)

      maxsum = max(left + right + node.val, maxsum)

      return left + right + node.val

    dfs(root)
    return max(maxsum,0)