# kadane's algorithm

'''
최대 서브 배열을 찾기 위해 어디서 시작되는지를 찾는 문제 O(n^2) 풀이에서 각 단계마다 최댓값을 담아
어디서 끝나는지를 찾는 문제 O(n) 풀이로 치환해서 풀이했다.
'''

import sys

class Solution:
    def maxSubArray(self, nums: list) -> int:
        best_sum = -sys.maxsize
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum