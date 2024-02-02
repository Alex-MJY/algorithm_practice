'''
n개의 카드. 

앞면 : m개에는 O가 적혀있고 n - m개에는 X가 적혀있다.

뒷면에도 적고 싶음. O는 k개, X는 n - k개

앞 면과 뒷 면에 같은 모양이 적혀있는 카드의 최대 개수를 구하는 프로그램을 작성하시오.



n = 5, m = 3, k = 3

front / m:O : 3, n - mX : 2
back / k:O : 3, n - kX : 2


4, 3, 2
front / o:3, x:1
back / o:2, x:2
'''

n, m, k = map(int, input().split())

print(min(m, k) + min((n - m), (n - k)))