class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # need to reset counter
        # case if current counter is max then prev reset.
        # find maximum consecutive ones
        count=0
        best=0

        for n in nums:
            if n==1:
                count+=1
                best=max(count,best)
            else:
                count=0
         
        return best

        

