class Solution:
  def solve(self, numeral):
    N = len(numeral)
    mapping = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    ans = 0
    prev = 0
    for i in reversed(range(N)):
      n = mapping[numeral[i]]
      if n >= prev:
        ans += int(n)
      else:
        ans -= int(n)
      prev = n
    return ans