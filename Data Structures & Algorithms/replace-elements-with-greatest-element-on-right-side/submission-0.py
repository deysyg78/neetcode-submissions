class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element=0

        # start max=-1
        # reversed iteration
        # new max = max(old max,arr[i])
        max_val=-1

        for i in range(len(arr)-1,-1,-1):
            new_max=max(max_val,arr[i])
            arr[i]=max_val
            max_val=new_max
                
        return arr

          
            