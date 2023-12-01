# 모험가 길드 (311p, 506p)

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # number of groups
count = 0  # number of members in group

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)