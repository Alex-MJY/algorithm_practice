'''
지폐는 모두 네 종류. 세로의 길이는 68로같지만 가로의 길이는 모두 다르다.
천원 : 136, 오천원 : 142, 만원 : 148, 오만원 : 154
수민이는 지폐 n장을 갖고 있다. 

'''
money = {
    136 : 1000,
    142 : 5000,
    148 : 10000,
    154 : 50000
}
counter = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    counter = money[a]
print(counter)