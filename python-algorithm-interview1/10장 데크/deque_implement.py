class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Deque:
    def __init__(self):
        self.front = None
        self.dequeSize = 0
        
    def isEmpty(self):
        if self.dequeSize == 0:
            return True
        return False
    
    def dequeLen(self):
        return self.dequeSize
    
    def insertFront(self, data):
        temp = Node(data)
        if self.front == None:
            self.front = temp
            self.dequeSize += 1
        else:
            temp.next = self.front
            self.front = temp
            self.dequeSize += 1
            
    def insertRear(self, data):
        temp = Node(data)
        if self.front == None:
            self.front = temp
            self.dequeSize += 1
        else:
            curr = self.temp
            while curr.next is not None:
                curr = curr.next
            curr.next = temp
            self.dequeSize += 1
            
    def delFront(self):
        try:
            if self.dequeSize == 0:
                raise Exception("Deque is Empty")
            else:
                temp = self.front
                self.front = self.front.next
                self.dequeSize -= 1
                del temp
        except Exception as e:
            print(str(e))
            
    def defRear(self):
        try:
            if self.dequeSize == 0:
                raise Exception("Deque is Empty")
            else:
                curr = self.front
                prev = None
                while curr.next != None:
                    prev = curr
                    curr = curr.next
                prev.next = curr.next
                self.dequeSize -= 1
                del curr
        except Exception as e:
            print(str(e))
            
    def getFront(self):
        try:
            if self.dequeSize == 0:
                raise Exception("Deque is Empty")
            else:
                return self.front.data
            
        except Exception as e:
            print(str(e))
            
    def getRear(self):
        try:
            if self.dequeSize == 0:
                raise Exception("Deque is Empty")
            else:
                curr = self.front
                while curr.next is not None:
                    curr = curr.next
                return curr.data
        except Exception as e:
            print(str(e))