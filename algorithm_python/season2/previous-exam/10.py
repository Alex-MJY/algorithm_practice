# 자물쇠와 열쇠 (p325, p518)

'''
자물쇠와 열쇠 있음
자물쇠는 격자 한 칸의 크기가 1x1인 NxN 크기의 정사각형 격자 형태, 열쇠는 MxM크기인 정사각 격자 형태
자물쇠는 홈이 파여있고 열쇠도 홈과 돌기부분이 있다. 열쇠는 회전 가능하며, 돌기 부분을 자물쇠의 홈 부분에 맞게 채워야 한다.
열쇠의 돌기와 자물쇠의 돌기가 만나면 안되고, 자물쇠의 모든 홈이 열쇠의 돌기로 채워져 있어야 한다.
열쇠 = key, 자물쇠 = lock / 둘 다 2차원 배열 / 자물쇠를 열 수 있음 true 없으면 false를 return
'''
# 문제에서 제시한 자물쇠와 열쇠의 크기는 20X20보다 작기 때문에 리스트에 있는 모든 원소에 접근할 때 400만큼이 필요
# 완전 탐색을 이용해 전부 시도해도 괜찮은 크기
# 자물쇠 크기보다 큰 리스트를 생성하고 중앙에 자물쇠르 위치 시킨다
# 열쇠배열은 왼쪽 위부터 시작해서 한 칸씩 이동하는 방식으로 자물쇠의 모든 홈을 채울 수 있는 확인한다
# 효율적인 풀이를 위해 열쇠를 돌리는 함수와 자물쇠의 중각 부분이 모두 1인지 확인하는 함수를 따로 분기하여 만든다


# 2차원 리스트 90도 회전
def rotate_matrix(a):
    n = len(a)  # 행 길이
    m = len(a[0])  # 열 길이
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * n for _ in range(n * 3)]  # 자물쇠의 크기를 기존의 3배로 변환
    for i in range(n): # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
            
    for rotation in range(4):  # 4가지 방향 확인
        key = rotate_matrix(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):  # 자물쇠에서 열쇠를 다시 빼기
                    for j in range(m):
                        new_lock[x + i][y + i] -= key[i][j]
        return False