# alphabet_dict = {
#     'A' : 2, 'B' : 2, 'C' : 2, 
#     'D' : 3, 'E' : 3, 'F' : 3, 
#     'G' : 4, 'H' : 4, 'I' : 4, 
#     'J' : 5, 'K' : 5, 'L' : 5, 
#     'M' : 6, 'N' : 6, 'O' : 6, 
#     'P' : 7, 'Q' : 7, 'R' : 7, 'S' : 7, 
#     'T' : 8, 'U' : 8, 'V' : 8, 
#     'W' : 9, 'X' : 9, 'Y' : 9, 'Z' : 9,
# }

# result = 0
# s = str(input())
# s = list(s)
# for i in s:
#     result += (alphabet_dict[i] + 1)
# print(result)

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = list(input())
result = 0
for i in word:
    for j in dial:
        if i in str(j):
            result += dial.index(j) + 3
print(result)