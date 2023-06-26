# 팰린드롬 여부를 판별하기 위해선 앞뒤로 모두 추출할 수 있는 자료구조가 필요하다
# 리스트는 pop()을 이용하여 마지막 요소가 아니더라도 원하는 위치를 자유롭게 추출할 수 있다

class Solution1:
    def isPalindrome(self, head) -> bool:
        q: list = []

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True
    

# q.pop(0)으로 동적 배열로 구성된 리스트의 맨 앞을 추출하며 이후의 값들이 한 칸씩 시프팅되어 시간복잡도 O(n)이 발생한다
# collections.deque는 이중 연결 리스트 구조로 양쪽 방향 모두 추출하는 데 시간 복잡도 O(1)이 걸린다.
import collections
class Solution2:
    def isPalindrome(self, head) -> bool:
        q = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True
    
    
# runner 기법
# fast funner와 slow runner를 각각 출발시키면, 빠른 러너가 끝에 다다를 때 느린 러너는 중간까지 이동한다
# 역순으로 연결된 리스트 rev를 만들고, 느린 러너는 나머지 경로를 이동하며 둘의 값을 비교한다
class Solution3:
    def isPalindrome(self, head) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev