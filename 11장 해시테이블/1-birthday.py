'''
여러 사람이 모였을 때 생일이 같은 2명이 존재할 확룰은 비둘기집 원리에 따라 366명이 모여야 일어나는 일 같다.
그러나 실제론 23명만 모여도 50%를 넘고, 57명이 모이면 그때부터는 90%를 넘어선다.
아래와 같이 계산 코드를 작성해서 직접 실험해보자
'''


import random

TRIALS = 100000 # 10만 번 실험
same_birthdays = 0 # 생일이 같은 실험의 수

for _ in range(TRIALS):
    birthdays = []
    # 23명이 모였을 때, 생일이 같은 경우 same_birthdays += 1
    for i in range(23):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

# 전체 10만 번 실험 중 생일이 같은 실험의 확률
print(f'{same_birthdays / TRIALS * 100}%')
