vowel = ['a', 'e', 'i', 'o', 'u']
s = str(input())
counter = 0
for i in s:
    if i in vowel:
        counter += 1
print(counter)