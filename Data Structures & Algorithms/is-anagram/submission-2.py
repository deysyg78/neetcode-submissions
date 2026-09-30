class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t) 

        # nlogn time and space O(n)  creating new list^^

        # setting up a dictionary count number of occurences 

        #s = "racecar" : t = "carrace"
        # seen ={r:2,a:2,c:2,e:1}  

        seen = {}

        for value in s:
            seen[value] = 1+ seen.get(value,0)
        for value in t:
            seen[value] = seen.get(value,0) -1
            if seen[value] == 0:
                del seen[value]
            else:
                continue
        if seen=={}:
            return True
        else:
            return False











