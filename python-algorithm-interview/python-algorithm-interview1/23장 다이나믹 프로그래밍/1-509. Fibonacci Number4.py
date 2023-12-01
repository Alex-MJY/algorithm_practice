'''
두 변수만 이용해 공간 절약
앞선 풀이처럼 메소드 바깥에 클래스의 멤버 변수도 선언할 필요가 없기 때문에 코드가 훨씬 간결하다.
공간 복잡도도 O(n)에서 O(1)로 줄어든다. 시간 복잡도는 동일한 O(1)이다.
'''
class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x+y
        return x