'''
탁구게임, 둘 다 0점으로 시작해서 n회의 라운드 진행. 
각 라운드마다 승자가 1점 얻음.
n회의 라운드가 끝나거나, 누군가가 2점 이상 앞서면 경기 종료.
윤이는 누가 이길지 예측. 예측이 맞다면 경기가 몇 대 몇으로 끝나나?
'''
x, y = 0, 0 # D, P
for i in range(int(input())):
    if abs(x - y) >= 2:
        break
    winner = str(input())
    if winner == 'D':
        x += 1
    if winner == 'P':
        y += 1

print(f"{x}:{y}")