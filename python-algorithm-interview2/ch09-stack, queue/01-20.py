'''괄호로 된 입력값이 올바른지 판별하라.'''

# (, [, { 는 스택에 push하고 ), ], }를 만날 때 스택에서 pop한 결과가 매핑 테이블 결과와 매칭되는지 확인한다.
# 먼저 매핑 테이블을 만들어 놓고 테이블에 존재하지 않으면 push하고, pop했을 때 결과가 일치하지 않으면 false를 리턴한다.
# 예외처리(스택이 비어있는지, 팝 결과가 일치하지 않는지 등등)은 필수
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0