import sys, collections, heapq, functools, itertools, re, math, bisect, typing

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head == ListNode
class Solution:
    def isPalindrome(self, head):
        q = collections.deque()
        
        # exception handling
        if not head:
            return True
        
        node = head
        # list conversion
        while node is not None:
            q.append(node.val)
            node = node.next
            
            
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True