a = int(input()) # 고기의 온도
b = int(input()) # 목표 온도
c = int(input()) # 얼어있는 고기를 1도 데우는 데 걸리는 시간
d = int(input()) # 얼어있는 고기를 해동하는 데 걸리는 시간
e = int(input()) # 얼어있지 않은 고기를 1도 데우는 데 걸리는 시간

# output : 고기를 b도로 데우는 데 걸리는 시간을 초단위로 출력


while a < b:
    if a > 0:
        print((b - a) * e)
        break
    if a < 0:
        print((b * e) + abs(a * c) + d)
        break
    else:
        print((b - a) * e) + d        