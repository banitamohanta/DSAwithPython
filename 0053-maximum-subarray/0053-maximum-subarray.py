class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        c = 0
        s = nums[0]
        for i in range(n):
            c += nums[i]
            if c > s:
                s = c
            if c < 0:
                c = 0
        return s

        