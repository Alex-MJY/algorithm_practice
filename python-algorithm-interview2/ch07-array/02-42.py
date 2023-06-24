# 높이와 너비 모든 공간을 차례대로 모두 살펴보면 O(n^2)이 걸린다
# 투 포인터 또는 스택으로 O(n) 풀이가 가능


# two pointer 
# 가장 높이가 높은 막대는 최대 높이가 전체 부피에 영향을 끼치지 않는다(왼쪽과 오른쪽을 가르는 장벽 역할)
# 최대 높이의 막대까지 좌우 기둥 최대높이가 현재 높이와의 차이만큼 볼륨을 더한다
class Solution1:
    def trap(self, height: list) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume 
    
    
# stack
# inflection point(부분 변곡점)을 기준으로 격차만큼 볼륨을 더한다
# 이전 높이는 높이가 들쑥날쑥하기 때문에, 스택을 채우다가 변곡점을 만날 때 스택에서 하나씩 꺼내며넛 이전과의 차이만큼 물 높이를 채운다
class Solution2:
    def trap(self, height: list):
        stack = []
        volume = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not len(stack):
                    break
                
                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volume += distance * waters
            stack.append(i)
        return volume