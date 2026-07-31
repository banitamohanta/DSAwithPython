class Solution(object):
    def minimumPushes(self, word):
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        freq.sort(reverse=True)

        pushes = 0

        for i in range(26):
            if freq[i] == 0:
                break

            cost = (i // 8) + 1
            pushes += freq[i] * cost

        return pushes
        