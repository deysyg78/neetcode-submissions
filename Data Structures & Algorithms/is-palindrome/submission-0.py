import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #                   v
        #.                 v  
        # s = "Was it a car or a cat I saw?"
        # - any pointer needs to point at its first alphanumrtic char
        # isalnum() - returns true is element/s are alphanumeric

        l,r = 0, len(s)-1
        # we want to move pointers to the center of the string 

        while l < r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True

        





        

        
        

      

   


