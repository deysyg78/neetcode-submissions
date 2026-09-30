class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        


        # brute force : sort the string first 
        # iterte through both comparing both and figuring out if they are angram
        if len(t) != len(s):
            return False
        countS,countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[t[i]] = 1+countT.get(t[i],0)
        return countS == countT


# O (nlongn + mlogm) 