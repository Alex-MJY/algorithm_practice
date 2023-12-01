# 기둥과 보 설치 (p329, p525)

'''
2차원 가상 벽변에 기둥과 보를 이용한 구조물을 설치 가능. 기둥과 보는 길이 1인 선분으로 표시된다. 벽면은 NxN 크기 정사각 격자 형태.
(조건)
- 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야 한다.
- 보는 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 한다.
기둥과 보를 삭제한 후에도 조건을 만족해야 한다.
벽면의 크기, 기둥과 보를 설치하거나 삭제하는 작업이 담긴 build_frame이 매개변수로 주어질 때 명령을 수행한 후 구조물의 상태를 return하는 solution 함수를 완성해라.

build_frame = [x, y, a, b]
x,y는 기둥, 보를 설치 또는 삭제할 좌표(가로좌표, 세로좌표).
a는 구조물의 종류를 나타낸다 (0은 기둥, 1은 보).
b는 구조물의 설치와 삭제를 나타낸다 (0은 삭제, 1은 설치).

구조물은 좌표 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 / 보는 바닥에 설치 불가능

return하는 배열의 원소는 [x, y, a] 형식
x,y는 기둥,보의 교차점 좌표 / a는 구조물의 종류이며 0은 기둥, 1은 보를 나타낸다.
'''

# 시뮬레이션 문제
# 전체 명령 개수는 총 1000개 이하. 시간 제한이 5초로 넉넉하기 때문에 O(n^3)도 가능
# 가장 간단한 방법은 설치 및 삭제 연산을 요구할 때마다 전체 구조물을 확인하며 규칙을 확인

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False        
        elif stuff == 1:  # 보
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer
                                                                   and [x+1, y, 1] in answer):
                continue
            return False
        return True
    
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:  # 삭제
            answer.remove([x, y, stuff]) # 삭제 시도 후
            if not possible(answer): # 삭제 가능한지 확인
                answer.append([x, y, stuff]) # 삭제 불가능한 구조물이라면 다시 설치
        if operate == 1: # 설치
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)