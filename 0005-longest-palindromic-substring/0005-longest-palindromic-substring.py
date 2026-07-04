class Solution(object):
    def longestPalindrome(self, s):
        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp = s[i:j+1]
                if temp == temp[::-1] and len(temp) > len(ans):
                    ans = temp
        return ans

        