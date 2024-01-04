list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

score1 = (list1[0] * 6) + (list1[1] * 3) + (list1[2] * 2) + (list1[3]) + (list1[4] * 2)
score2 = (list2[0] * 6) + (list2[1] * 3) + (list2[2] * 2) + (list2[3]) + (list2[4] * 2)

print(score1, score2)