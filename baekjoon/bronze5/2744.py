s = str(input())
string = []
for i in s:
    if i.isupper():
        i = i.lower()
    elif i.islower():
        i = i.upper()
    string.append(i)
print(''.join(string))