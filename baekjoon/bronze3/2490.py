'''
윷놀이. 네 개의 윷짝을 던져 배(0)와 등(1)이 나오는 숫자를 세어 도, 개, 걸, 윷, 모 결정.

도(배 한 개, 등 세 개), 
개(배 두 개, 등 두 개), 
걸(배 세 개, 등 한 개), 
윷(배 네 개), 
모(등 네 개)

도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력
'''

# import sys
# input = sys.stdin.readline

for i in range(3):
    array = list(map(str, input().split()))
    count0, count1 = 0, 0
    for j in array:
        if j == '0':
            count0 += 1
        if j == '1':
            count1 += 1
    
    if count0 == 1 and count1 == 3:
        print('A')
    if count0 == 2 and count1 == 2:
        print('B')
    if count0 == 3 and count1 == 1:
        print('C')
    if count0 == 4 and count1 == 0:
        print('D')
    if count0 == 0 and count1 == 4:
        print('E')