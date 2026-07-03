class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        g = [[] for _ in range(n)]
        indeg = [0] * n
        vals = []
        for u, v, w in edges:
            g[u].append((v, w))
            indeg[v] += 1
            vals.append(w)
        if not vals:
            return -1
        q = deque(i for i in range(n) if indeg[i] == 0)
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, w in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        vals = sorted(set(vals))
        def check(x):
            dp = [float("inf")] * n
            dp[0] = 0
            for u in topo:
                if dp[u] == float("inf"):
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                for v, w in g[u]:
                    if w >= x and (v == n - 1 or online[v]):
                        dp[v] = min(dp[v], dp[u] + w)

            return dp[-1] <= k
        l, r = 0, len(vals) - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if check(vals[mid]):
                ans = vals[mid]
                l = mid + 1
            else:
                r = mid - 1
        return ans
        