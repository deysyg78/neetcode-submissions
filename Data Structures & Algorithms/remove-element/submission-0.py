class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # iterate through arr to find all values not equal to val
        # replace with self if currval not equal to input val
        # ex: Input: nums = [0,1,2,2,3,0,4,2], val = 2
        #                        ^
        k=0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
            