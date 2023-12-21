# runtime error
# import collections

# s = str(input()).upper()

# if len(s) == 1:
#     print(s)
# else:
#     s_dic = collections.defaultdict(int)
#     for i in s:
#         s_dic[i] += 1
    
#     s_dic = sorted(list(s_dic.items()), key=lambda x: x[1])
#     if s_dic[-1][1] == s_dic[-2][1]:
#         print("?")
#     else:
#         print(s_dic[-1][0])

word = input().upper()
word_list = list(set(word))
counter = []

for i in word_list:
    counter.append(word.count(i))
if counter.count(max(counter)) >= 2:
    print("?")
else:
    print(word_list[counter.index(max(counter))])