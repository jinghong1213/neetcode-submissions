class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0]*self.capacity    # O(n), n = capacity

    def get(self, i: int) -> int:
        return self.arr[i]      # O(1)

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n     # O(1)

    # O(1) - Avg case / Amortized
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()       # O(n) due to resizing calling constructor
        
        self.arr[self.size] = n        
        self.size += 1

    # O(1)
    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size] 

    # O(n)
    def resize(self) -> None:
        self.capacity = 2*self.capacity
        new_arr = [0]*self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    # O(1)
    def getSize(self) -> int:
        return self.size
    
    # O(1)
    def getCapacity(self) -> int:
        return self.capacity
