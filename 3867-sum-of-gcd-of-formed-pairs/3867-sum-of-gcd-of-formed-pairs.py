class Solution(object):
    def gcdSum(self, nums):
        def findGcd(a, b):
            while b:
                a, b = b, a % b
            return a

        prefixGcd = []
        mx = 0

        for x in nums:
            if x > mx:
                mx = x
            prefixGcd.append(findGcd(x, mx))

        prefixGcd.sort()

        ans = 0
        i = 0
        j = len(prefixGcd) - 1

        while i < j:
            ans += findGcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return ans
        