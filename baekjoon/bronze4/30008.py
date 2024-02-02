n, k = map(int, input().split())
scores = list(map(int, input().split()))


grades = []
for i in scores:
    i = ((i * 100) // n)
    if 0 <= i <= 4:
        grades.append(1)
    elif 4 <= i <= 11:
        grades.append(2)
    elif 11 < i <= 23:
        grades.append(3)
    elif 23 < i <= 40:
        grades.append(4)
    elif 40 < i <= 60:
        grades.append(5)
    elif 60 < i <= 77:
        grades.append(6)
    elif 77 < i <= 89:
        grades.append(7)
    elif 89 < i <= 96:
        grades.append(8)
    elif 96 < i <= 100:
        grades.append(9)

# print(*grades) 
print(" ".join(map(str, grades)))