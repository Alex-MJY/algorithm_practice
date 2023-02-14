import collections

class Solution:
    def groupAnagrams(self, strs: str) -> str:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()
    
'''
anagram을 판단하는 가장 간단한 방법은 정렬하여 비교하는 것이다.
sorted()는 문자열도 잘 정렬하며 결과를 리스트 형태로 리턴하는데, 
이를 다시 키로 사용하기 위해 join()으로 합친다.
애너그램끼리는 같은 키를 갖게 되고 여기에 append()하는 형태가 된다.

dictionary에서 key가 없는 상태에서 value를 추가하면 KeyError가 발생한다.
즉, dict[key] = 0으로 초기화를 해줘야 한다.
collections.defaultdict()로 선언하면 에러 없이 사용할 수 있다.
'''