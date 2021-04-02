# class Tree:
#   def __init__(self, val, left=None, right=None):
#   self.val = val
#   self.left = left
#   self.right = right
class Solution:
  def solve(self, root0, root1):
  q0 = [root0]
  q1 = [root1]

  while len(q0) > 0 and len(q1) > 0:
    curr0 = q0.pop(0)
    curr1 = q1.pop(0)

    if curr0 and curr1 and curr0.val == curr1.val:
    q0.append(curr0.left)
    q0.append(curr0.right)

    q1.append(curr1.left)
    q1.append(curr1.right)
    elif not ((curr0 is None) and (curr1 is None)):
    return False

  return True
