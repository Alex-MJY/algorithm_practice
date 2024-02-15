'''
대회 여2 남1. n명의 여학생과 m명의 남학생이 팀원을 찾고 있다. 
k명은 반드시 인턴쉽에 참여해야 한다. 인턴쉽에 참여하면 대회에 참여 못한다.
만들 수 있는 최대의 수?
'''

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

for i in range(k):
    if n // 2 >= m:
        n -= 1
    else:
        m -= 1
print(min(n // 2, m))