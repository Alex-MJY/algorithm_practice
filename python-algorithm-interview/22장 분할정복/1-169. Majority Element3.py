# divide and conquer

'''
먼저 분할을 시도한다. a와 b는 각각 최소 단위로 쪼개질 것이다. 그렇게 하기 위해서는 상단에 끊어서 리턴해주는 부분이 필요하다.
    a = self.majorityElement(nums[:half])
    b = self.majorityElement(nums[half:])
    
마지막으로 백트래킹될 때 처리하는 부분, 즉 정복 단계에 해당하는 부분을 아래처럼 구현한다
    return [b, a][nums.count(a) > half]
    
만약 a가 과반수를 차지한다면 해당 인덱스는 1이 될 것이고, [b, a][1]이 되어 a를 리턴할 것이다.
이외에는 b를 리턴한다. 만약 [2,2,1]이 있을 때 각각 2와 1이 백트래킹되고 2가 과반수를 차지하므로 [1, 2][1]이 되어 2를 리턴하게 된다.
최종적으로 루트에 이르러서는 양쪽 모두 2,2 가 리턴되었고 이 경우는 예외 없이 2가 정답이다.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half] # ture/false