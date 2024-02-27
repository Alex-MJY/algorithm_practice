'''
마법거울은 매일 자신의 심리상태에 따라 
거울에 비친 공주님의 모습을 좌/우 또는 상/하로 반전시켜 비추기로 한다. 
마법거울의 심리상태는 1부터 3까지의 자연수로 표현할 수 있으며, 
숫자가 클수록 더 화가 난 상태를 의미한다.

마법거울의 심리상태가 
1일 때는 지영 공주님의 모습을 있는 그대로 표현,
2일 때는 좌/우로 반전된 모습을, 
3일 때는 상/하로 반전된 모습을 표현.
'''

import sys
input = sys.stdin.readline

# arr = []
# for _ in range(int(input())):
#     inp = list(input())
#     arr.append(arr)

# n = int(input())
# if n == 1:
#     print(*arr, sep='\n')
# elif n == 2:
#     for i in range(len(arr)):
#         arr[i] = arr[i].reverse()
#     print(*arr, sep='\n')
# elif n == 3:
#     arr = arr.reverse()
#     print(*arr, sep='\n')

arr = [input().rstrip() for _ in range(int(input()))]
n = int(input())

if n == 1:
    print(*arr, sep='\n')
elif n == 2:
    print(*[i[::-1] for i in arr], sep='\n')
elif n == 3:
    print(*arr[::-1], sep='\n')