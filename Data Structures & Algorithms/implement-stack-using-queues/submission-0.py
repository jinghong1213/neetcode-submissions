class MyStack:

    def __init__(self):
        # 真正创造一个空的双端队列（Queue）来当我们的普通队伍
        self.q = deque()

    def push(self, x: int) -> None:
        # 【第 1 步】不管三七二十一，先把新学生 x 加到队伍的最后面
        self.q.append(x)

        # 【第 2 步】接力赛开始！
        # 我们把新学生“前面”的所有人，一个一个从排头叫出来，重新排到队伍最后面。
        # 这样刚刚进来的新学生 x，就会慢慢被推到整个队伍的最前面（排头）！
        for _ in range(len(self.q) - 1):
            # 把排头的人抓出来，塞去队尾
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # 因为在 push 的时候，最后进来的新学生已经被我们完美送到了“排头”
        # 所以 Stack 的 pop（拿走最新的），在这里刚好就是直接拿走 Queue 的排头！
        return self.q.popleft()

    def top(self) -> int:
        # 同样的道理，最新的元素就在最前面
        return self.q[0]

    def empty(self) -> bool:
        # 只要队伍的人数是 0，就是空的
        return len(self.q) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()