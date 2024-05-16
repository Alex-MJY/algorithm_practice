import sys
input = sys.stdin.readline

count, price = map(int, input().split())

result = [0, 0, 0] # 0번 총합, 1번 베드룸, 2번 곱한값
result_balcony = 0

for i in range(count):
    num, area = map(str, input().split())
    if area == "balcony":
        result_balcony += int(num) / 2
    else:
        result_balcony += int(num)
    result[0] += int(num)
    if area == "bedroom":
        result[1] += int(num)
result[2] = price * result_balcony

for i in result:
    print(i)  
    