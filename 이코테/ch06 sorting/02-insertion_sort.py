# 삽입정렬은 선택 정렬보다 효율적이다.
# 필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬'되어 있을 때 훨씬 효율적이다. (이 경우 퀵 정렬보다 효율적이다.)
# 정렬이 이루어진 원소는 항상 오름차순을 유지하고 있다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)