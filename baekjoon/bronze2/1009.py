# 시간 초과
# import sys
# input = sys.stdin.readline

# for i in range(int(input())):
#     a, b = map(int, input().split())
#     result = a ** b
#     print(str(result)[-1])
'''
끝자리 패턴을 찾아서 패턴별로 다르게 처리
1, 5, 6은 계속 자신과 같은 수 반복

2 : 2, 4, 6, 8
3 : 9, 7, 1
4 : 4, 6
7 : 9, 3, 1
8 : 8, 4, 2, 6
9 : 9, 1

끝자리가 0인 값의 제곱수들인데 0번 컴퓨터는 없으므로 해당 값들은 10번 컴퓨터가 출력되도록 한다.
'''
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))
    
# for i in range(len(arr)):
#     a = arr[i][0] % 10
#     b = arr[i][1]
    
#     if a == 0:
#         print(10)
#     elif a == 1 or a == 5 or a == 6:
#         print(a)
#     elif a == 4 or a == 9:
#         if b % 2 == 0:
#             print((a**2) % 10)
#         else:
#             print(a % 10)
#     elif a == 2 or a == 3 or a == 7 or a == 8:
#         print((a**b) % 10)

n = int(input())
# a의 b 제곱값의 1의 자리 수의 패턴 저장
array = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6, 4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1, 9, 1]]

for _ in range(n):
    # a, b값 입력 받음
    a, b = map(int, input().split())
    # a가 10의 배수일 경우, 10 출력
    if a % 10 == 0:
        print(10)
        continue
    # a % 10이 1, 5, 6일 경우, a % 10 값 출력
    elif a % 10 == 1 or a % 10 == 5 or a % 10 == 6:
        print(a % 10)
        continue
    # b가 0이면 1 출력
    if b == 0:
        print(1)
    # b % 4가 0이면, array에 저장해둔 패턴값 가져옴
    elif b % 4 == 0:
        print(array[a % 10][3])
    else:
        print(array[a % 10][b % 4 - 1])