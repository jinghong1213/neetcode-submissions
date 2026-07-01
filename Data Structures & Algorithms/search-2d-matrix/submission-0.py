class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # 获取矩阵的总行数（ROWS）和总列数（COLS）
        ROWS, COLS = len(matrix), len(matrix[0])

        # ==========================================
        # 【第一阶段】二分查找：锁定在哪一行
        # ==========================================
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2

            # matrix[row][-1] 是当前行最右边、最大的数
            if target > matrix[row][-1]:
                top = row + 1  # 目标更大，往更下面的行去找

            # matrix[row][0] 是当前行最左边、最小的数
            elif target < matrix[row][0]:
                bot = row - 1  # 目标更小，往更上面的行去找

            else:
                # 目标被夹在这一行的最小值和最大值之间，说明找对行了！
                break

        # 如果找了一圈发现 top > bot，说明目标根本不在矩阵的数值范围内
        if not (top <= bot):
            return False

        # ==========================================
        # 【第二阶段】二分查找：在锁定好的那一行里找数字
        # ==========================================
        row = (top + bot) // 2  # 刚才锁定好的那一行
        l, r = 0, COLS - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[row][mid]:
                l = mid + 1  # 目标在右边
            elif target < matrix[row][mid]:
                r = mid - 1  # 目标在左边
            else:
                return True  # 找到了！

        # 【注意这里的缩进！】只有等整个 while 循环彻底找完了都没找到，才可以说 False
        return False