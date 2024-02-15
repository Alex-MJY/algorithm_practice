'''
1 - 9 (3 ** 2)  
2 - 25 (5 ** 2)   
3 - 81 (9 ** 2) 
4 - 289 (17 ** 2)
5 - 1089 (33 ** 2)

(2^n + 1) ^ 2
'''


# n = int(input())
# arr = [0 for i in range(16)]

# b = 1
# a = 2
# for i in range(1, 16):
#     a += b
#     arr[i] = pow(a, 2)
#     b *= 2
# print(arr[n])


# (2^n + 1)^2 
print((2 ** int(input()) + 1) ** 2)