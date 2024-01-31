s = str(input())
if len(s) == 2:
    print(int(s[0]) + int(s[1]))
if len(s) == 3:
    print(int(s[0:2]) + int(s[2]))
if len(s) == 4:
    print(int(s[0:2]) + int(s[2:4]))