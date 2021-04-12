class Solution:
  def solve(self, nums):
    if nums[0] > nums[1]:
      return False

    prev = float('inf')
    for v in nums:
      if prev == v:
        return False
      prev = v

    return True