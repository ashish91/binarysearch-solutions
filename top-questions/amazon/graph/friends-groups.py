class Solution:
    def solve(self, friends):
        N = len(friends)
        visited = {}
        groups = 0

        def dfs(curr):
            nonlocal friends
            nonlocal visited

            for nei in friends[curr]:
                if nei not in visited:
                    visited[nei] = True
                    dfs(nei)

        for i in range(N):
            if not i in visited:
                visited[i] = True
                dfs(i)

                groups += 1

        return groups
