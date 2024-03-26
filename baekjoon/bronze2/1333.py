'''
노래가 N곡, 노래 길이 L초, 노래 사이에 5초 공백
노래 시작부터 전화벨 울림. D초에 한번씩 울리고 1초간 울림.
'''

n, l, d = map(int, input().split())
check_array = [False] * ((n * l) + (5 * (n - 1)))

for i in range(n):
    s = (l + 5) * i
    for j in range(s, s + l):
        check_array[j] = True

answer = 0
while answer < len(check_array):
    if not check_array[answer]:
        break
    answer += d
print(answer)