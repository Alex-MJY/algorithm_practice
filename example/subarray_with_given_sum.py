# https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

'''
난도가 낮은 것으로 되어 있는데, 쉽지 않다. 이중 반복문을 이용하면 쉽게 찾을 수 있지만, 
조건을 보면 시간 복잡도는 O(n)이고 공간 복잡도는 O(1)이다. 
쉽게 말해서 이중 반복문을 쓰지 말고 풀라는 얘기다.

'''

def find_sub_array1(arr: list[int], s: int):
    for i in range(len(arr)):
        sub_total= 0
        for j in range(i, len(arr)):
            sub_total += arr[j]
            if sub_total == s:
                return [i + i, j + 1]
    return [-1]

# test code
# sample1 = ([1, 2, 3, 7, 5], 12)
# sample2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
# for arr, s in (sample1, sample2):
#     print(find_sub_array1(arr, s))



# two pointer
def find_sub_array2(arr, s):
    left = 0
    sub_total = 0
    for right in range(len(arr)):
        sub_total += arr[right]
        while left < right and sub_total > s:
            sub_total -= arr[left]
            left += 1
        if sub_total == s:
            return [left + 1, right + 1]
    return [-1]

# test code
# sample1 = ([1, 2, 3, 7, 5], 12)
# sample2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
# sample3 = ([1, 2, 3, 4], 0)
# for arr, s in (sample1, sample2, sample3):
#     print(find_sub_array2(arr, s))