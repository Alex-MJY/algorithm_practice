import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())



arr = []

counter = 0
arr.append([(a / c) + (b / d), counter])

counter += 1
arr.append([(c / d) + (a / b), counter])

counter += 1
arr.append([(d / b) + (c / a), counter])


counter += 1
arr.append([(b / a) + (d / c), counter])

arr.sort(key= lambda x: x[0])
print(arr[3][1])