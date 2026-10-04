import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    n=heapq.nsmallest(1,arr)
    return n[0]
    pass


def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    return heapq.nsmallest(4,arr)
    pass


def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    arr1=heapq.nsmallest(2,arr)
    
    max_heap=[-x for x in arr1]
    heapq.heapify(max_heap)
    ans=[]
    while max_heap:
        ans.append(-heapq.heappop(max_heap))
   

        
    return ans

    pass


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

