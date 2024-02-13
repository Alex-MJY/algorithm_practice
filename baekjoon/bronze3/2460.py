'''
기차. 1~10번역까지 운행. 역마다 사람 수 자동 인식. 가장 사람이 많을 때?

'''

import sys
input = sys.stdin.readline

counter = 0
array = []
for i in range(10):
    o, i = map(int, input().split())
    counter -= o
    array.append(counter)
    counter += i
    array.append(counter)
print(max(array))