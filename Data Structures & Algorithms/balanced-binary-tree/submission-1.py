# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            # 1. 如果底下已经没有积木了（空节点）
            # 城堡当然不会倒 [没倒 (True), 高度是 0]
            if not root:
                return [True, 0]

            # 2. 问问左边和右边的小朋友：你们那边的积木怎么样啦？
            left = dfs(root.left)  # 左边的汇报
            right = dfs(root.right)  # 右边的汇报

            # 3. 检查城堡会不会倒：
            # - 左边的积木没倒？ (left[0])
            # - 右边的积木没倒？ (right[0])
            # - 左右两边的高度差是不是最多只差 1 块？ (abs(left[1] - right[1]) <= 1)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # 4. 算算我现在这层总共有多高：
            # 拿左边和右边比较高的那一边，再加上我自己这 1 块积木
            my_height = 1 + max(left[1], right[1])

            # 5. 打包好，向上汇报：[我这里有没有倒, 我的总高度]
            return [balanced, my_height]

        # 拿着最顶上（根节点）的汇报结果，看看整座城堡到底有没有倒 [0]
        return dfs(root)[0]


