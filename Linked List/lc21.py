# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys, collections, heapq, functools, itertools, re, math, bisect, typing

'''
조건에 맞게 스왑하면서 그 다음 값이 엮이도록 계속 재귀호출을 하면, 연결 리스트가
점점 하나로 병합되면서 엮이게 된다.
'''

class Solution:
    # list1, list2 == ListNode
    def mergeTwoLists(self, list1, list2):
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1