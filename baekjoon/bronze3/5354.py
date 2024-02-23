import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    print('#' * n)
    for i in range(n - 2):
        print(f"#{'J' * (n - 2)}#")
    print('#' * n)