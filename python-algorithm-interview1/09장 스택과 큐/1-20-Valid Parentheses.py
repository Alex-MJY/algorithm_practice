class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table: # table key값에 없다면 stack에 push
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0 # stack.pop과 table[char]이 같으면 stack에서 계속 빠져나가기 때문에 len == 0