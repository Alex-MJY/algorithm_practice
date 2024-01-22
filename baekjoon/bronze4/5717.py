while True:
    male, female = map(int, input().split())
    if male == 0 and female == 0:
        break
    print(male + female)