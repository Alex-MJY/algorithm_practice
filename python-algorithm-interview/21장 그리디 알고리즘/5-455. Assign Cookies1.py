'''
그리디로 배분하면 쉽게 풀린다.
배분 전에 정렬해주는 작업을 진행해야 한다.
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        chile_i = cookie_j = 0
        # 만족하지 못할 때까지 그리디 진행
        while chile_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[chile_i]:
                chile_i += 1
            cookie_j += 1
        return chile_i