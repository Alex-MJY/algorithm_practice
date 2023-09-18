# 부품 찾기
'''
n = 5
[8, 3, 7, 9, 2]

m = 3
[5, 7, 9]

각 부품이 존재하면 yes, 없으면 no를 출력
'''

# 이진 정렬
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())  # inventory
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split())) # customer orders

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print("yes", end= " ")
    else:
        print("No", end = " ")