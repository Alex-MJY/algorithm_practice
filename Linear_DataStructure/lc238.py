# 자기 자신을 제외하고 왼쪽의 곱셈 결과와 오른쪽의 곱셈 결과를 곱해야 한다.
class Solution:
    def productExceptSelf(self, nums):
        out = []
        p = 1 
        
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        
        p = 1
        for i in range(len(nums)-1, 0-1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        
        return out