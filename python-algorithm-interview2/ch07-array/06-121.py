'''한 번의 거래로 낼 수 있는 최대 이익을 산출하라.'''

# brute force
# 처음부터 O(n^2)으로 사고팔고를 반복해서, 마지막에 최대 이익 산출. 비효율
class Solution1:
    def maxProfit(self, prices: list[int]) -> int:
        max_price = 0

        for idx, price in enumerate(prices):
            for j in range(idx, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price
    
# 저점과 현재 값과의 차이 계산
# 현재값을 가리키는 포인터가 우측으로 이동하면서 이전 상태의 저점을 기준으로 가격 차이를 계산하고 최댓값을 계속 교체
# 최댓값이 되어야 할 profit(max_price) 변수는 최솟값으로, 최솟값이 되어야 할 min_price 변수는 최댓값으로 지정한다. 그래야 어느 값이 들어오든 교체 가능하다
# None으로 초기화하면 타입 에러가 발생할 수 있다
# max_price를 0으로 초기화하는 이유는 최종 결과로 리턴되는 값인데, 입력값이 []일 경우, -sys.maxsize가 그대로 리털될 수 있기 때문
import sys

class Solution2:
    def maxProfit(self, prices: list[int]):
        max_price = 0 # profit
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(min_price, price)
            max_price = max(max_price, price - min_price)
        return max_price