from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # seen = {"act":,"pots":,"tops":,"cat":,"stop":,"hat":}
        # act:["act",cat]  if presented "cat" how would I know it is in same group ??
        # pots:["pots"]
        #keeping a dictionary wich we have the keys be arbitrary word so that
        # each group can be identified via key
        # 1 option::sorted key identifier for keys in dictionaries... and group that is equal to the key once sorted??
        #

        seen = defaultdict(list)

        for value in strs:
            lst = [0]*26
            for char in value:
                lst[ord(char)-ord("a")]+=1
            key = tuple(lst)
            seen[key].append(value)
        solution = seen.values()
        return list(solution)
# nlogn time complexity and space O(n)

#instead of sorting all words - we can keep tack the number 
#of occurences of each character for each element 



