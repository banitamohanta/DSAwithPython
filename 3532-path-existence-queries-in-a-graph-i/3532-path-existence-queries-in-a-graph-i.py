class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        group = [0] * n
        group[0] = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                group[i] = group[i - 1]
            else:
                group[i] = group[i - 1] + 1
        ans = []
        for u, v in queries:
            ans.append(group[u] == group[v])

        return ans
        