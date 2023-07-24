'''전체 수 n을 입력받아 k개의 조합(combination)을 리턴하라.'''

# dfs로 k개 조합 생성
# 순열의 경우 자기 자신을 제외한 요소들을 next_elements로 처리했으나, 조합의 경우 자기 자신뿐 아니라 앞의 모든 요소들을 배제하고 next_elements를 구성한다.
class Solution:
    def combine(self, n: int, k: int):
        result = []
        
        def dfs(start, elements):
            if len(start) == k:
                result.append(elements.copy())
                return
        
            for i in range(start, n + 1):
                elements.append(i)
                dfs(i + 1, elements)
                elements.pop()
        
        dfs(1, [])
        return result