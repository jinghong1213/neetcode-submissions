# Doubly Linked List Node
class Node:
        def __init__(self, value):
            self.value = value
            self.next = None  # 右手拉着下一个人
            self.prev = None  # 左手拉着上一个人

class Deque:
    
    def __init__(self):
# 1. 创造两尊固定不动的门神/石雕：head（左石雕）和 tail（右石雕），名字统一叫 -1
        self.head = Node(-1)
        self.tail = Node(-1)

        # 2. 一开始队伍是空的，两尊石雕面对面，互相拉紧对方的手
        self.head.next = self.tail  # 左石雕右手 ➡️ 拉着右石雕
        self.tail.prev = self.head  # 右石雕左手 ➡️ 拉着左石雕

    def isEmpty(self) -> bool:
        # 如果左石雕的右手拉着的依然是右石雕，就说明中间没有真正的学生，队伍是空的
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        # 目标：从队伍的“最后面”（右边）加人
        new_node = Node(value)  # 新学生手拉手进场

        # 找出目前排在最后面的那个真正学生（右石雕左手拉着的那个人）
        last_node = self.tail.prev

        # 插队连线（4条线接好）：
        last_node.next = new_node  # 原本最后学生的右手 ➡️ 拉住新学生
        new_node.prev = last_node  # 新学生的左手 ➡️ 拉住原本最后的学生
        new_node.next = self.tail  # 新学生的右手 ➡️ 拉住右石雕
        self.tail.prev = new_node  # 右石雕的左手 ➡️ 转过来拉住新学生

    def appendleft(self, value: int) -> None:
        # 目标：从队伍的“最前面”（左边）插队加人
        new_node = Node(value)

        # 找出目前排在第一名的真正学生（左石雕右手拉着的那个人）
        first_node = self.head.next

        # 插队连线（4条线接好）：
        self.head.next = new_node  # 左石雕的右手 ➡️ 转向拉住新学生
        new_node.prev = self.head  # 新学生的左手 ➡️ 拉住左石雕
        new_node.next = first_node  # 新学生的右手 ➡️ 拉住原本的第一名
        first_node.prev = new_node  # 原本第一名的左手 ➡️ 转过来拉住新学生

    def pop(self) -> int:
        # 目标：把队伍“最后面”（右边）的那个学生赶走，并拿回他的名字
        if self.isEmpty():
            return -1  # 没人排队，赶不到人，返回 -1

        # 找到最后面的那个倒霉蛋学生
        target_node = self.tail.prev
        value = target_node.value  # 悄悄记下他的名字，等下要退还
        prev_node = target_node.prev  # 找到倒霉蛋左边的那个人

        # 踢人：让倒霉蛋左边的人和右边的右石雕“跨过他”直接拉手
        prev_node.next = self.tail  # 左边人的右手 ➡️ 直接拉向右石雕
        self.tail.prev = prev_node  # 右石雕的左手 ➡️ 直接拉向左边人

        return value  # 成功把人赶走，把名字交回去

    def popleft(self) -> int:
        # 目标：把队伍“最前面”（左边）的第一个学生赶走，并拿回他的名字
        if self.isEmpty():
            return -1  # 空队伍，没人可赶

        # 找到排在第一名的那个倒霉蛋学生
        target_node = self.head.next
        value = target_node.value  # 记下名字
        next_node = target_node.next  # 找到倒霉蛋右边的那个人（第二名）

        # 踢人：让左石雕和第二名学生直接拉手，把第一名孤立出来
        self.head.next = next_node  # 左石雕的右手 ➡️ 直接拉向第二名
        next_node.prev = self.head  # 第二名的左手 ➡️ 直接拉向左石雕

        return value  # 成功赶走，返回名字