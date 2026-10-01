from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    new_list=arr1+arr2
    return new_list
    pass


def pop_n(arr: List[int], n: int) -> List[int]:
    # n = the nth amount of elents popped from list
    removed_count=0
    for i in range(len(arr))[::-1]:
        if n>len(arr):
            return []
        arr.pop(i)
        removed_count+=1
        if removed_count==n:
            return arr
    pass


def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    if index <= len(arr):
        arr.insert(index,element)
    elif index>len(arr):
        arr.insert(len(arr),element)
    return arr
    pass


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2)) # rmoves index 3&4
print(pop_n([1, 2, 3, 4, 5], 6)) #rmoves index 1,2,3,4,5,6 (returns empty list)
print(pop_n([1, 2, 3, 4, 5], 5)) #rmoves all

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
