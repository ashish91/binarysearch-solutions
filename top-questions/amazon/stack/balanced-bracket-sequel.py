class Solution:
  def solve(self, s):
    val = { '(': ')', '{': '}', '[': ']' }
    stack = []

    for c in s:
      if c == '(' or c == '[' or c == '{':
        stack.append(c)
      elif len(stack) == 0 or val[stack.pop()] != c:
        return False

    return len(stack) == 0
