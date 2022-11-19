# 첫 번째 수를 뺀 결과 key 조회

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        nums_map = dict()
        
        for i, num in enumerate(nums):
            nums_map[num] = i
            
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]