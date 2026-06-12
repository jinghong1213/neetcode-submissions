class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_val = -1
        tmp = 0

        for i in range(len(arr) - 1, -1, -1):   # start, stop(before -1, so stop at 0), step (decrement)
            tmp = arr[i]
            arr[i] = max_val
            max_val = max(max_val, tmp)
        
        return arr

