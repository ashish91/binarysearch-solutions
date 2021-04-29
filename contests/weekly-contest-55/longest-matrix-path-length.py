class Solution:
  def solve(self, mat):
    R, C = len(mat), len(mat[0])
    prev_dp = [0] * C

    for i in range(R):
      curr_dp = [-float('infinity')] * C

      curr = 0
      while curr < C:
        # Skip walls
        while curr < C and mat[i][curr] == 1:
          curr += 1
        l = curr

        # Find next wall
        while curr < C and mat[i][curr] == 0:
          curr += 1
        r = curr - 1

        if l == C:
          continue

        max_path = -float('infinity')
        for k in range(l, r+1):
          max_path = max(max_path + 1, prev_dp[k]+1)
          curr_dp[k] = max_path

        max_path = -float('infinity')
        for k in reversed(range(l, r+1)):
          max_path = max(max_path + 1, prev_dp[k]+1)
          curr_dp[k] = max(curr_dp[k], max_path)

      prev_dp = curr_dp

    return max(0, max(curr_dp))
