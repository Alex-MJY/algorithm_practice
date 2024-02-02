'''
후라이드, 간장, 양념 중 인당 하나씩 부대원에게 배급
각 치킨별 선호하는 인원의 수 a, b, c
가장 선호하는 종류의 치킨을 받을 수 있는 인원수의 최댓값?

n : 각 종류의 치킨 마릿수
'''
n = int(input())
array = list(map(int, input().split()))
counter = 0

for i in array:
    if i < n:
        counter += i
    else:
        counter += n
print(counter)