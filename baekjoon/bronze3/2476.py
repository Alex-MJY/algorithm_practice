'''
주사위 3개.
1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  
'''

import sys
input = sys.stdin.readline

# array = []
# for i in range(int(input())):
#     li = list(map(int, input().split()))
#     if len(set(li)) == 3:
#         array.append(max(li) * 100)
#     elif len(set(li)) == 2:
#         array.append(sorted(li)[1] * 100)
#     elif len(set(li)) == 1:
#         array.append((li[0] * 1000) + 10000)
# print(max(array))


maxMoney = 0
for i in range(int(input())):
    a,b,c = map(int, input().split())
    if a == b == c :
        maxMoney = max(maxMoney, 10000+a*1000)
    elif a == b:
        maxMoney = max(maxMoney, 1000+a*100)
    elif a == c:
        maxMoney = max(maxMoney, 1000+a*100)
    elif b == c:
        maxMoney = max(maxMoney, 1000+b*100)
    else :
        maxMoney = max(maxMoney, max(a,b,c)*100)
        
print(maxMoney)