class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # creating a dictionary empty for counting purposes
        seen = {}

        # iterate through all values of list nums
        #.        1  1  1. 1
        # nums = [1, 2, 3, 4]

        for values in nums:
            if values not in seen:
                seen[values] = 1
            elif values in seen:
                seen[values] += 1
                
            if seen.get(values, 0) > 1:
                return True
        return False
