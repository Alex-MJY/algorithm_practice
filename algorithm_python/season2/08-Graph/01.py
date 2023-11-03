"""
팀 결성 :
학생들에게 0부터 N번까지의 번호 부여. 처음엔 모든 학생이 구분되어 N+1개의 팀 존재
선생은 '팀 합치기 연산'과 '같은 팀 여부 확인 연산' 가능
M개의 연산을 수행할 때, '같은 팀 여부 확인 연산'에 대한 연산 결과를 출력하시오
"""
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, v + 1):
    parent[i] = i
    
for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("Yes")
        else:
            print("No")