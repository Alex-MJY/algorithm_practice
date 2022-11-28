import collections

class Solution:
    def groupAnagrams(self, strs: str) -> str:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()