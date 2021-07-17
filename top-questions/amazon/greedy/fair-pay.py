class Solution:
  def solve(self, ratings):
    N = len(ratings)
    if N < 1:
      return N

    l = [1 for i in range(N)]
    r = [1 for i in range(N)]

    for i in range(1, N):
      if ratings[i-1] < ratings[i]:
        l[i] = l[i-1] + 1

    for i in range(N-2, -1, -1):
      if ratings[i] > ratings[i+1]:
        r[i] = r[i+1] + 1

    ans = 0
    for i in range(N):
      ans += max(l[i], r[i])

    return ans