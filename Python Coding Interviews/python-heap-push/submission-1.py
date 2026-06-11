import heapq
from typing import List


def heap_push(heap: List[int], value: int) -> int:
    
    #min_heap = []
    #heapq.heappush(min_heap, value)

    #for count in heap:
    #    heapq.heappush(min_heap, count)

    #return min_heap[0]

    heapq.heappush(heap, value)
    return heap[0]

# do not modify below this line
print(heap_push([1, 2, 3], 4))
print(heap_push([1, 2, 3], 0))
print(heap_push([1, 2, 3], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 5))
