'''2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.'''

# 모든 조합 탐색
# 각 자릿수에 해당하는 키판 배열을 dfs로 탐색하면 결과가 완성된다.
# dfs() 함수는 자릿수가 동일할 때까지 재귀 호출을 반복하다 끝까지 탐색하면 결과를 추가하고 리턴한다.
# 모든 경우의 수를 dfs로 탐색하고 백트래킹으로 결과를 조합하면서 리턴하게 된다.
class Solution:
    def letterCombinations(self, digits: str) -> list:
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return

            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        # exception handling
        if not digits:
            return []

        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        dfs(0, "")

        return result
    
# 어렵다