'''
OX문제. 앞에가 틀리고 다음이 맞으면 1점, 두개 연속으로 맞으면 2점, 세개 연속으로 맞으면 3점...
틀린 문제는 0점.
OX문제에서 답이 맞으면 1, 틀린 경우는 0.
총점을 계산하는 프로그램 작성.
'''

import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))

counter = 0
check = 0
for i in range(len(scores)):
    if scores[i] == 0:
        check = 0
    if scores[i] == 1:
        counter += (check + 1)
        check += 1
print(counter)