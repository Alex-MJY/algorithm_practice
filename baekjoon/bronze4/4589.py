n = int(input())
result = []
for i in range(n):
    array = list(map(int, input().split()))
    if array == sorted(array) or array == sorted(array, reverse=True):
        result.append("Ordered")
    else:
        result.append("Unordered")
        
print("Gnomes:")
for i in result:
    print(i)