import sys
input = sys.stdin.readline

odd_sum = 0
smaller = 100
for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        odd_sum += n
        if n <= smaller:
            smaller = n
        
        
if odd_sum == 0:
    print(-1)
else:
    print(odd_sum)
    print(smaller)