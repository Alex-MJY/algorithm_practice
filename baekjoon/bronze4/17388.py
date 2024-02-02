s, k, h = map(int, input().split())
if (s + k + h) >= 100:
    print("OK")
else:
    uni = min(s, k, h)
    if uni == s:
        print("Soongsil")
    elif uni == k:
        print("Korea")
    elif uni == h:
        print("Hanyang")