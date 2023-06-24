# 자기 자신을 제외하고 왼쪽의 곱셈 결과와 오른쪽의 곱셈 결과를 곱해야 한다
# 기준점의 왼쪽 부분의 곱셈 값들을 리스트에 저장한 이후 같은 리스트를 재활용하여 
# 오른쪽의 마지막 값부터 차례대로 곱하면 공간복잡도 O(1)에 풀이가 가능하다


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        out = []
        p = 1

        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out