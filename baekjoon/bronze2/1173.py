'''
운동을 하는 과정은 1분 단위. 매 분마다 운동과 휴식 중 하나를 선택.
운동을 할 경우 맥박이 T만큼 증가. 맥박이 X였다면 1본 후 맥박은 X + T.
맥박이 M보다 낮을 경우에만 운동 가능. 휴식을 할 경우 R만큼 맥박 감소. 맥박은 m보다 낮으면 안됨. X-R이 m보다 작으면 맥박은 m이 됨.
초기 맥박은 m. 운동은 N분 하려고 함. 이때 필요한 시간의 최솟값은? (운동하는 시간은 연속되지 않아도 됨.)
만약 운동을 N분 할 수 없다면 -1 출력.
'''

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, m, M, T, R = map(int, input().split())
    cnt = time = 0
    now = m
    while cnt < N:
        if m + T > M:
            break
        if now + T <= M:
            now += T
            cnt += 1
        else:
            now = max(now-R, m)  # m보다 작으면 m이 default
        time += 1
    print(time if cnt == N else -1)