import sys
input = sys.stdin.readline

p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())

if (p1 + p2) > (s1 + s2):
    print("Persepolis")
elif (p1 + p2) < (s1 + s2):
    print("Esteghlal")
else:
    if s1 == p2:
        print("Penalty")
    elif p2 > s1:
        print("Persepolis")
    else:
        print("Esteghlal")