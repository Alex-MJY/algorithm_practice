'''
세 수를 서로 나누었을 때 나머지가 같으려면 세 수가 모두 같아야 한다.
'''
for i in range(int(input())):
    a, b, c = map(int, input().split())
    print(min(a, b, c))