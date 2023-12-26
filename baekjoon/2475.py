numbers = list(map(int, input().split()))
result = 0
for i in numbers:
    result += i * i
print(result % 10)