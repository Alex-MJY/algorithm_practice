def bubble_sort(a):
    for i in range(1, len(a)):
        for j in range(0, len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                

# def quick_sort(a, lo, hi):
#     def partition(lo, hi):
#         pivot = a[hi]
#         left = lo
#         for right in range(lo, hi):
#             if a[right] < pivot:
#                 a[left], a[right] = a[right], a[left]
#                 left += 1
#         a[left], a[hi] = a[hi], a[left]
#         return left
    
#     if lo < hi:
#         pivot = partition(lo, hi)
#         quick_sort(a, lo, pivot-1)
#         quick_sort(a, pivot+1, hi)

def quicksort1(x):
    if len(x) <= 1:
        return x
    
    pivot = x[len(x) // 2]
    less, more, equal = [], [], []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)
            
    return quicksort1(less) + equal + quicksort1(more)


# cache없는 퀵소트
def partition(arr, start, end):
    pivot = arr[start]
    left  = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right  and pivot <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] == arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right

def quicksort2(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quicksort2(arr, start, pivot-1)
        quicksort2(arr, pivot+1, end)
    return arr