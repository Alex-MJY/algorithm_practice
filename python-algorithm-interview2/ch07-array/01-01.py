# brute force는 마지막 element까지 일일히 확인하는 방식이다. 비효율적이지만 쉽다. 시간복잡도 O(n^2)
class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        
# in의 시간복잡도도 O(n)이기 때문에 O(n^2)의 시간복잡도지만 연산이 더 가볍고 빠르다.
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            complement = target - n
        if complement in nums[i + 1]:
            return nums.index(n), nums[i + 1:].index(complement) + (i + 1)


# 타겟에서 첫 번째 수를 빼면 두 번째 수를 알아낼 수 있다. 두 번째 인덱스를 키로 하고 기존의 인덱스를 밸류로 딕셔너리에 저장하면,
# 두 번째 수를 키로 조회해서 정답을 즉시 찾을 수 있다. 
# 타겟에서 첫 번째 수를 뺀 결과를 키로 조회하면 두 번째 수의 인덱스를 즉시 조회할 수 있다.
# 딕셔너리는 해시 테이블로 구현되고, 평균적으로 O(1)에 검색 가능하다.
class Solution3:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]
            
            
# solution3의 두 for문을 합칠 수 있다. 실행속도의 큰 차이는 없다.
class Solution4:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i