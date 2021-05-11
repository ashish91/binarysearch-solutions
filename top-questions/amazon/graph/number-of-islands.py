class Solution:
  def solve(self, mat):
    def dfs(mat, i, j, M, N):
      if (i < 0 or i >= M or j < 0 or j >= N) or mat[i][j] == 0:
        return

      mat[i][j] = 0
      dfs(mat, i+1, j, M, N)
      dfs(mat, i, j-1, M, N)
      dfs(mat, i, j+1, M, N)
      dfs(mat, i-1, j, M, N)

    islands = 0
    R, C = len(mat), len(mat[0])
    for r in range(R):
      for c in range(C):
        if mat[r][c] == 1:
          islands += 1
          dfs(mat, r, c, R, C)

    return islands