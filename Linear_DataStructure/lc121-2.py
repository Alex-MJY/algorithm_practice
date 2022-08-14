import sys, collections, heapq, functools, itertools, re, math, bisect, typing

class Solution:
    def maxProfit(self, prices):
        profit = 0
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit