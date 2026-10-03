from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue=deque(arr)
    temp=deque()
    count=0

    for i in range(len(arr)):
        if count<k:
            curr=queue.popleft()
            count+=1
            temp.append(curr)
    for i in temp:
        queue.append(i)
    
   
    return queue
    
    pass



# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
