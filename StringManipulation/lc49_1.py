import collections

class Solution:
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            
        return anagrams.values()
        
        

a = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(a.groupAnagrams(strs)) 


       