import heapq
from typing import List


def heap_push(heap: List[int], value: int) -> int:
    #implementing min-heap: smallest priority val will always be on top of the heap or,in other words, in index 0
    #heap=[]
    heapq.heappush(heap,value)
    return heap[0] 

    # time complexity of heapq.heappush() is O(lon(n)) where n is the num of elements in heap
    # time complexity of accessing an element w/ smallest priority  is O(1) since  indexing into a list is O(1)
    #space complexity is O(n), where n is the number of the elements in a heap
    pass


# do not modify below this line
print(heap_push([1, 2, 3], 4))
print(heap_push([1, 2, 3], 0))
print(heap_push([1, 2, 3], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 5))
