# mine
def solution(numbers):
    arr = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            arr.append(numbers[i] + numbers[j])
    arr = sorted(list(set(arr)))
    return arr


# print(solution([2,1,3,4,1]))
print(solution([5, 0, 2, 7]))


# book
def solution(numbers):
    ret = []  # ➊ 빈 배열 생성
    # ➋ 두 수를 선택하는 모든 경우의 수를 반복문으로 구함
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # ➌ 두 수를 더한 결과를 새로운 배열에 추가
            ret.append(numbers[i] + numbers[j])
        # ➍ 중복된 값을 제거하고, 오름차순으로 정렬
        ret = sorted(set(ret))
        return ret  # ➎ 최종 결과 반환
