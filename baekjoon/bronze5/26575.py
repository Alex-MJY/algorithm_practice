# n = int(input())
# array = []
# for i in range(n):
#     d, f, p = map(float, input().split())
#     total = d * f * p
#     array.append(total)

# for i in array:
#     print(f"${i:.2f}")
    


# for i in[*open(0)][1:]:print(f"${eval(i.replace(' ','*')):.2f}")


for i in range(int(input())):
    d, f, p = map(float, input().split())
    print(f"${d * f * p:.2f}")