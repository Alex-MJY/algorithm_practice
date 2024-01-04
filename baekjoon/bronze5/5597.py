array = [0] * 30
    
for i in range(28):
    n = int(input())
    array[n - 1] = "yes"

for i in range(30):
    if array[i] == 0:
        print(i + 1)