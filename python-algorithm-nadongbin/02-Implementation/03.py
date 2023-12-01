# 왕실의 나이트
'''
input : 
- 첫째 줄에 8*8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다. 입력 문자는 a1처럼 열과 행으로 이뤄진다.
- (수평으로 두 칸 이동뒤 수직으로 한 칸 이동 / 수직으로 두 칸 이동 뒤 수평으로 한 칸 이동만 가능))

output : 
- 첫째 줄에 나이트가 이동할 수 있는 모든 경우의 수를 출력하시오.
'''

input_data = input() # ex) a1
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1   # ord() : 유니코드로 캐스팅

# 나이트가 이동할 수 있는 8가지 방향
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

# 방향 이동 가능한지 체크
result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_column >= 1 and next_row <= 8 and next_column <= 8:
        result += 1
    
print(result)