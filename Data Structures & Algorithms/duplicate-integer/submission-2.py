class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums = [1, 2, 3, 3]
        # seen = {
        #   1:1
        #.  2:1
        #.  3:2 
        #}
        #

        seen={}

        for val in nums:
            seen[val] = seen.get(val,0) + 1
        for i in seen.values():
            if i > 1:
                return True 
        return False


        


