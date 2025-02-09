def solution(arr):
    arr.sort()
    return arr

# 버블 정렬로 정렬하기
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
    return arr

def do_sort(arr): # sort() 함수로 배열 정렬하기
    arr.sort()
    return arr

def measure_time(func, arr): # 시간을 측정하고 뒤집힌 배열 반환
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    return end_time - start_time, result


arr = list(range(10000))
bubble_time, bubble_result = measure_time(bubble_sort, arr)
print("첫 번째 코드 실행 시간: ", format(bubble_time, ".10f"))

arr = list(range(10000))
reverse_time, reverse_result = measure_time(do_sort, arr)
print("두 번째 코드 실행 시간: ", format(reverse_time, ".10f"))

print("bubble_result == reverse_result: ", bubble_result == reverse_result)