'''매일의 화씨 온도(F) 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서 며칠을 더 기다려야 하는지 출력하라.'''

# stack
# 현재의 인덱스를 스택에 쌓아두다가, 이전보다 상승하는 지점에서 현재 온도와 스택에 쌓아둔 인덱스 지점의 온도 차이를 비교해서, 더 높다면 스택의 값을 꺼내고 
# 현재 인덱스와 스택에 쌓아둔 인덱스의 차이를 정답으로 처리한다.
class Solution1:
    def dailyTemperatures(self, temperatures: list):
        answer = [0] * len(temperatures)
        stack = []

        for i, cur in enumerate(temperatures):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer