from typing import List


def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    out_of_bounds=False
    for i ,sublist in enumerate(grid):
        for j, val in enumerate(sublist):
            if len(sublist)<=c:
                return out_of_bounds
            if len(grid)<=r:
                return out_of_bounds

    return True
    pass


# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3)) # this use case would be the reason for checking columns as well
