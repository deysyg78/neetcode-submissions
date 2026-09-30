class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        


        # brute force : sort the string first 
        #return sorted(s) == sorted(t)# (nlogn)
        # two dictionary solution
        # count(s)==count(t)
        # iterte through both comparing both and figuring out if they are angram
        seen = {}


        # iterate through the values of s
        # s= "racecar" 
        # t="carrace"
        # seen = {r:0,a:0,c:0,e:0}
        for i in range(len(s)):
            seen[s[i]] = 1 + seen.get(s[i],0)
        for i in range(len(t)):
            if t[i] not in seen:
                return False
            seen[t[i]] -= 1
            if seen[t[i]] == 0:
                del seen[t[i]]
        return len(seen) == 0







