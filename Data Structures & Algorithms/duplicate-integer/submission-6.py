class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count={}
        ans=0

        for val in nums:
            count[val] = count.get(val,0) +1
        for val in count.values():
            if val>1:
                return True
        return False


