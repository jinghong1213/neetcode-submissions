# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        low, high = 1, n

        # 只要包围圈（下限 low 和 上限 high）还合法，游戏就继续
        while low <= high:
            # 每次都猜正中间的那个数字
            mid = (low + high) // 2

            res = guess(mid)  # 💡 正确做法：只调用一次，把结果存进变量 res

            if res > 0:
                # 系统返回 1，代表你猜的 mid 太小了，答案在右边
                # 下限老师往右大跨步，跳到 mid + 1
                low = mid + 1

            elif res < 0:
                # 系统返回 -1，代表你猜的 mid 太大了，答案在左边
                # 上限老师往左大退步，跳到 mid - 1
                high = mid - 1

            else:
                # 系统返回 0，刚好猜中！
                return mid

        # 走出循环代表找完了都没找到（虽然这题保证一定能猜中）
        return -1