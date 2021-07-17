# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    max_path = 0
    def dfs(node):
      nonlocal max_path
      if node is None:
        return 0

      left  = dfs(node.left)
      right = dfs(node.right)

      max_path = max(left+right + 1, max_path)
      return max(left, right) + 1

    dfs(root)   
    return max_path   