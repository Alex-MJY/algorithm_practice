array = []
for _ in range(3):
    n = int(input())
    array.append(n)
    
if len(set(array)) == 1 and sum(array) == 180:
    print("Equilateral")
elif len(set(array)) == 2 and sum(array) == 180:
    print("Isosceles")
elif len(set(array)) == 3 and sum(array) == 180:
    print("Scalene")
elif sum(array) != 180:
    print("Error")