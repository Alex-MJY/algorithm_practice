'''연결리스트를 입력받아 pair단위로 스왑하라.'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 노드 구조는 그대로 유지하되 값만 바꾸는 방법
# 실용성과는 거리가 있다. 
class Solution1:
    def swapPairs(self, head):
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head
    
    
# 반복 구조 스왑
# b = a.next이고 a와 b를 스왑할 때 b가 a를 가리키고 a는 b의 다음을 가리키도록 변경한다. 그러나 아직 a의 이전 노드가 b를 가리키지 못한다
# a의 prev shemrk b를 가리키가 하고, 다음번 비교를 위해 prev는 두 칸 앞으로 이동한다
# 연결리스트의 head를 가리키는 노드가 직접 바뀌기 때문에, 그 이전 값을 root로 별도 설정한 다음, root.next를 리턴
class Solution2:
    def swapPairs(self, head: ListNode):
        root = prev = ListNode(None)
        prev.next = head
        
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next
    
    
# 재귀구조
# 반복 풀이와 달리 포인터 역할을 하는 p변수는 하나만 있어도 충분하며, 더미 노드를 만들 필요도 없이 head를 바로 리턴할 수 있어 공간 복잡도가 낮다
# p는 head.next가 되고, p.next는 head가 된다. 그 사이 재귀 호출로 계속 스왑된 값을 리턴받게 된다. 
class Solution3:
    def swapPairs(self, head: ListNode):
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head