# Find Local Peaks Sequel
#
# You are given a list of integers nums. Return the index of every peak in the list, sorted in ascending order.
# An index i is called a peak if all three conditions are true:
#
# The next number on its right that's different than nums[i] doesn't exist or is smaller than nums[i]
# The next number on its left that's different than nums[i] doesn't exist or is smaller than nums[i]
# There is at least one number on its left or its right that's different than nums[i]
# Constraints

# 0 ≤ n ≤ 100,000 where n is the length of nums
#
# Solution
# --------
#
# Using prefix array pre compute the right nearest number which is different
# then loop over comparing the element with left immediate number and right nearest number.
#
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
  def solve(self, nums):
    N = len(nums)

    # Base condition
    if N == 1:
      return []

    right = [float('-infinity')] * N

    # Pre compute right nearest number
    for i in reversed(range(0, N-1)):
      right[i] = right[i+1] if nums[i+1] == nums[i] else nums[i+1]

    peaks = []
    left = float('-infinity')
    for i in range(0,N):
      # If current nums[i] is greater than nearest right different number and nearest different left number
      # then it's a peak. Also check for if left and right is not present
      if (left != float('-infinity') or right[i] != float('-infinity')) and nums[i] > right[i] and nums[i] > left:
        peaks.append(i)

      # Update left when nums[i] is different then the next element
      if i != N-1 and nums[i] != nums[i+1]:
        left = nums[i]

    return peaks