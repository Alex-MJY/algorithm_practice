n = int(input())
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(n):
            fact = fact * (i + 1)
        return fact
print(str(factorial(n))[-1])