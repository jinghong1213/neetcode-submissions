# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# ==========================================
        # 1. Iterative Solution（迭代解法：带队老师在原地换拉手）
        # ==========================================

        # prev 老师代表“刚刚已经换好方向、站在后面的小朋友”（一开始后面没人，所以是 None）
        # curr 老师代表“当前正在转圈的小朋友”（从排头的 head 开始）
        prev, curr = None, head

        # 只要当前还有小朋友需要转身，游戏就继续
        while curr:
            # 【第 1 步】大喊：“下一个小朋友（curr.next）你先别跑，拿个绳子牵着！”
            # 用 nxt 老师把后面的队伍死死抓紧，不让队伍断掉
            nxt = curr.next

            # 【第 2 步】当前小朋友（curr）松开原本拉着右边的手，转过身，把手拉向后面的 prev 老师
            curr.next = prev

            # 【第 3 步】接力赛交棒：prev 老师往前移一步，站到当前这个换好方向的小朋友这里
            prev = curr

            # 【第 4 步】curr 老师也往前移一步，走到刚刚被 nxt 老师抓着的下一个小朋友那里，准备下一轮转身
            curr = nxt

        # 当所有人都换好方向，curr 会变成 None。此时站在最前面的就是 prev 老师（也就是原本的队尾，现在的队头）
        return prev

        # ==========================================
        # 2. Recursive Solution（递归解法：把责任层层往下推）
        # ==========================================
        # （注：以下代码被多行注释起来了，如果要跑递归，需要把上面的迭代代码删掉/注释掉，并把这里解开）
        """
        # Base Case（终止条件）：如果队伍是空的，或者只剩一个人，根本不用倒转，直接交上去
        if not head or not head.next:
            return head

        # Recursive Step（递归交棒）：当前的小朋友（head）偷懒，大喊：
        # “后面的排头（head.next），你们先把身后的队伍完美倒转好拿给我！”
        # new_head 会一路传到最老大的那个新队头（也就是原本的最后一个节点）
        new_head = self.reverseList(head.next)

        # Post-processing（倒序收尾的神奇 2 行代码）：
        # 此时后面的队伍已经倒转好了，但【我后面那个人】的右手还在放空。
        # head.next.next = head ➡️ 意思就是：“让我后面那个人转过来，拉住我的手！”（形成互相拉手）
        head.next.next = head
        
        # head.next = None ➡️ 意思就是：“我自己松开原本指向他的手，放空。”（成功把我自己断后，接在最后面）
        head.next = None

        # 把新队伍的老大（new_head）继续往上传
        return new_head
        """