class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
    
'''
모든 값을 꺼내서 푸시Push 하지않고도 한번에 heapity() 하여 처리할 수 있다. 
heapify( )란주어진자료구조가힙특성을만족하도록바꿔주는연산이며, 
이경우파이 썬의일반적인리스트는힙특성을만족하는리스트로, 값의위치가변경된다. 

'''