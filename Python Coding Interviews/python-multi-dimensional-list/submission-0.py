from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    arr_temp=[]
    for j,sublist in enumerate(nested_arr):
        for i, element in enumerate(sublist):
            if i==-1:
                break
            
        arr_temp.append(max(sublist))
    return arr_temp
    

    pass


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
