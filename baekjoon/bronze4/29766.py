s = str(input())
counter = 0
for i in range(len(s) - 3):
    if s[i] == 'D':
        if s[i + 1] == 'K':
            if s[i + 2] == 'S':
                if s[i + 3] == 'H':
                    counter += 1
print(counter)