'''
현재 (x,y). 직사각형은 각 변이 좌표축에 평행, 왼쪽 아래 꼭짓점은 (0,0), 
오른쪽 위 꼭짓점은 (w, h). 경계선까지 가는 거리의 최솟값은?
'''

x, y, w, h = map(int, input().split())

print(min((abs(w - x)), (abs(h - y)), x, y))