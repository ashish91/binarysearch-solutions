class Solution:
  def solve(self, N, requests):
    mark = [[0 for c in range(N)] for r in range(2)]
    blocked = set()

    paths = 0
    print(requests)
    for i,j,v in requests:
      mark[i][j] = v

      # we check 3 cases which are blocking:
      #
      # X .
      # . X
      #
      # . X
      # X .
      #
      # X .
      # X .
      #
      # if we see these cases we add it to blocked set
      for dir in [-1,1,0]:
        if 0 <= j+dir < N and mark[(i+1)%2][j+dir] == 1:
          if v == 1:
            blocked.add((i,j,(i+1)%2,j+dir))
          else:
            blocked.discard((i,j,(i+1)%2,j+dir))
            blocked.discard(((i+1)%2,j+dir,i,j))

      if not blocked and not (mark[0][-1] == 1 and mark[1][-1] == 1):
        paths += 1

    return paths