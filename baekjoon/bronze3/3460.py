import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i - 1] == '1':
            print(i, end=' ')