import sys

# for i in range(3):
#     counter = 0
#     for j in range(int(sys.sdin.readline())):
#         n = int(sys.sdin.readline())
#         counter += n
#     if counter == 0:
#         print("0")
#     elif counter > 0:
#         print("+")
#     else:
#         print("-")

for _ in range(3):
    array = [int(sys.stdin.readline()) for i in range(sys.stdin.readline())]
    if sum(array) == 0:
        print("0")
    elif sum(array) > 0:
        print("+")
    else:
        print("-")