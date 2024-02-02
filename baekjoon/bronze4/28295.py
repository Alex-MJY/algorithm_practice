'''
학생들 초기에 북쪽 바라보고있음. 열 번의 지시를 내림(우향우, 뒤로돌아, 좌향좌)
1 = 우향우
2 = 뒤로 돌아
3 = 좌향좌

마지막 방향이 북:N, 동:E, 서:W, 남:S
'''

# start = 0
# for i in range(10):
#     n = int(input())
#     if n == 1:
#         start += 90
#     if n == 2:
#         start += 180
#     if n == 3:
#         start -= 90


direction = ["N", "E", "S", "W"]
result = "N"

for i in range(10):
    command = int(input())
    if command == 1:
        result = direction[(direction.index(result) + 1) % 4]
    elif command == 2:
        result = direction[(direction.index(result) + 2) % 4]
    elif command == 3:
        result = direction[(direction.index(result) + 3) % 4]
print(result)