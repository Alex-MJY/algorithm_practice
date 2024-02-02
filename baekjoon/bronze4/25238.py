a, b = map(int, input().split()) # 몬스터 방어율 수치, 방무

a = a - (a * (b * 0.01))
if a >= 100:
    print(0)
else:
    print(1)
