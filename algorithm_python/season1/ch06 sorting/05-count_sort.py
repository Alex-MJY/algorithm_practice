# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘.
# 모든 데이터가 양수일 경우, 데이터 개수가 n, 최대값이 k일 때, 최악의 경우에도 O(n + k)를 보장.
# 데이터의 크기 범위가 제한되어 정슈 형태로 표현할 수 있을 때만 사용 가능. (float의 경우 불가능)
# 데이터가 0과 999.999일 경우에도 리스트의 크기가 100만개가 되기 때문에 비효율적이다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')