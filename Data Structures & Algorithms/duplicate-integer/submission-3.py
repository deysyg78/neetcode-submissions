class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        """
        {
            1:1
            2:1
            3:2
        }
        """
        for n in nums:
            seen[n] = seen.get(n,0) + 1
        for count in seen.values():
            if count > 1:
                return True
        return False




