class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0

        # calculate the frequency of stones
        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        
        # sum frequency counts of jewels
        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count