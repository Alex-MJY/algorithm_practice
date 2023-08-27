# 병합 정렬 알고리즘과 더불어 가장 많이 사용된다. 
# 피봇을 설정하고 큰수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작.
# 평균 시간복잡도는 O(n log n) 이지만 최악의 경우 O(n^2)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # element가 1개인 경우 종료
        return
    
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
            
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
            
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    
quick_sort(array, 0, len(array) - 1)
print(array)