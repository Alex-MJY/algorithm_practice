'''
1 2 3
3 2 1
2 3 1
2 1 3
3 1 2

1 2 3
2 1 3
2 3 1

1 2 3
1 3 2
3 1 2
2 1 3
1 2 3
3 2 1
'''


li = [1, 2, 3]

for i in range(int(input())):
    x, y = map(int, input().split())
    xx = li.index(x)
    yy = li.index(y)
    li[xx], li[yy] = li[yy], li[xx]
    
print(li[0])
