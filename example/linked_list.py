class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def __len__(self):
        return self.length
        
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)



# node = head
# while node:
#     print(node.data, end=" ")
#     node = node.next
    
