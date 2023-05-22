'''
왕실 정원은 체스판과 같은 8x8 좌표 평면이다. 특정한 한 칸에 나이트가 서 있다.
나이트는 두 가지 경우로 움직일 수 있다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동

나이트의 위치가 주어졌을 때 이동할 수 있는 경우의 수를 출력하는 프로그램을 만들어라.

행 위치는 1~8, 열 위치는 a~h로 나타낸다. 정원의 밖으로는 이동할 수 없다.
'''
# input = a1

input_data = input()
column = int(ord(input_data[0])) - int(ord('a')) + 1
row = int(input_data[1])

# 이동할 수 있는 8가지 방향
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1
        
print(result)