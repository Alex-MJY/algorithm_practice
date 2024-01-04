# import sys
# a = str(sys.stdin.readline()) 
# 👉 sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아집니다. 
# input()과 같은 값을 얻으려면 1을 빼야 한다.
s = str(input())
print(len(s))