l = int(input()) # 방학일수
a = int(input()) # 국어 숙제 페이지 수
b = int(input()) # 수학 숙제 페이지 수
c = int(input()) # 국어 가능 수
d = int(input()) # 수학 가능 수

korean = 0
if a % c > 0:
    korean = (a // c) + 1
else:
    korean = a // c
    
math = 0
if b % d > 0:
    math = (b // d) + 1
else:
    math = b // d
    
print(l - max(korean, math))