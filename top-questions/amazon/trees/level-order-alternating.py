# class Tree:
#   def __init__(self, val, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def solve(self, root):
    if root is None:
      return []

    q = [root]
    temp = []
    aux = []

    ans = [root.val]
    as_stack = True

    while len(q) > 0:
      while len(q) > 0:
        curr = q.pop(0)

        if not curr.left is None:
          temp.append(curr.left)
          aux.append(curr.left)

        if not curr.right is None:
          temp.append(curr.right)
          aux.append(curr.right)

      while len(aux) > 0:
        if as_stack:
          ans.append(aux.pop().val)
        else:
          ans.append(aux.pop(0).val)

      q = temp
      temp = []
      as_stack = not as_stack

    return ans