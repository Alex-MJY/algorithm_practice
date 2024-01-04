from string import ascii_lowercase
al_list = list(ascii_lowercase)
n_list = [-1] * len(al_list)

s = str(input())
for i in s:
    idx = s.index(i)
    n_list[al_list.index(i)] = idx

for i in n_list:
    print(i, end=' ')