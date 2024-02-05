'''
관우를 죽인 것같은 n명의 용의자 중 범인을 찾으려고 한다.
범인의 이름에는 s가 들어간다. 
'''
result = []
for i in range(int(input())):
    s = str(input())
    for j in s:
        if j == 'S':
            result += s
print(''.join(result))