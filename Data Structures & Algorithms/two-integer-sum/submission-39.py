class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # we can optimize the above solution using a hash map.
         # lets find the complement value of the pair of sum using the target value - the curr value in the loop
         # storing the index of the values as the hash key values.
        seen={}
        

        for i,val in enumerate(nums):
            complement=target-val
            
            if complement in seen:
                return[seen[complement],i]
            seen[val]=i
        
        return []
           
        
               
  
        
        
        #first we can use brue force solution 
        #iterating through the ist of int and comparing each one with one another to see if they add up to the target
"""
        for i in range(len(nums)):
            for j in range(len(nums)-1,-1,-1):
                total =nums[i]+nums[j]
                if total == target and (i!=j):
                    return [i,j]
                
"""
        # we can optimize the above solution using a hash map.
      

        


       


        

        
