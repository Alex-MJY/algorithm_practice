'''
n개의 문제 후보마다 m명의 출제위원이 찬반 의견을 내고, 과반수의 찬성을 얻은 문제가 출제.
m은 항상 홀수.
출제될 문제의 수를 구하라.
'''
n, m = map(int, input().split())
counter = 0
for i in range(n):
    yes = 0
    no = 0
    for j in str(input()):
        if j == 'O':
            yes += 1
        if j == 'X':
            no += 1
    if yes > no:
        counter += 1
print(counter)