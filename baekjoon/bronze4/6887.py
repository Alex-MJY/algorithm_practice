num = int(input())
counter = 1
while True:
    if counter ** 2 > num:
        break
    counter += 1
print(f"The largest square has side length {counter - 1}.")