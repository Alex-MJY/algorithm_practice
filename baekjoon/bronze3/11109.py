'''
<input>
테스트케이스 개수 t
d, n, s, p 
d는 병렬 버전을 개발하는데 걸리는 시간
n은 다음해 동안 이 프로그램이 실행되는 횟수
s는 직렬버전 p는 병렬버전의 실행 시간

각각의 테스트케이스에 대해 병렬화를 하는게 좋으면 "parallelize" 를 출력
병렬화를 하는게 좋지 않으면 "do not parallelize" 를 출력
직렬화와 병렬화를 통한 시간이 같으면 "does not matter" 를 출력
'''

import sys
input = sys.stdin.readline

for _ in range((int(input()))):
    d, n, s, p = map(int, input().split())
    if d + p * n == n * s:
        print("does not matter")
    elif d + p * n == n * s:
        print("do not parallelize")
    else:
        print("parallelize")