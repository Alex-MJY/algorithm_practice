class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    '''
    처음 Trie 클래스를 생성하게 되면 루트 노드로 별도 선언한 TrieNode 클래스를 갖게 되고,
    삽입 시 루트부터 자식 노드가 점점 깊어지면서 문자 단위의 다진 트리(m-ary Tree) 형태가 된다.
    '''

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # 단어가 모두 완성되면, True가 된다.
        node.word = True

    '''
    문자열에서 문자를 하나씩 for 반복문으로 순회하면서 자식 노드로 계속 타고 내려간다.
    마지막에 node.word 여부를 리턴한다. 단약 단어가 완성된 트라이라면 True로 되어 있을 것이고,
    이때 True가 결과로 리턴된다.
    '''
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word
        
    '''
    startsWith는 search와 거의 동일하다. node.word를 확인하지 않고, 
    자식 노드가 존재하는지 여부만 판별한다. 자식 노드가 존재한다면 for 반복문을 끝까지 빠져나올 것이고, True를 리턴한다.
    '''
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)