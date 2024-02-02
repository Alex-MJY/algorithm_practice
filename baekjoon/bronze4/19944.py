'''
new = 1, 2
old = n 이하, 뉴비가 아님
tlt = new, old가 아님
'''

n, m = map(int, input().split())
if m == 1 or m == 2:
    print("NEWBIE!")
elif m <= n and 2 < m:
    print("OLDBIE!")
else:
    print("TLE!")
    