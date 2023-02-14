class Solution:
    def productExceptSelf(self, nums: list) -> list:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
            
        p = 1
        #왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums)-1, 0-1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out
    
'''
나눗셈을 하지 말고 O(n)에 풀이하라는 제약사항이 있다.
자기 자신을 제외하고 왼쪽의 곱셈 결과와 오른쪽의 곱셈 결과를 곱해야 한다.
'''