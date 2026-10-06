class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1={}
        count2={}

        for i in s:
            if i in count1:
                count1[i]+=1
            else:
                count1[i]=1
        for i in t:
            if i in count2:
                count2[i]+=1
            else:
                count2[i]=1
        return count1==count2