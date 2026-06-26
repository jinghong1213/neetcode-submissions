class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force way: nums.sort()
        # range: 0 - 2
        
        """
        # Solve using BucketSort

        counts = [0] * 3
        
        for num in nums:
            counts[num] += 1

        
        i = 0
        for n in range(0, len(counts)):
            for _ in range(0, counts[n]):
                nums[i] = n
                i += 1

        
        return nums
        """

        # Solve using Three Pointers

        # l 是 0 的地盘(左边界)； r 是 2 的地盘(右边界)
        l = 0
        r = len(nums) - 1
        i = 0  # i 是负责巡逻的老师，从 Index 0 开始看起

        # 两个位置互换的小工具
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        # 只要巡逻老师还没踩到 2 的地盘，游戏就继续
        while i <= r:
            if nums[i] == 0:
                # 看到 0，扔去左边 l 的位置
                swap(l, i)
                l += 1  # 0 的地盘往右挪一格
                # 后面会自动执行 i += 1，巡逻老师去看下一个
            elif nums[i] == 2:
                # 看到 2，扔去右边 r 的位置
                swap(i, r)
                r -= 1  # 2 的地盘往左缩一格
                i -= 1  # 留在原地！防止刚从右边换过来的未知数字被漏掉检查

            i += 1  # 巡逻老师往前走一步