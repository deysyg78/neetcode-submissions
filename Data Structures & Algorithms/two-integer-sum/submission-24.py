class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #first we can use brue force solution 
        #iterating through the ist of int and comparing each one with one another to see if they add up to the target
        for i in range(len(nums)):
            for j in range(len(nums)-1,-1,-1):
                total =nums[i]+nums[j]
                if total == target and (i!=j):
                    return [i,j]
    

       


        

        
