'''
행렬을 사용하면 n번째 피보나치 수를 O(log n)번의 연산으로 구할 수 있다.
선형대수 관점에서 행렬의 n승을 계산하는 방식으로, numpy 모듈을 사용했다
'''

import numpy as np

class Solution:
    def fib(self, n):
        M = np.matrix([0, 1], [1, 1])
        vec = np.array([[0], [1]])
        
        return np.matmul(M ** n, vec)[0]