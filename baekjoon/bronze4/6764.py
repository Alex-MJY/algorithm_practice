array = []
for i in range(4):
    n = int(input())
    array.append(n)


if len(set(array)) != 1 and array == sorted(array):
    print("Fish Rising")
elif len(set(array)) != 1 and array == sorted(array, reverse=True):
    print("Fish Diving")
elif len(set(array)) == 1:
    print("Fish At Constant Depth")
else:
    print("No Fish")