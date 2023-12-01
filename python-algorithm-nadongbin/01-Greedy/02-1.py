# 큰 수의 법칙

'''
배열에서 주어진 수들을 M번 더하여 가장 큰 수를 만들어 한다
배열의 특정한 인덱스에 해당하는 수가 연속해서 k번을 초과하여 더해질 수 없다
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
    
print(result)