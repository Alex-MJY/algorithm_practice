import sys
input = sys.stdin.readline
arr = []

user1 = list(map(int, input().split()))
arr.append((1000 / user1[1]) * user1[0])
for i in range(int(input())):
    user2 = list(map(int, input().split()))
    arr.append((1000 / user2[1]) * user2[0])
print(round(min(arr), 2))