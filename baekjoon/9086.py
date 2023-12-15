# import sys
# n = int(sys.stdin.readline())
# array = []
# for _ in range(n):
#     s = str(sys.stdin.readline())
#     string = s[0] + s[-1]
#     array.append(string)

# for i in array:
#     print(i)

import sys
n = int(input())
array = []

for i in range(n):
    s = str(input())
    string = s[0] + s[-1]
    array.append(string)

for i in array:
    print(i)