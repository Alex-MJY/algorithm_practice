'''
7자리 번호 중 끝 4자리는 특징이 있음
1. 네 자리 중 첫 번째 숫자는 8 또는 9
2. 마지막 숫자는 8 또는 9
3. 두 번째와 세번째 숫자는 동일
'''

import sys
input = sys.stdin.readline

arr = []
for _ in range(4):
    arr.append(int(input()))

if arr[1] == arr[2]:
    if arr[0] + arr[3] == 16 or arr[0] + arr[3] == 17 or arr[0] + arr[3] == 18:
       print("ignore") 
    else:
        print("answer")
else:
    print("answer")