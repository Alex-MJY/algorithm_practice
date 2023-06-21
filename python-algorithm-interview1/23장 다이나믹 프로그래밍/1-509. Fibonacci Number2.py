# memoization
'''
브루트 포스와 유사하게 재귀로 계산해 나가지만, 이미 계산한 값은 저장해뒀다가 바로 리턴한다.
앞서 fib(5)일 때 15번의 연산을 진행하던 구조는 메모이제이션 풀이에서는 9번의 연산만으로 풀 수 있다.
'''

import collections

class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]