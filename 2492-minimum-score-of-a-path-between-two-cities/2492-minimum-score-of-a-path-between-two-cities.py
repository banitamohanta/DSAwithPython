class Solution(object):
    def minScore(self, n, roads):
        graph = [[] for _ in range(n + 1)]
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
        visited = [False] * (n + 1)
        q = deque([1])
        visited[1] = True
        ans = float("inf")
        while q:
            node = q.popleft()
            for n, dist in graph[node]:
                ans = min(ans, dist)
                if not visited[n]:
                    visited[n] = True
                    q.append(n)
        return ans
        
        