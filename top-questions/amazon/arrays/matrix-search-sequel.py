class Solution:
  def binary_search(self, row, target):
    lo = 0
    hi = len(row)

    while lo <= hi:
      mid = lo + (hi - lo) // 2
      if row[mid] == target:
        return True
      elif target < row[mid]:
        hi = mid - 1
      else:
        lo = mid + 1

    return False

  def solve(self, matrix, target):
    for row in matrix:
      if row[0] <= target and row[-1] >= target:
        if self.binary_search(row, target):
          return True
    return False