'''문자열 배열을 받아 애너그램 단위로 그룹핑하라.'''

# dictonary에 append를 하면 문자열이 추가되고 +=로 넣으면 문자 하나씩 추가된다.

import collections

class Solution:
    def groupAnagrams(self, strs):
        dic = collections.defaultdict(list)
        for i in strs:
            i_sort = ''.join(sorted(i))
            dic[i_sort].append(i)

        return dic.values()