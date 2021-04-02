class Solution:
  def solve(self, nums):
    N = len(nums)
    if N < 2:
      return 0

    left = [0] * N
    right = [0] * N

    lmax = nums[0]
    rmax = nums[-1]
    for i in range(N):
      lmax = max(lmax, nums[i])
      left[i] = lmax

      rmax = max(rmax, nums[N-i-1])
      right[N-i-1] = rmax

    drops = 0
    for i in range(1,N-1):
      drops += max(0, min(left[i-1], right[i+1]) - nums[i])

    return drops