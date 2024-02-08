'''
비밀 키를 만들어야 한다. 소수 p와 q를 주어 두 수의 곱 pq를 비밀키로.
p, q 중 하나라도 k보다 작은 암호는 무효.
'''
import sys
input = sys.stdin.readline
p, k = map(int, input().split())
for i in range(2, k):
    if p % i == 0:
        print("BAD", i)
        break
else:
    print("GOOD")