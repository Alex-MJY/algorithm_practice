'''
Data Cleaning이라 불는 입력값에 대한 preprocessing 작업이 필요하다. 
편리하게 처리하기 위해 정규식을 섞어 사용한다.


정규식에서 \w는 word character를, ^은 not을 의미한다. 단어 문자가 아닌 모든 문자를 공백으로 치환(substitute)하는 역할을 한다.

단어의 개수는 defaultdict()를 사용해 int 기본값이 자동으로 부여되게 했다.


Counter는 해시 가능한 객체를 세기 위햔 dict 서브 클래스. 요소와 개수가 딕셔너리로 저장. 
Counter.most_common()은 내림차순 리스트를 반환. most_common(1)은 한개의 값을 리스트에 저장.
https://docs.python.org/ko/3/library/collections.html#collections.Counter
'''

import re
import collections

class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                 if word not in banned]
        
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
        
        