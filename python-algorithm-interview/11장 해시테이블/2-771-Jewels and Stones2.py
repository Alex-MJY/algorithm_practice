import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        # calculate the frequency of stones
        for char in stones:
            freqs[char] += 1
        
        # sum frequency counts of jewels
        for char in jewels:
            count += freqs[char]

        return count