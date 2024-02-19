'''
마을의 우체부, 우유배달원, 신문배달원은 
상근이네 집에 사나운 개 두마리가 있어서 가기 싫어함. 
그러나 개들의 행동은 예측 가능.
매일 아침, 개 한마리는 a분동안 공격적, b분동안 쉼.
다른 개는 c분동안 공격적, d분동안 쉼.
이 행동을 반복.
우체부, 신문, 우유배달원의 도착 시간이 주어졌을 때 몇 마리에게 공격을 받는
프로그램 작성.

2 2 3 3
1 3 4
'''

a, b, c, d = map(int, input().split())
arr = list(map(int, input().split()))

for n in arr:
    attacked = 0
    if 0 < n % (a + b) <= a:
        attacked += 1
    if 0 < n % (c + d) <= c:
        attacked += 1
print(attacked)