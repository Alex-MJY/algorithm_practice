import sys

class Solution:
    def maxProfit(self, prices: list) -> int:
        profit = 0
        min_price = sys.maxsize
        
        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit
    
'''
최댓값에는 가장 낮은 값을, 최소값에는 가장 높은 값으로 초기 설정해야
어떤 값이 들어오든 바로 교체될 수 있다.
만약 None으로 잡아두게 되면 크기 비쇼 시 TypeError가 발생할 수 있다.

이 문제에선 최대 이익인 profit이 나중에 최종 결과로 리턴되는데, 입력값이 []인 경우,
즉 빈 배열인 경우에는 -sys.maxsize가 그대로 리털될 수 있기 떄문에 0으로 초기화 한다.
'''