array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort1(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    
    pivot = start  # 첫 번째 원소를 피봇으로 설정
    left = start + 1
    right = end
    
    while left <= right:
        # 피봇보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피봇보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 피봇을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
            
    # 분할 이후 왼쪽 부분과 오른쪽 부분 각각 정렬 수행
    quick_sort1(array, start, right - 1)
    quick_sort1(array, right + 1, end)
    
quick_sort1(array, 0, len(array) - 1)
print(array)


# pythonic quick sort
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort2(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:] # pivot을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분 
    right_side = [x for x in tail if x >= pivot]  # 분할된 오른쪽 부분
    
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))