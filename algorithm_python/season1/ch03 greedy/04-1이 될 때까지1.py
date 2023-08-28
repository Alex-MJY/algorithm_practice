'''
어떠한 수 N이 1이 될 때까지 아래의 과정 중 하나를 반복 수행한다. 두 번째 연산은 N이 K로 나누어 떨어질 경우에만 선택 가능하다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.

N이 1이 될 때까지 1또는 2의 과정을 수행하는 최소 횟수를 구해라.
'''

n, k = map(int, input().split())
count = 0

while True:
    if n == 1:
        break
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1
print(count)