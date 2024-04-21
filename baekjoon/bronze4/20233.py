import sys
input = sys.stdin.readline

a = int(input()) # 한달 요금 / 30분부터 추가요금
x = int(input()) # a의 추가요금
b = int(input()) # 한달 요금 / 45분부터 추가요금
y = int(input()) # b의 추가요금
t = int(input()) # 하루 출퇴근 시간

result = []

if (t - 30) >= 0:
    result.append((((t - 30) * x) * 21) + a)
else:   
    result.append(a)
    
if (t - 45) >= 0:
    result.append((((t - 45) * y) * 21) + b)
else:
    result.append(b)
    
print(*result)