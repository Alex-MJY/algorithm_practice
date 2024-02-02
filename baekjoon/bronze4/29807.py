n = int(input())
scores = list(map(int, input().split()))

num = 0

if n ==  5:
    if scores[0] > scores[2]:
        num += ((scores[0] - scores[2]) * 508)
    else:
        num += (abs(scores[0] - scores[2]) * 108)

    if scores[1] > scores[3]:
        num += ((scores[1] - scores[3]) * 212)
    else:
        num += (abs(scores[1] - scores[3]) * 305)
    num += scores[-1] * 707
    

if n == 4:
    if scores[0] > scores[2]:
        num += ((scores[0] - scores[2]) * 508)
    else:
        num += (abs(scores[0] - scores[2]) * 108)

    if scores[1] > scores[3]:
        num += ((scores[1] - scores[3]) * 212)
    else:
        num += (abs(scores[1] - scores[3]) * 305)
    
print(num * 4763)