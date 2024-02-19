'''
요리사 다섯명. 음식 각자 하나씩 만들고 서로 다른 사람의 음식 평가.
점수는 1~5점까지. 우승자와 그의 점수를 구하여라.
'''

arr = []
for i in range(5):
    scores = list(map(int, input().split()))
    arr.append([i + 1, sum(scores)])
arr.sort(key= lambda x: x[1])

print(*arr[-1])
    
