import string
alphabet = list(string.ascii_lowercase)
dic = {}
for i in alphabet:
    dic[i] = 0
s = str(input())
for i in s:
    dic[i] += 1
print(*dic.values())