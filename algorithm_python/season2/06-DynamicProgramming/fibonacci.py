# fibonacci : recursive
d = [0] * 100  # memoization list

def fibonacci(x):
    print("f(" + str(x) + ")", end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibonacci(x - 1) + fibonacci(x - 2)
    return d[x]
    # return fibonacci(x - 1) + fibonacci(x - 2)

print(fibonacci(6))


# fibonacci : iterative
d2 = [0] * 100
d2[1] = 1
d2[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
    
print(d2[n])