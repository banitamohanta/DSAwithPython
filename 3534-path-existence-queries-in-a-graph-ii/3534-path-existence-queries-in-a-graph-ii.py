class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        arr = sorted((nums[i], i) for i in range(n))
        pos = [0] * n
        values = [0] * n
        for i, (v, idx) in enumerate(arr):
            pos[idx] = i
            values[i] = v
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        nxt = [0] * n
        r = 0
        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            nxt[l] = r

        LOG = n.bit_length()

        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            a = pos[u]
            b = pos[v]

            if a > b:
                a, b = b, a

            if comp[a] != comp[b]:
                ans.append(-1)
                continue

            cur = a
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < b:
                    cur = up[k][cur]
                    steps += 1 << k

            ans.append(steps + 1)

        return ans
        