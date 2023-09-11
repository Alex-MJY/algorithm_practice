# 두 배열의 원소 교체
'''
배열 a,b 두개가 있고, n개의 원소로 구성(모두 자연수). 
최대 k번의 바꿔치기 가능. 목표는 a의 모든 원소의 합이 최대가 되도록.
'''

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
    
count = 0
for i in a:
    count += i
    
print(count)