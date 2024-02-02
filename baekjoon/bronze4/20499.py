s = str(input())
k, d, a = s.split('/')

if int(k) + int(a) < int(d) or int(d) == 0:
    print("hasu")
else:
    print("gosu")
