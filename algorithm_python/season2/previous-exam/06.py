# 무지의 먹방 라이브 (316p, 513p)

'''
먹방 찍으려고 함. 회전판에 먹어야할 음식 n개 있음
회전판은 번호가 증가하는 순서대로 음식을 가져옴
마지막 번호 음식을 먹으면 다시 1번 음식으로
음식 하나를 1초동안 먹고 다음 음식을 섭취
회전판이 다음 음식을 가져오는 시간은 없다고 가정
먹방시작한지 k초 후 네트워크 장애로 방송 중단
네트워크 정상화 후 다시 방송을 이어갈 때 몇 번 음식부터 먹어야 하는가?

food_times : 음식을 먹는데 필요한 시간이 음식의 순서대로 들어 있는 배열
k : 방송이 중단된 시간
더 섭취해야 음식이 없으면 -1 반환
'''

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:  # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    
    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 시간
    length = len(food_times)  # 남은 음식 개수

    # sum_value + (현재음식시간 - 이전음식시간) * 현재음식개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1  # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    result = sorted(q, key = lambda x: x[1])  # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) * length][1]