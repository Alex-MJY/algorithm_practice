'''
n개의 공부 계획. i번째 공부 계획을 실행하는데 Ti시간 소모.
계획 사이에 8시간 휴식.

n개의 계획을 마친 후 지금의 시간이 첫 번째 공부 계획을 시작한 시간으로부터
얼마나 지났는지?

일과 시단단위로 출력
'''
n = int(input())
array = list(map(int, input().split()))

total = sum(array) + (len(array) - 1) * 8

print(total // 24, total % 24)