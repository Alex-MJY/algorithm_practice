import itertools

class Solution:
    def permute(self, nums: list):
        return list(itertools.permutations(nums))
    
nums = [1,2,3]
c = Solution()
print(c.permute(nums))