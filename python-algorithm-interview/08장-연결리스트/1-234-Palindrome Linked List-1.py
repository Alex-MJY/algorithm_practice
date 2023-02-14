# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        q = []
        
        if not head:
            return True
        
        node = head
        
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # 펠린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
            
        return True
    
'''
파이썬의 리스트는 q.pop(0) != q.pop() 형태로 인덱스를 지정해서 비교가 가능하기 때문에
자료형을 변경하여 리스트만으로도 충분히 풀이할 수 있다.
'''