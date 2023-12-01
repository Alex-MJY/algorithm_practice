# 여러 사람이 모였을 때 생일이 같은 2명이 존재할 확률.
# 생일의 가짓수가 365개이므로, 확률이 매우 낮아보이지만 23명만 모여도 50%를 넘고, 57명이 모이면 그때부터 99%를 넘어선다.
# 즉, 일반적인 상식(잘못된 상식)과는 달리, 충돌은 생각보다 쉽게 일어나므로 충돌을 최소화하는 것은 중요하다.

import random

trials = 100000
same_birthdays = 0

for _ in range(trials):
    birthdays = []
    # 23명이 모였을 때, 생일이 같은 경우 same_birthdays += 1
    for i in range(23):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)
        

# 전체 10만 번 실험 중 생일 같은 실험의 확률
print(f'{same_birthdays / trials * 100}%')