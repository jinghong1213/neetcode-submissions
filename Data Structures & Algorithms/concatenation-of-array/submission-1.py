class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0]*2*n

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        
        #for i, num in enumerate(nums):
        #    ans[i] = ans[i + n] = num

        return ans
