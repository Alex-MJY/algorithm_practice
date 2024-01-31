a, b = map(int, input().split())



if a != 0 and b != 0 and (a + b) % 2 == 0:
    print(f"Even {a * b}")
elif a != 0 and b != 0 and (a + b) % 2 != 0:
    print(f"Odd {a * b}")
elif a == 0 and b == 0:
    print("Not a moose")
    