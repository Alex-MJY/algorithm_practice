arr = list(map(int, input().split()))
arr.sort()
dic = {
    'A' : arr[0],
    'B' : arr[1],
    'C' : arr[2],
}
alph = str(input())


print(f"{str(dic[alph[0]])} {str(dic[alph[1]])} {str(dic[alph[2]])}")
