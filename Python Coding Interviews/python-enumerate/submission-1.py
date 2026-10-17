from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i, n in enumerate(nums):
        if n == 7:
            return i
    return -1
    pass


def get_dist_between_sevens(nums: List[int]) -> int:
    last_seven_index = None
    current_seven_index = None
    distance = None
    for i, n in enumerate(nums):
        if n == 7 and last_seven_index is None:
            last_seven_index = i
        elif n == 7 and last_seven_index is not None:
            current_seven_index = i
            distance = current_seven_index - last_seven_index
            return distance
    pass


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
