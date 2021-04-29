# class LLNode:
#   def __init__(self, val, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def solve(self, head, pos, val):

    if pos == 0:
      node = LLNode(val)
      node.next = head
      return node

    curr = head
    while curr is not None:
      if pos == 1:
        node = LLNode(val)
        node.next = curr.next
        curr.next = node
        return head
      curr = curr.next
      pos -= 1
