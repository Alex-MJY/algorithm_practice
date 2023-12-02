# Array

class Array:
    def __init__(self):
        self.array = {}
        self.length = 0
        
    def append(self, value):
        # self.value = value
        self.array[self.length] = value
        self.length += 1
    
    def prepend(self, value):
        self.array[1] = self.array[0]
    
    def pop(self):
        pass
    
a = Array()
a.append("google")
a.append("naver")
a.append("kakao")
print(a.array)