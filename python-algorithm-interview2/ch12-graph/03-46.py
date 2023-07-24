'''서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라'''

# dfs를 활용한 순열 생성
# 순열은 분자의 팩토리얼만 계산하면 되기 때문에 쉽다. 그러나 모든 결과를 출력(생성)하는 것은 까다롭다.
# 순열이란 모든 가능한 경우를 그래프 형태로 나열한 결과다. (그래프의 레벨이 증가할수록 자식 노드의 개수는 줄어든다.
class Solution1:
    def permute(self, nums: list):
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:]) # 참조 관계를 갖지 않도록 복사값을 넣어준다.

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results
 
 
 
 # itertools module 사용
import itertools

class Solution2:
    def permute(self, nums: list):
        return list(itertools.permutations(nums))