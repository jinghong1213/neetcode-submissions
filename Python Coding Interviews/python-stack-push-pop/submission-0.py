from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    reverse_arr = []
    for i in range(len(arr)):
        reverse_arr.append(arr.pop())

    return reverse_arr    


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
