# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        # Implementation of Quick Sort
        return self.quickSortHelper(pairs, 0, len(pairs) - 1)

    def quickSortHelper(self, pairs, s, e):

        if ((e - s + 1) <= 1):
            return pairs

        pivot = pairs[e] # pivot is the last element
        left = s # pointer for left side

        # Partition: elements smaller than pivot on left side
        for i in range(s, e): # not include e cause e is the pivot, if include e need e + 1
            if (pairs[i].key < pivot.key):
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left += 1
        
        # Move pivot in-between left & right sides
        pairs[e] = pairs[left]
        pairs[left] = pivot

        # Quick sort left side
        self.quickSortHelper(pairs, s, left - 1)

         # Quick sort right side
        self.quickSortHelper(pairs, left + 1, e)

        return pairs
