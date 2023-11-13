# 문자열 재정렬 (p322, p516)

data = input()
letters = []
digits = 0

for i in data:
    if i.isdigit():
        digits += int(i)
    else:
        letters.append(i)
letters.sort()
letters = ''.join(letters)

result =  letters + str(digits)
print(result)