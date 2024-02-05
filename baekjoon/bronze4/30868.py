for i in range(int(input())):
    n = int(input())
    if n >= 5:
        print("++++ " * (n // 5), end='')
        print("|" * (n % 5))
    else:
        print("|" * n)