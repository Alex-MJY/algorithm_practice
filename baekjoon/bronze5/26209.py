bits = list(map(int, input().split()))

counter = 0

for i in bits:
    if i == 0 or i == 1:
        continue
    else:
        counter += 1

if counter == 0:
    print("S")
else:
    print("F")