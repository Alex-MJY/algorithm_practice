# 조회 구조 개선 (for문은 하나만 사용하기)

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i