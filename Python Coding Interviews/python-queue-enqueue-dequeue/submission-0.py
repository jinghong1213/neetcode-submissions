from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue = deque(arr)
    rotate_queue = []
    first_queue_till_k = []

    for i in range(k):
        first_queue_till_k.append(queue.popleft()) 

    for k in range(len(queue)):
        rotate_queue.append(queue.popleft())

    done_queue = rotate_queue + first_queue_till_k
    return deque(done_queue)


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
