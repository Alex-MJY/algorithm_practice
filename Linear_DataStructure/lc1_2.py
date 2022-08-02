'''
모든 조합을 비교하지 않고, 타켓에서 첫 번째 값을 뺀 target - n이 존재하는지
탐색하면 더 빠르게 찾아낼 수 있다.

for문이 O(n)이고 in이 O(n)이기 때문에 bruteforce와 같은 O(n^2)이지만,
작성이 쉽다.
'''
class Solution:
    def twoSum(self, nums: list, target: int):
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i + 1:]:
                return nums.index(n), nums[i+1:].index(complement) + (i + 1)