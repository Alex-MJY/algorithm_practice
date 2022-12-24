# two pointer

class Solution:
    def trap(self, height: list) -> int:
        if not height:
            return 0
        
        volume = 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
                
        return volume
    
'''
최대 높이는 3이지만 100이어도 상관 없다.
막대는 높고 낮음에 무관하게, 전체 부피에 영향을 끼치지 않고, 왼쪽과 오른쪽을 가르는 장벽 역할을 한다.

최대 높이의 막대까지 각각 좌우 기둥 최대 높이 left_max, right_max가 현재 높이와의 차이만큼 물 높이 volume을 더해 나간다.

좌우 어느 쪽이든 낮은 쪽은 높은 곳을 향해서 포인터가 가운데로 점점 이동한다. 
가장 높은 막대인 '최대'지점에서 좌우 포인터가 서로 만나며 끝난다.
'''