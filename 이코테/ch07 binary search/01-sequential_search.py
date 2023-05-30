# 순차 탐색

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1
        
n = int(input("생성할 원소의 개수를 입력하세요 : "))
target = str(input("찾고자 하는 문자열을 입력하세요 : "))
array = input().split()

print(sequential_search(n, target, array))