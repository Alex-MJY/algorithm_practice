arr = list(map(int, input().split()))
arr.sort()

if abs(arr[1] - arr[0]) == abs(arr[2] - arr[1]):
    print(arr[2] + abs(arr[2] - arr[1]))
elif abs(arr[1] - arr[0]) < abs(arr[2] - arr[1]):
    print(arr[1] + abs(arr[1] - arr[0]))
else:
    print(arr[1] - abs(arr[2] - arr[1]))