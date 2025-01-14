def solution(arr):
    arr = sorted(list(set(arr)), reverse=True)
    # arr = list(set(arr))
    return arr


def solution2(lst):
    unique_lst = list(set(lst))  # ➊ 중복값 제거
    unique_lst.sort(reverse=True)  # ➋ 내림차순 정렬
    return unique_lst
