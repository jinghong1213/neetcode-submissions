class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None  # 右手拉着下一个人
        self.prev = None  # 左手拉着上一个人


class MyLinkedList:

    def __init__(self):
        # 1. 创造左右两尊不动的“石雕”
        self.left = ListNode(0)
        self.right = ListNode(0)

        # 2. 让两尊石雕一左一右互相拉好手
        self.left.next = self.right  # 左石雕右手拉着右石雕
        self.right.prev = self.left  # 右石雕左手拉着左石雕

    def get(self, index: int) -> int:
        # 从左石雕右手拉着的第一个“真正学生”开始数起
        cur = self.left.next

        # 只要还没走到尽头，而且还没数到我们要的 index，就一直往右走
        while cur and index > 0:
            cur = cur.next
            index -= 1

        # 如果找到了，而且它不是右边那尊石雕，就返回他的名字（val）
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1  # 找不到就给 -1（比如 index 太大超出队伍）

    def addAtHead(self, val: int) -> None:
        # 目标：塞一个新学生到“左石雕”的屁股后面（成为第一个真正的学生）
        # 先打听好：新学生（node）、原本排第一的学生（next）、左石雕（prev）
        node, next, prev = ListNode(val), self.left.next, self.left

        # 开始连线（4条线必须全部接好）：
        prev.next = node  # 左石雕的右手 ➡️ 拉住新学生
        next.prev = node  # 原本第一名的左手 ➡️ 拉住新学生
        node.next = next  # 新学生的右手 ➡️ 拉住原本的第一名
        node.prev = prev  # 新学生的左手 ➡️ 拉住左石雕

    def addAtTail(self, val: int) -> None:
        # 目标：塞一个新学生到“右石雕”的前面（成为最后一个真正的学生）
        # 先打听好：新学生（node）、右石雕（next）、原本最后的学生（prev）
        node, next, prev = ListNode(val), self.right, self.right.prev

        # 开始连线：
        prev.next = node  # 原本最后的右手 ➡️ 拉住新学生
        next.prev = node  # 右石雕的左手 ➡️ 拉住新学生
        node.next = next  # 新学生的右手 ➡️ 拉住右石雕
        node.prev = prev  # 新学生的左手 ➡️ 拉住原本最后的

    def addAtIndex(self, index: int, val: int) -> None:
        # 目标：数到指定的 index，把新学生塞在那个位置的前面
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        # 找到了那个位置的学生（cur）
        if cur and index == 0:
            # 此时：新学生是 node、原位置的学生是 next、他前面的人是 prev
            node, next, prev = ListNode(val), cur, cur.prev

            # 强行插队，4条线接好：
            prev.next = node  # 前面人的右手 ➡️ 拉新学生
            next.prev = node  # 原位置人的左手 ➡️ 拉新学生
            node.next = next  # 新学生的右手 ➡️ 拉原位置人
            node.prev = prev  # 新学生的左手 ➡️ 拉前面人

    def deleteAtIndex(self, index: int) -> None:
        # 目标：找到那个倒霉的学生，把他从队伍里踢走
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        # 找到了那个要被踢的学生（cur），且确保他不是右石雕
        if cur and cur != self.right and index == 0:
            # 打听好他右边的人（next）和左边的人（prev）
            next, prev = cur.next, cur.prev

            # 踢人绝招：让他左边的人和右边的人“跨过他”直接手拉手！
            next.prev = prev  # 右边人的左手 ➡️ 直接拉向左边人
            prev.next = next  # 左边人的右手 ➡️ 直接拉向右边人
            # 这样 cur 就完全被孤立，从队伍里消失了！

            
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)