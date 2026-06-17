# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#           val 是小朋友的名字/身高，next 是他右手拉着的下一个人
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. 创造一个“假人/道具人” dummy，用来给新队伍当临时起点
        dummy = ListNode()

        # 2. 派一个带队老师 tail（队尾指针），一开始站在 dummy 身边
        tail = dummy

        # 3. 游戏开始：只要一班（l1）和二班（l2）都还有人，就继续比身高
        while list1 and list2:
            if list1.val < list2.val:
                # 一班的排头比较矮，老师（tail）右手拉住他，让他进新队伍
                tail.next = list1
                # 一班排头进队了，一班队伍往前移，换下一个人当排头
                list1 = list1.next
            else:
                # 二班的排头比较矮，老师（tail）右手拉住他，让他进新队伍
                tail.next = list2
                # 二班排头进队了，二班队伍往前移，换下一个人当排头
                list2 = list2.next

            # 无论是谁进队，带队老师（tail）都要往前移一步，站到新进队那个人的身边（成为新队尾）
            tail = tail.next

        # 4. 神奇的捡漏（注意：这部分在 while 循环外面）
        # 走到这里，代表其中一队已经全部进队了（变空了）
        if list1:
            # 如果一班还有剩人，因为他们原本就排好序了，老师不用再比了，直接整串接在队尾后面
            tail.next = list1
        elif list2:
            # 如果二班还有剩人，同理，直接把二班整串接在队尾后面
            tail.next = list2

        # 5. 游戏结束，dummy 只是工具人，它后面带起的队伍（dummy.next）才是我们要的完整新队伍
        return dummy.next