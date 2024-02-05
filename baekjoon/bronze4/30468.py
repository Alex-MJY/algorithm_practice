'''
스탯은 네 종류 힘(str), 민첩(dex), 지능(int), 운(luk)
네 가지 스탯 중 하나의 수치를 1씩 올릴 수 있는 축복을 여러 번 사용해 평균 스탯 수치를 n이상으로
마드려고 할 때 최소 몇 번의 축복을 사용해야 하는가?
'''

array = list(map(int, input().split()))
n = array.pop()
counter = 0
total = sum(array)


while True:
    avg = total // len(array)
    if avg >= n:
        break
    total += 1
    counter += 1
print(counter)
    