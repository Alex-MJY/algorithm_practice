import sys
input = sys.stdin.readline


result = []

for i in range(9):
    array = list(map(int, input().split()))
    result.append([max(array), i + 1, array.index(max(array)) + 1])
    
    
result.sort(key= lambda x: x[0])
print(result[-1][0])
print(result[-1][1], result[-1][2])