'''jewels는 보석이며, stones는 갖고 있는 돌이다. S에는 보석이 몇개나 있을까? 대소문자는 구분한다.'''

# 해시 테이블을 이용한 풀이
# 갖고 있는 stones의 개수를 모두 헤아린 후, jewels의 각 요소를 키로 하는 각 개수를 합산하면 된다.
# freqs 해시테이블 변수에 stones를 문자 단위로 하나씩 분리해 넣어주고 카운팅한다.
# 해당 문자의 빈도 수를 더해서 리턴한다.
class Solution1:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0

        # stones의 빈도 수 계산
        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        # jewels의 빈도 수 합산
        for char in jewels:
            if char in freqs:
                count += freqs[char]
        return count


# defaultdict를 사용해 존재하지 않는 키에 대해 디폴트를 리턴하면 코드 길이를 줄일 수 있다.
import collections

class Solution2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        # stones의 빈도 수 계산
        for char in stones:
            freqs[char] += 1

        # jewels의 빈도 수 합산
        for char in jewels:
            count += freqs[char]

        return count
    
# Counter로 계산 생략
class Solution3:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0
        for char in jewels:
            count += freqs[char]
        return count
    
    
# pythonic
class Solution4:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)