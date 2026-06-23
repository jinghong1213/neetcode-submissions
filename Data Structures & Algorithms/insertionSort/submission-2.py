# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

            res = []

            for i in range(len(pairs)): 
                j = i - 1
                                            #Example: 3, 2, 5, 1
                while (j >= 0 and pairs[j + 1].key < pairs[j].key): #从2开始，如果2小过3
                    tmp = pairs[j + 1]    #先存2的value去tmp
                    pairs[j + 1] = pairs[j] #把3移去2的位置
                    pairs[j] = tmp  #把2移去之前3的位置
                    j -= 1   # j - 1 so that可以继续compare 2和上一个，如果没有上个了就去下个for loop check
                
                res.append(list(pairs))

            return res

