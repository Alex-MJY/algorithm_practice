import sys
input = sys.stdin.readline

next_month = int(input())
this_month = int(input())

if next_month <= this_month + 60:
    print((next_month) * 1500)
else:
    print(((this_month + 60) * 1500) + (next_month - (this_month + 60)) * 3000)