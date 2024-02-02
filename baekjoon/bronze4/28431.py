import collections

dic = collections.defaultdict(int)
for i in range(5):
    n = int(input())
    dic[n] += 1

for i in dic.items():
    if i[1] % 2 != 0:
        print(i[0])