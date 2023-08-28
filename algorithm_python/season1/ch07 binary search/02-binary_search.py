def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)
    else:
        return binary_search_recursive(array, target, mid + 1, end)
    
    
def binary_search_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
    
n = int(input("생성할 원소의 개수를 입력하세요 : "))
target = str(input("찾고자 하는 문자열을 입력하세요 : "))
array = list(map(int, input().split()))

result = binary_search_recursive(array, target, 0, n - 1)

if result == None:
    print("element dosne't exist")
else:
    print(result + 1)