dic = {
    'black' : [0, 1],
    'brown' : [1, 10],
    'red' : [2, 100],
    'orange' : [3,1000],
    'yellow' : [4, 10000],
    'green' : [5, 100000],
    'blue' : [6, 1000000],
    'violet' : [7, 10000000],
    'grey' : [8, 100000000],
    'white' : [9, 1000000000],
}

fst_line = str(input())
sec_line = str(input())
thr_line = str(input())

result = str(dic[fst_line][0]) + str(dic[sec_line][0])
print(int(result) * dic[thr_line][1])