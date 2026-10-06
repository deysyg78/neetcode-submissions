class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we could store values in an empty dict to keep track of total count in array
        temp={}
        #iterate through the array of nums and then store each val 
        for i in nums:
            if i in temp:
                temp[i]+=1
            else:
                temp[i]=1
        
        for i, element in temp.items():
            if element>=2:
                return True
        return False
        