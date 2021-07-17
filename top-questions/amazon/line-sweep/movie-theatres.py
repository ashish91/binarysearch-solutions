from collections import defaultdict

class Solution:
  def solve(self, intervals):
    sweep = defaultdict(int)

    for x in intervals:
      sweep[x[0]] += 1
      sweep[x[1]] -= 1

    curr = 0
    ans = 0
    for k in sorted(sweep.keys()):
      curr += sweep[k]
      ans = max(curr, ans)

    return ans