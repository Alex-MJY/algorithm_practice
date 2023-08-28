#  배열 a에서 가장 작은 원소와 b의 가장 큰 원소들과 스왑

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split())) 

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))