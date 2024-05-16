'''
0은 구멍 하나랑 타원형 보상
4, 6, 9 구멍 하나
8 구멍 둘
나머지 숫자는 종이를 찢어버림
'''

n = int(input())

if n == 0:
    print(1)
elif n == 1:
    print(0)
elif n % 2 == 0:
    print("8" * (n // 2))
else:
    print("4" + "8" * (n // 2))