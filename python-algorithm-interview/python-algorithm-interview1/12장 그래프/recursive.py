# https://thebook.io/080200/ch01/

def factorial(n):
    if n <= 0:
        return 1
    return factorial(n-1)*n

# for i in range(1, 6):
#     print(factorial(i))
    
# 1) 언제 어떤 매개변수를 가지고 호출할지 정해야 하고, 2) 호출을 정지시켜 줄 기저 사례가 필요하다.


# 함수가 호출되면 내부에 스택 프레임이라는 공간이 생긴다. 이곳엔 함수 실행에 필요한 지역 변수들이 할당된다.

def add_two(a, b):
    c = a + b
    return c

# a, b = 10, 20
# result = add_two(a, b)
# print(result)

'''
add_two 함수를 호출하면 내부적으로 스택 프레임이라는 내부 공간이 생기고, 그 공간에 add_two 내부에 있는
매개변수 a와 b, 결과를 담을 지역 변수 c가 저장된다.
함수가 종료되면 스택 프레임도 같이 사라진다.
호출을 끝낼 제약 사항(기저 사례)을 정하지 않으면 계속해서 변수가 저장되고 스택 프레임은 제한된 메모리 크기를 가졌기 때문에
Recursive Depth Error가 난다. == stack overflow

재귀 함수를 스택 프레임 관점에서 보면, 상태 정보를 가지고 있는 지역 변수는 서로 다른 프레임에 저장된다.
함수 내에서 자기를 호출하더라도, 같은 기능의 코드를 실행하는 것일 뿐, 실행 결과는 서로 다른 스택 프레임에 있는 지역 변수에 저장된다.  
'''

# 순열을 재귀함수로 구현하기
# permutation({1,2,3})
# 부분문제 1 : 1을 출력 후 permutation({2,3})
# 부분문제 2 : 2을 출력 후 permutation({1,3})
# 부분문제 3 : 3을 출력 후 permutation({1,2})
# 12{3}, 13{2}, 21{3}, 23{1}, 31{2}, 32{1} 
# 총 6개의 스택 프레임이 생긴다.

def permutation(arr: list, start: int):
    if len(arr) - 1 == start:
        print(arr)
        return
    
    for idx in range(start, len(arr)):
        arr[start], arr[idx] = arr[idx], arr[start]
        permutation(arr, start+1)
        arr[start], arr[idx] = arr[idx], arr[start]
        
arr = [1,2,3]
permutation(arr, 0)