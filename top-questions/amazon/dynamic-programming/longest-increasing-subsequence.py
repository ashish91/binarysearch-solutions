class Solution:
  def solve(self, nums):
    N = len(nums)

    if N < 2:
      return N
    dp = [1] * N

    for j in range(1, N):
      for i in range(0, j):
        if nums[j] > nums[i]:
          dp[j] = max(dp[j], dp[i]+1)

    return max(dp)