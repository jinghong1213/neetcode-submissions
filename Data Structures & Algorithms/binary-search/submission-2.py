class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 一开始，包围圈锁住整张数组
        L, R = 0, len(nums) - 1  # R = length of array - 1, can prevent overflow

        # 只要包围圈还合法（左边界没跑到右边界的右边），就继续找
        while L <= R:
            # 找到当前包围圈的正中间位置
            mid = (L + R) // 2

            if target > nums[mid]:
                # 目标比中间的数还要大，说明在右半区
                # 左边界老师移到 mid 右边，把左半区丢掉
                L = mid + 1

            elif target < nums[mid]:
                # 目标比中间的数还要小，说明在左半区
                # 右边界老师移到 mid 左边，把右半区丢掉
                R = mid - 1

            else:
                # 刚好 nums[mid] == target，抓到了！
                return mid

        # 走出循环代表包围圈空了都没找到
        return -1