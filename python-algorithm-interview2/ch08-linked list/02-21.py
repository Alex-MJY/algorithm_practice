'''정렬되어 있는 두 연결 리스트를 합쳐라.'''

from typing import Optional, ListNode

# recursive
# 정렬된 리스트여야 한다. 병합 정렬의 마지막 조합과 동일한 방식으로 첫 번째부터 비교하면서 리턴한다. 
# 스왑하면서 다음 값이 엮이도록 재귀호출하면, 연결 리스트가 하나로 병합되면서 엮이게 된다.
# 마지막에서 list1이 Null이 되면서 재귀가 끝나고 리턴을 시작한다. 리턴을 시작하면 백트래킹되면서 엮이게 된다. 
# 백트래킹이 종료되면 두 정렬 리스트가 병합되어 하나의 연결 리스트가 된다.
class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    

# recursive를 더 직관적으로 풀어쓴 코드
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1

    
# dummy 연결 리스트를 새로 생성해서 채워나가는 방법
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution3:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
            else:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return dummy.next