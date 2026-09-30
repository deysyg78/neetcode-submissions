from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
       seen = defaultdict(list)

       for value in strs:
        arr = [0]*26
        for char in value:
            arr[ord(char)-ord("a")]+=1
        key = tuple(arr)
        seen[key].append(value)
       solution = seen.values()
       return list(solution)



