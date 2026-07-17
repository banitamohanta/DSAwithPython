class Solution(object):
    def gcdValues(self, nums, queries):
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
        cnt = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            for m in range(d, max_val + 1, d):
                cnt[d] += freq[m]
        exact = [0] * (max_val + 1)
        for d in range(max_val, 0, -1):
            pairs = cnt[d] * (cnt[d] - 1) // 2
            m = d * 2
            while m <= max_val:
                pairs -= exact[m]
                m += d
            exact[d] = pairs
        prefix = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix[i] = prefix[i - 1] + exact[i]

        ans = []

        for q in queries:
            target = q + 1
            left = 1
            right = max_val

            while left < right:
                mid = (left + right) // 2
                if prefix[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

            ans.append(left)

        return ans
        
        