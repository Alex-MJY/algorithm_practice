'''
기차. 4개의 정차역. 타거나 내리는 사람 자동 인식. 
출발역에서 종착역까지 가는 도중 가장 사람이 많을 때의 사람 수 계산?
역에서 기차에 탈 때, 내릴 사람이 모두 내린 후에 탄다.

'''

import sys
input = sys.stdin.readline

counter = 0
array = []
for i in range(4):
    o, i = map(int, input().split())
    counter -= o
    array.append(counter)
    counter += i
    array.append(counter)
print(max(array))