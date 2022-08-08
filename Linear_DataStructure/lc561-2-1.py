# 홀수
class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        result = sum(nums[::2])
        return result