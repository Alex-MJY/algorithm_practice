array = []
for _ in range(4):
    array.append(int(input()))

if array[0] < array[1] < array[2] < array[3]:
    print("Fish Rising")
elif array[0] > array[1] > array[2] > array[3]:
    print("Fish Diving")
elif array[0] == array[1] == array[2] == array[3]:
    print("Fish At Constant Depth")
else:
    print("No Fish")