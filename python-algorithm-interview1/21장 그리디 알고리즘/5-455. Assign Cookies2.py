'''
2개의 리스트를 모두 번갈아가며 탐색하는 게 아니라 하나의 리스트를 순회하면서 다른 하나는 이진 검색으로 찾는다.
찾아낸 인덱스가 현재 부여한 아이들보다 클 경우에는 더 줄 수 있다는 말이 되므로, 줄 수 있는 아이들의 수를 1명 더 늘린다
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()

        result = 0
        for i in s:
            # 이진 검색으로 더 큰 인덱스 탐색
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1
        return result