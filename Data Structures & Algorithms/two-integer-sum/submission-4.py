class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # given : array , target num,
       # return : i,j index
       # nums[i] + nums[j] == target
       # i!= j
       #.             V
       #  nums = [3,4,5,6] 
       

       for i in range(len(nums)):
        for j in range(1,len(nums)):
            if ((nums[i] + nums[j]) == target )and i!=j:
                return [i,j]
            else:
                continue



        

        
