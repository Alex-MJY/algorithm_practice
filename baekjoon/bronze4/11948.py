n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())


n5 = int(input())
n6 = int(input())


array = [n1, n2, n3, n4]
array.sort()
array.pop(0)
print(sum(array) + max(n5, n6))