class Solution:
    def arrayPairSum(self, nums: list) -> int:
        return sum(sorted(nums)[::2])