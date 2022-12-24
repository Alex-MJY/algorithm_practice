# 첫 번째 수를 뺀 결과 key 조회
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        nums_map = dict()
        
        for i, num in enumerate(nums):
            nums_map[num] = i
            
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]
            
'''
타겟에서 첫 번째 수를 빼면 두 번째 수를 알아낼 수 있다.
두 번째 수를 키로 하고 기존의 인덱스는 값으로 바꿔서 딕셔너리에 저장하면, 나중에
두 번째 수를 키로 조회해서 정답을 찾아낼 수 있다.

타겟에서 첫 번째 수를 뺀 결과를 키로 조회하면 두 번째 수의 인덱스를 O(1)에 조회할 수 있다.
최악의 경우는 O(n)이지만 매우 드물다.
'''