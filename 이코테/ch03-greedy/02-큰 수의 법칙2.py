'''
결국엔 0부터 k+1까지의 값들이 반복되는 수열 구조이다. (M을 k+1로 나눈 몫이 수열이 된다)
몫이 나누어 떨어지지 않을 경우는 순차적으로 더해준다.
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
             
result = 0

first = data[-1]
second = data[-2]

count = int(m / (k + 1)) * k
print(count)
count += m % (k + 1)
print(count)

result += ((count) * first) + ((m - count) * second)

print(result)