import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    #temp_heap=storing all the values of least priority in order
    temp_heap=[]
    for i in range(len(heap)):
        temp_heap.append(heapq.heappop(heap))
    return temp_heap

    pass
    # time complexity for heapq.heapppop() is O(log(n)) where n is the num of elements in the heap


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
