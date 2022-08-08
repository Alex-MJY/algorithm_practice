class Solution:
    def trap(self, height):
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
                                  
            #더 큰 값이 기준점이 될 수 있기 때문에 작은 걸 옮겨준다.
            if left_max <= right_max: 
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
                
        return volume        