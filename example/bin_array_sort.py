def bin_array_sort1(arr):
    arr[:] = [0] * arr.count(0) + [1] * arr.count(1)

# Test Code
# for arr in ([1, 0, 1, 1, 1, 1, 1, 0, 0, 0], [1, 1]):
#     bin_array_sort1(arr)
#     print(arr)
    
    
    
def bin_array_sort2(arr: list[int]) -> None:
    """0과 1로 이루어진 배열 arr를 오름차순으로 정렬한다.
    Arguments:
        arr (list[int]): 0과 1로 이루어진 배열
    Return:
        None: 배열 arr 자체를 정렬한다.
    """
    left: int = 0
    right: int = len(arr) - 1
    while left < right:
        while left < len(arr) and arr[left] == 0:
            left += 1
        while right >= 0 and arr[right] == 1:
            right -= 1
        if left < right:
            arr[left], arr[right] = 0, 1
            left, right = left + 1, right - 1


# Test Code 
# for arr in ([1, 0, 1, 1, 1, 1, 1, 0, 0, 0], [1, 1]):  
#     bin_array_sort2(arr)  
#     print(arr)