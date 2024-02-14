'''
p와 q가 있을 때, p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다
두 개의 자연수 n과 k가 주어졌을 때, n의 약수들 중 k번째로 작은 수를 출력
'''
n, k = map(int, input().split())
array = []
for i in range(1, n + 1):
    if n % i == 0:
        array.append(i)
    
if len(array) < k:
    print(0)
else:
    print(array[k - 1])