import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == arr[1] == arr[2] == 0: break
    
    arr.sort()
    
    if arr[2] >= arr[0] + arr[1]:
        print("Invalid")
        continue
    if len(set(arr)) == 1:
        print("Equilateral")
    elif len(set(arr)) == 2:
        print("Isosceles")
    elif len(set(arr)) == 3:
        print("Scalene")
    