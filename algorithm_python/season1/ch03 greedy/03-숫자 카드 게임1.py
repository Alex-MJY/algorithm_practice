'''
여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 잦을 뽑는 게임.
조건1. 카드들이 N * M 형태로 놓여 있다. (N은 행의 개수, M은 열의 개수)
조건2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택.
조건3. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
조건4. 따라서 처음에 카드를 골라낼 행을 선택할 때 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려해서 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 해야한다.


아이디어 : 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수
'''

n, m = map(int, input().split())

result =  0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)