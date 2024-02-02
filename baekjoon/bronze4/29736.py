a, b = map(int, input().split())
k, x = map(int, input().split())

counter = 0
for i in range((k - x), (k + x + 1)):
    if i >= a and i <= b:
        counter += 1
        
if counter > 0:
    print(counter)
else:
    print("IMPOSSIBLE")