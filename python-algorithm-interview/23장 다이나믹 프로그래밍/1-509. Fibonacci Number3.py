# tabulation
'''
재귀를 사용하지 않고 반복으로 풀이하며, 작은 값부터 직접 계산하면서 타뷸레이션 한다.
미리 계산을 해두는 것인데, 다른 복잡한 다이나믹 프로그래밍 문제와는 달리 일차원 선형 구조라 구조 자체가 단순하다.
'''

import collections

class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        self.dp[1] = 1

        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[n]