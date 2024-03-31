# runtime error

# import sys

# for i in range(int(sys.stdin.readline())):
#     n = int(sys.stdin.readline())
#     if (n + 1) % int(str(n)[-2:-1]) == 0:
#         print("Good")
#     else:
#         print("Bye")

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = str(input())
    if (int(n) + 1) % int(n[2:]) == 0:
        print("Good")
    else:
        print("Bye")