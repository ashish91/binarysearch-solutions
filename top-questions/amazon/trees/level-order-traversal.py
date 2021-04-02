# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    q = [root]
    level = []

    while len(q) > 0:
      curr = q.pop(0)
      if curr is None:
        continue

      level.append(curr.val)
      q.append(curr.left)
      q.append(curr.right)

    return level