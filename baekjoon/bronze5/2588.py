a = int(input())
b = list(input())
b.reverse()


array = []
x = 1
for i in b:
    print(int(i) * a)
    array.append(int(i) * a * x)
    x *= 10
    
print(sum(array))