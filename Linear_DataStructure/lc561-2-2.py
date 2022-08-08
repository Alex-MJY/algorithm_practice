class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        sum = 0
        
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        return sum
        