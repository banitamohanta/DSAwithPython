class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        ones = s.count('1')
        n = len(s)

        ans = ones
        i = 0

        while i < n:
            if s[i] == '0':
                l = 0
                while i < n and s[i] == '0':
                    l += 1
                    i += 1

                if i == n:
                    break
                j = i
                one = 0
                while j < n and s[j] == '1':
                    one += 1
                    j += 1

                if i > l - 1 and j < n and s[j] == '0':
                    r = 0
                    k = j
                    while k < n and s[k] == '0':
                        r += 1
                        k += 1
                    ans = max(ans, ones + l + r)

                i = j
            else:
                i += 1

        return ans
        