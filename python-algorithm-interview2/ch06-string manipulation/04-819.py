'''금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.'''

# 입력값에 대소문자가 섞여있고 쉼표 등 구두점이 존재하기 때문에, 필터링(데이터 클렌징)이 필요 == 정규식 사용하면 쉽게 가능
# 정규식 \w는 모든 단어 문자를 의미하며, ^은 not을 의미

import collections
import re


class Solution1:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        return max(counts, key = counts.get)


# Counter의 most_common을 이용해 더 쉽게 풀 수 있다
class Solution2:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
        