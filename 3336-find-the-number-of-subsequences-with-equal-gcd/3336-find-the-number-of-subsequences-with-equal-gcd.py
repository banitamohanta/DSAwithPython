class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        dp = {}
        dp[(0, 0)] = 1
        for num in nums:
            new_dp = {}
            for (g1, g2), count in dp.items():
                key = (g1, g2)
                new_dp[key] = (new_dp.get(key, 0) + count) % MOD
                if g1 == 0:
                    ng1 = num
                else:
                    ng1 = self.gcd(g1, num)
                key = (ng1, g2)
                new_dp[key] = (new_dp.get(key, 0) + count) % MOD
                if g2 == 0:
                    ng2 = num
                else:
                    ng2 = self.gcd(g2, num)
                key = (g1, ng2)
                new_dp[key] = (new_dp.get(key, 0) + count) % MOD
            dp = new_dp
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 != 0 and g1 == g2:
                ans = (ans + count) % MOD
        return ans