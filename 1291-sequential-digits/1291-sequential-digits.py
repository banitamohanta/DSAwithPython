class Solution(object):
    def sequentialDigits(self, low, high):
        s = "123456789"
        ans = []

        for length in range(2, 10):
            for i in range(0, 10 - length):
                num = int(s[i:i + length])

                if low <= num <= high:
                    ans.append(num)

        return ans