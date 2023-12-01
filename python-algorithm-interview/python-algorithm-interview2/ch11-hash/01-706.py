'''다음의 기능을 제공하는 해시맵을 디자인하라. put(key, value), get(key), remove(key)
MyHashMap hashMap = mew MyHashMap();'''


# 개별 체이닝(separate chaining) 방식을 이용한 해시 테이블 구현

# push()
# 키와 값을 보관하여 연결리스트로 처리할 별도의 객체를 구현해야 하는데, ListNode 클래스를 정의한다.
# 기본 사이즈는 1000개 정도로 적당히 설정하고, 각 ListNode를 담게 될 기본 자료형을 선언한다. 편리하게 구현하기 위해 존재하지 않는 키를 조회할 경우
# 디폴트를 생성해주는 collections.defaultdict를 사용한다.
# 모든 키를 정수형으로 지정하고, size의 개수만큼 모듈로 연산을 한 나머지를 해시값으로 처리하고, index 변수에 담는다.
# 해시 충돌(hash collision)이 발생한 경우 개별 체이닝 방식으로 충돌을 해결한다.
# p는 인덱스의 첫번째 값이며 여기서부터 p.next를 계속 탐색한다. 이미 키가 존재할 경우 값을 업데이트하고 빠져나가고, 키가 없다면 값을 넣어준다.

# get()
# 마찬가지로 모듈로 연산으로 인덱스를 정하고, 해당 인덱스에 아무것도 없다면 -1을 리턴한다.
# 만약 해싱 결과에 하나 이상의 노드가 존재한다면, p.next로 탐색하면서 일치하는 키를 찾는다. 찾지 못한다면 루프를 빠져나오고 -1을 리턴한다.

# remove()
# 인덱스를 구한 다음 아무것도 없다면,잘못된 키를 삭제 시도한 경우이므로 그냥 리턴한다. 값이 있을 경우 두가지 케이스로 나눠서 처리한다.
# 1. 인덱스의 첫 번째 노드일 때, p.next is None이라면 유일한 노드를 삭제하는 경우이기 때문에 모두 없애야 하지만, self.table은 defaultdict(ListNode)라서
# 매번 빈 노드를 생성하기 때문에, self.table[index] = None으로 처리한다면, 추가, 조회할 때 에러가 발생한다.
# 그래서 ListNode()로 빈 노드를 할당한다.
# 2. 연결 리스트 노드를 삭제할 때, prev는 이전 노드, p는 현재 노드로, 계속 p.next로 탐색하다가 일치하는 노드를 찾게 되면, 이전 노드의 다음을 
# 현재 노드의 다음으로 연결한다. 즉 현재 노드를 아무런 연결 고리가 없도록 끊어 버린다. 

import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        
    def put(self, key: int, value: int):
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
    
        # 인덱스에 노드가 있다면 연결 리스트 처리 (체이닝)
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return 
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)
        
    def get(self, key: int):
        index = key % self.size
        if self.table[index].value is None:
            return -1
        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
    
    def remove(self, key: int):
        index = key % self.size
        if self.table[index].value is None:
            return
        
        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
        
        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next # 연결고리 끊어주기
                return
            prev, p = p, p.next
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)