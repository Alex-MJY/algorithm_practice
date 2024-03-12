import sys
import collections

input = sys.stdin.readline


dic = collections.defaultdict(int)

for _ in range(int(input())):
    s = str(input())
    dic[s[0]] += 1
    
result = [k for k, v in dic.items() if v >= 5]
if len(result) == 0:
    print("PREDAJA")
else:
    print(''.join(sorted(result)))