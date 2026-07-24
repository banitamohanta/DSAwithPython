class Solution(object):
    def uniqueXorTriplets(self, nums):
        MAXX = 2048

        vals = list(set(nums))  # duplicates don't matter

        pair = [False] * MAXX
        for a in vals:
            for b in vals:
                pair[a ^ b] = True

        triple = [False] * MAXX
        for x in range(MAXX):
            if pair[x]:
                for v in vals:
                    triple[x ^ v] = True

        return sum(triple)
        